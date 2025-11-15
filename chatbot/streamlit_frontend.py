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

    response = chatbot.invoke({"messages" : [HumanMessage(content=user_input)]} ,config)

    ai_message = response['messages'][-1].content

    st.session_state['message_history'].append({"role" : "assistant" , "content" :ai_message})
    with st.chat_message("assistant"):
        st.text(ai_message)
