from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient


load_dotenv()
tavily=TavilyClient()


@tool
def search(query: str) ->str:
    """ 
    tool that searches internet
     args:
      query: the query to search for
    Returns:
     the search result
    """
    print(f'searching for {query}')
    return tavily.search (query=query)
llm=ChatOpenAI()
tools=[search]
agent=create_react_agent(model=llm,tools=tools)

def main():
    print("Langchain")
    result=agent.invoke({"messages": HumanMessage(content="what is the weather in Pune for next 3 days")})
    #print(os.environ.get("OPEN_AI_KEY"))
    print(result)
    
    #information = """Elon Reeve Musk EE-lon; born June 28, 1971) is a businessman and entrepreneur known for his leadership of Tesla, SpaceX, X, and xAI. Musk has been the wealthiest person in the world since 2025; as of February 2026, Forbes estimates his net worth to be around US$852 billion. Born into a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he has Canadian citizenship since his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. Musk also became an American citizen in 2002.
    #In 2002, Musk founded, where he supported Donald Trump. After Trump was inaugurated as president in early 2025, Musk served as Senior Advisor to the President and as the de facto head of the Department of Government Efficiency (DOGE). After a public feud with Trump, Musk left the Trump administration and returned to managing his companies. Musk is a supporter of global far-right figures, causes, and political parties. His political activities, views, and statements have made him a polarizing figure. Musk has been criticized for COVID-19 misinformation, promoting conspiracy theories, and affirming antisemitic, racist, and transphobic comments. His acquisition of Twitter was controversial due to a subsequent increase in hate speech and the spread of misinformation on the service, following his pledge to decrease censorship. His role in the second Trump administration attracted public backlash, particularly in response to DOGE. The emails he sent to Jeffrey Epstein are included in the Epstein files, which were published between 2025–26 and became a topic of worldwide debate.
   # """
   # summary_template = """ 
   # given the details {information} of the person, i want to create
   # 1. a short summary
    #2. Two interesting facts about the person
   # """
    #summary_prompt_template = PromptTemplate (
       # input_variables={information},template=summary_template
   # )

    #llm = ChatOpenAI(temperature=0.5,model="gpt-5")
   # chain =summary_prompt_template | llm
    #response=chain.invoke (input={"information":information})
   # print (response.content)

if __name__== "__main__":
    main()