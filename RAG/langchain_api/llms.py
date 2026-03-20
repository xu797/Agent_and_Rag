#通过langchain调用通义千问接口
from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max")

#invoke:直接输出
# res = model.invoke("你是谁")
# print(res)

#stream:流式输出

res = model.stream("你是谁")
for r in res:
    print(r, end=" ", flush=True)
    #flash=true表示立即输出，不等待缓冲区满了才输出