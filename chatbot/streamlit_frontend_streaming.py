import streamlit as st
from langchain_core.messages import HumanMessage
from chatbot.langgraph_backend import chatbot

config={"configurable":{"thread_id" : "1"}}

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

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

   

    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk , metadata in chatbot.stream(
            {"messages":[HumanMessage(content=user_input)]} , 
            config={"configurable":{"thread_id" : "1"}},
            stream_mode="messages"
        ))

    st.session_state['message_history'].append({"role" : "assistant" , "content" :ai_message})

