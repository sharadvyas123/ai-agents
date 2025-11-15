from langgraph.graph import StateGraph , START , END
from typing import TypedDict , Annotated 
from langchain_core.messages import BaseMessage , HumanMessage 
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
import sqlite3


llm = ChatGoogleGenerativeAI(model = "models/gemini-2.0-flash", google_api_key="AIzaSyBudd3Ynuiz2JeLQnITpMZWZ2DHGk8pSDw")

class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage] , add_messages]

def chat_node(state : ChatState)->ChatState:
    messages = state['messages']
    response = llm.invoke(messages)

    return {"messages":[response]}


conn = sqlite3.connect(database="chatbot.db" , check_same_thread=False)

checkpointer = SqliteSaver(conn=conn)

graph = StateGraph(ChatState)

graph.add_node("chat_node" , chat_node)
graph.add_edge(START , 'chat_node')
graph.add_edge("chat_node" , END)

chatbot = graph.compile(checkpointer=checkpointer)

def retrive_all_threads():
    all_threads = set()

    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])

    return list(all_threads)
