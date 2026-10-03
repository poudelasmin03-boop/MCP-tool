import os
import asyncio


from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()

tavily_key = os.getenv("TAVILY_API_KEY")


client = MultiServerMCPClient(
  {
    "tavily":{
      "transport":"streamable_http",
      "url":f"https://mcp.tavily.com/mcp/?tavilyApiKey={tavily_key}",
    }
  }

)


##tool discovery
async def main():
  tools =  await client.get_tools()
  # getting first elem from list
  search_tool = tools[0]

  result = await search_tool.ainvoke(
    {
      "query":"Best hotel in nepal"
    }
  )
  print(result)

  # print("/n Avaible tools are: ")
  # for i in tools:
  #   print(i.name)


asyncio.run(main())

search_tool = None

async def intialize_mcp():
  global search_tool

  if search_tool is   None:
    return

  tools = await client.get_tools()

  search_tool = tools[0]

async def tavily_mcp_search(query:str)->str:
  await intialize_mcp()
  result = await search_tool.ainvoke(
    {
      "query":query
    }
  )
  return result



if __name__ == "__main__":
  asyncio.run(main())