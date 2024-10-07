from typing import Annotated, TypedDict,Any
import operator
from pydantic import BaseModel,Field
import json

#from langchain_core.pydantic_v1 import BaseModel as langchainBaseModel

from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode

from llama_index.core.schema import TextNode
from llama_index.core import VectorStoreIndex

import re

from tools import *
from prompts import *
from config import *
tools=get_langchain_tools()
tool_node = ToolNode(tools)

model = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
    #model='gpt-4o-2024-08-06'
    model='gpt-4o-mini'
)

model_4o = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
    #model='gpt-4o-2024-08-06'
    model='gpt-4o-2024-08-06'
)

model_o1 = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
    temperature=1,
    model='o1-mini'
)

from llama_index.core.agent import ReActAgentWorker
llm=get_llm(model='gpt-4o-mini')
query_tools=[query_engine_tool]
react_worker = ReActAgentWorker.from_tools(
    query_tools,
    llm=llm,
    verbose=False,
)
agent=react_worker.as_agent()

class State(TypedDict):
    #历史消息
    message: Annotated[list, operator.add] = []
    #问题
    question:str 
    #问题类型
    question_type:str
    #提炼过后的子问题
    subproblem:str
    #临时消息
    tmp_message:str
    #代码
    code:str
    #代码运行结果
    code_ans:str
    #代码运行是否成功
    code_run_state:bool
    #答案
    answer:str
    #调用o1的次数
    o1_count:int
    #文档查询关键字
    doc_keywords:str
    #文档
    doc:str
    #答案是否被验证
    is_verify:bool
    #是否显示中间过程
    verbose:str
    #反思
    reflect_reason:str
    #反思分数
    point:int
    #下一个步骤
    next:str

# 定义您所需的数据结构。
class Answers(BaseModel):
    code: str
    answer: str

llm_4o_mini=get_llm(model_name='gpt-4o-mini')
node1 = TextNode(text="<text_chunk>", id_="<node_id>")
nodes=[node1]
query_index=VectorStoreIndex(nodes)
query_engine = query_index.as_query_engine(llm=llm_4o_mini)
query_engine_struct = query_index.as_query_engine(llm=llm_4o_mini,output_cls=Answers)