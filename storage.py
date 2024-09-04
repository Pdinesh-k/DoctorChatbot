from store_index import vector_database
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_core.tools import Tool
from langchain.agents import create_structured_chat_agent
from langchain.agents import AgentExecutor
from src.prompt import *
from langchain_groq import ChatGroq
import os

from dotenv import load_dotenv
load_dotenv()


os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
api = os.getenv("GROQ_API_KEY")
os.environ["GOOGLE_CSE_ID"] = os.getenv("GOOGLE_CSE_ID")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
api_key_langchain = os.getenv("LANGCHAIN_API_KEY")


Model = "llama-3.1-70b-versatile"
llm = ChatGroq(api_key=api,model=Model)


prompt = PromptTemplate(template = prompt_template , input_variables=["context","query"],chain_type_kwargs={"prompt":prompt_template})

qa_chain = RetrievalQA.from_chain_type(llm = llm,
            chain_type="stuff",
            retriever=vector_database,
            chain_type_kwargs={"prompt":prompt})

google_search = GoogleSearchAPIWrapper()

google_tool = Tool(
    name = "google-search",
    description = "Search for medical and health related queries only",
    func = google_search.run
)

from langchain import hub
prompt = hub.pull("hwchase17/structured-chat-agent",api_key = api_key_langchain)

agent = create_structured_chat_agent(
    llm=llm,
    tools=[google_tool],
    prompt=prompt,
)

agent_executor = AgentExecutor(agent = agent,verbose=True,tools=[google_tool],handle_parsing_errors=True,max_iterations=5)


def is_health_related(query):
    keywords = ["medicine", "health", "disease", "symptom", "treatment", "diagnosis", "doctor", "hospital", "pharmacy", "drug", "therapy", "illness", "prescription", "medical", "surgery","pain","cure"]
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in keywords)

def combined_query(user_input):
    if is_health_related(user_input):
        result = qa_chain({"query": user_input})
        final_result = result["result"]

        if not final_result or "I don't know" in final_result:
            print("Fetching additional information from Google...")
            google_result = agent_executor.invoke({"input": user_input})
            final_result += "\n\nAdditional Information from Google:\n" + google_result["output"]

        return final_result
    else:
        return "BrainWave AI only answers questions related to health and medicine. Please ask a relevant question."