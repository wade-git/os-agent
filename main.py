from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from windows.agent import Agent
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    llm=ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite',temperature=0.2)
    # llm=ChatGroq(model='openai/gpt-oss-120b',api_key=os.getenv("GROQ_API_KEY"),temperature=0)
    agent = Agent(llm=llm,browser='chrome',use_vision=False)
    query=input("Enter your query: ")
    agent.print_response(query)

if __name__ == "__main__":
    main()


'''
Recommended to use atleast 17b model.
'''