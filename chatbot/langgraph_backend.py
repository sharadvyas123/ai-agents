from langgraph.graph import StateGraph , START , END
from typing import TypedDict , Annotated 
from langchain_core.messages import BaseMessage 
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages


llm = ChatGoogleGenerativeAI(model = "models/gemini-2.0-flash", google_api_key="AIzaSyBudd3Ynuiz2JeLQnITpMZWZ2DHGk8pSDw")

class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage] , add_messages]

def chat_node(state : ChatState)->ChatState:
    messages = state['messages']
    response = llm.invoke(messages)

    return {"messages":[response]}


checkpointer = InMemorySaver()

graph = StateGraph(ChatState)

graph.add_node("chat_node" , chat_node)
graph.add_edge(START , 'chat_node')
graph.add_edge("chat_node" , END)

chatbot = graph.compile(checkpointer=checkpointer)

