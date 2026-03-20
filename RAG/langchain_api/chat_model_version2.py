#chat-model api 调用示例
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

model = ChatTongyi(model="qwen3-max")#qwen3-max:chat-model，qwen-max:llm

#简写
messages = [
    # SystemMessage(content="你是一个田园风光诗人。"),
    # HumanMessage(content="写一首唐诗。"),
    # AIMessage(content="锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。"),
    # HumanMessage(content="按照上一个回复的格式，再次写一首唐诗。")
    ("system", "你是一个田园风光诗人。"),
    ("human", "写一首唐诗。"),
    ("ai", "锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。"),
    ("human", "按照上一个回复的格式，再次写一首唐诗。")
]

res = model.stream(messages)
#chat-model打印的时候需要加上.content
for r in res:
    print(r.content, end=" ", flush=True)