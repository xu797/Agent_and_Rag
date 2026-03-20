# Agent_and_RAG
一、LangChain简介
为各种LLMs实现通用的接口，把LLMs相关的组件“链接”在一起。
本质上就是一个python的三方库，提供了如下六种功能的API。
1）Prompts:提示词工程 
2）Models:调用各类模型(大语言模型llms、聊天模型chat-model、文本嵌入模型)
3）History:管理会话历史记录
4）Indexes:管理和分析各类文档
5）Chains:构建功能的执行链条
6）Agent:构建智能体
pip install langchain langchain-community langchain-ollama dashscope chromadb -i https://pypi.tuna.tsinghua.edu.cn/simple

二、RAG（检索增强生成任务）
通用大模型存在的一些问题：
1）LLM的知识不是实时的，存在部分信息滞后。因为模型的训练是在某一个时间点完成的。
2）LLM的领域知识是缺乏的，大模型的知识来源于训练数据。
利用RAG技术，可以为大模型提供从特定数据源检索到的信息，以此来修正和补充生成的方案。
RAG = 检索技术 + LLM提示