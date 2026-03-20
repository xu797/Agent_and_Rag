#文本嵌入模型
from langchain_community.embeddings import DashScopeEmbeddings

embeddings = DashScopeEmbeddings(model="text-embedding-v1")

print(embeddings.embed_query("hello world")) #单次转换

print(embeddings.embed_documents(["hello world", "hi", "hello langchain"]))#批量转换

