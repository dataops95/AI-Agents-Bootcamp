import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import tools

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

llm_with_tools = llm.bind_tools(tools)


## note: gemini processes the schema in its context window, deciding if/when to output JSON
## if no tool needed, it outputs normal text response.