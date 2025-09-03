from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI
from windows.agent import Agent
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    # llm模型设置
    # llm=ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite',temperature=0.2)
    # llm=ChatGroq(model='openai/gpt-oss-120b',api_key=os.getenv("GROQ_API_KEY"),temperature=0)
    # llm=ChatOpenAI(model='gpt-4',api_key=os.getenv("OPENAI_API_KEY"),temperature=0)
    llm=ChatDeepSeek(model='deepseek-chat',api_key=os.getenv("DEEPSEEK_API_KEY"),temperature=0.3)

    # 创建Agent
    agent = Agent(llm=llm,browser='chrome',use_vision=False)

    # 创建任务
    # 如：
    # 写一段有关LLMs的英文说明，并保存到本机桌面。注意，记事本应用打开后有可能残留上一次的打开文件，需要新建一个空白文件再记录，另外，注意当前输入法是否是英文输入法。
    # 打开微信，查找和‘wpc’的聊天记录，将2025-08-01~2025-09-01之间的聊天记录导出来，注意在中文系统，微信的应用程序名称可能是Weixin或是WeChat，请注意分辨。另外，我要的是微信中的聊天记录，请注意学习一下微信的聊天记录查找等操作方法
    query=input("Enter your query: ")
    agent.print_response(query)

if __name__ == "__main__":
    main()


'''
Recommended to use atleast 17b model.
'''