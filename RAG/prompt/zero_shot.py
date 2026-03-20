from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

prompt_text = PromptTemplate.from_template(
    "我的邻居姓{lastname}，刚生了一个{gender}，帮我取一个名字，简单回答。"
)

prompt_text = prompt_text.format(lastname="张", gender="男")

model = Tongyi(model="qwen-max")

res = model.invoke(prompt_text)
print(res)
