import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import tools
from llm_setup import llm_with_tools


load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a senior research analyst. Your job is to answer user questions by using the `search_internet` tool
    whenever current or external knowledge is required.
    Do not use internal knowledge for facts that could be outdated.
    Always use the Thought/Action/Observation sequence for every tool invocation.
    If a fact can't be obtained with the available tool, explain why and reason step-by-step."""),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])


# create the agent

agent = create_tool_calling_agent(
    llm=llm_with_tools,
    tools=tools,
    prompt=prompt,
)

# create the executor

research_agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)


query ="What were the main highlights of the recent government updates between india and russia (limit to 2 key points)"

print(f"Running Research Agent for query: {query}\n")

result = research_agent_executor.invoke({"input": query})

print(f"\nFinal Answer: {result['output']}\n")