from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import tool
from langchain import hub
from dotenv import load_dotenv
import requests

load_dotenv()

search_tool=DuckDuckGoSearchRun()

llm=ChatOpenAI()

prompt=hub.pull("hwchase17/react")

agent=create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt
)

agent_executor=AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True
)

response=agent_executor.invoke({"input":"3 ways to reach Goa from Delhi"})

print(response)