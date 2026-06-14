from langchain_community.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V4-Pro", task="text-generation")

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template="Answer the following question \n {question} from the following text \n {text}",
    input_variables=["question", "text"],
)

url = "https://www.myntra.com/shop/men"

loader = WebBaseLoader(url)

docs = loader.load()

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke(
    {"question": "What is the product we are asking", "text": docs[0].page_content}
)

print(result)

# print(len(docs))

# print(docs[0].page_content)
