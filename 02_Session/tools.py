from pydantic import BaseModel, Field
from langchain_core.tools import BaseTool
from langchain_community.tools import DuckDuckGoSearchResults
from typing import Type

# define pydantic schema for the tools input

class SearchInput(BaseModel):
    """Input schema for the search_internet tool"""

    query: str = Field(
        description="The precise search query to run (example, 'latest news on fusion energy'). Keep it concise and relevant."
    )

    max_results: int = Field(
        default=5,
        description="The maximum number of search results to return(integer between 1 and 10, default is 5).",
    )


# define a tool class

class DuckDuckGoSearchTool(BaseTool):
    name: str = "search_internet"
    description: str = """A free, open-source tool for fetching current, real-world information from
    the web using DuckDuckGo.
    Use this when you need up-to-date facts, news, or external knowledge not in your training data.
"""
    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str, max_results: int = 5):

        ddgs_tool = DuckDuckGoSearchResults(num_results=max_results)
        results = ddgs_tool.run(query)
        print(f"\n[Executing Search: '{query}' | Max Results: {max_results}]\n")

        return results

search_tool = DuckDuckGoSearchTool()
tools = [search_tool]



