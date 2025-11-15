import streamlit as st
from langchain_core.messages import HumanMessage
from langgraph_database_backend import chatbot , retrive_all_threads
import uuid


# ****************** utility function ********************
def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def add_thread_id (thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread_id(thread_id)
    st.session_state['message_history'] = []


def load_convo(thread_id):
    return chatbot.get_state(config={"configurable":{"thread_id" : thread_id}}).values['messages']



# ********************* session setup ******************

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

if "thread_id" not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if "chat_threads" not in st.session_state:
    st.session_state['chat_threads'] = retrive_all_threads()


add_thread_id(st.session_state['thread_id'])

# ********************side bar *********************#

st.sidebar.title("Langgrapg Chatbot")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("My Conversation")

for thread_id in st.session_state['chat_threads']:
    if st.sidebar.button(str(thread_id)):
        messages = load_convo(str(thread_id))
        temp_messages = []

        for msg in messages:
            if isinstance(msg , HumanMessage):
                role = "user"
            else :
                role = 'assistant'
            temp_messages.append({'role':role , "content" : msg.content})
        st.session_state['message_history'] = temp_messages


# loading the convo .
for message in st.session_state["message_history"]:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input("Type Here")

if user_input:

    # add
    st.session_state["message_history"].append({"role" : "user" , "content" :user_input})
    with st.chat_message("user"):
        st.text(user_input)

   
    config={"configurable":{"thread_id" : st.session_state['thread_id']}}

    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk , metadata in chatbot.stream(
            {"messages":[HumanMessage(content=user_input)]} , 
            config=config,
            stream_mode="messages"
        ))

    st.session_state['message_history'].append({"role" : "assistant" , "content" :ai_message})

