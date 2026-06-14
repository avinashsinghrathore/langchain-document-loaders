from langchain_community.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup

url = "https://www.myntra.com/shop/men"

loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
