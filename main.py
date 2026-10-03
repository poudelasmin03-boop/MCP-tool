import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage,AnyMessage
import operator
from typing import TypedDict,Annotated
from langgraph.graph import StateGraph,END,START
import psycopg2
from main_client import tavily_mcp_search





### llm
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)