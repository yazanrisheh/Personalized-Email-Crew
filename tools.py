from crewai.tools import tool
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()
tavily_client = TavilyClient()

@tool("Tavily Search Tool")
def search_tool(query: str):
    """
    This tool performs advanced searches with a specified query to gather structured and 
    unstructured data. It is particularly useful for prospect research, allowing users to 
    access relevant information about individuals, companies, and industries from multiple 
    sources.
    """
    return tavily_client.search(query, search_depth="advanced", max_results=5, include_raw_content=True)
