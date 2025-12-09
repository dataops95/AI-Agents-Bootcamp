# Tools and Structure function calling

Research Agent
- use tools
- search the web


steps

1. structured tools
- problem with simple tools
Thought: I need to multiply 65 and 85
Action: calculate
Action Input: 65 * 85
{
    "field": "age",
    "value": 30
}

LLM: 5 as Five

- structured function calling

schema

llm output:

{
    "tool_name": "search_internet",
    "arguments":{
        "query": "latest news on fusion energy",
        "max_results": 3
    }
}

pydantic -> 

three instead of 3 (int)

2. defining tools with pydantic
- pydantic
- binding tools to llm

3. building the research agent

- agent prompt - ReAct
- agent executor (LCEL)

Assignment

- build 2 more features on top of this research agent
- for ex - i invested in tata stock, give me 2 top updates about the company every day along with the variability score of the stock today
