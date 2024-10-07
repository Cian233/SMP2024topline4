from httpx import get
import langchain
from .utils import *
from config import *

from tools.code_interpreter import code_interpreter #code_interpreter_async,
from tools.query_engine import create_query_engine

from llama_index.core.tools import FunctionTool,QueryEngineTool,ToolMetadata
from llama_index.core import Settings
Settings.llm = get_llm()
Settings.embed_model=get_embed()
code_interpreter_tool=FunctionTool.from_defaults(
    code_interpreter,
    #async_fn=code_interpreter_async,
    name='CodeInterpreter',
    description=f"""
        注意这并不是jupyter环境,你必须使用print来输出才能得到返回值，例如print(a)可以得到a变量的值

        返回的图像你无法读取可以不用管他

        A function to execute python code, and return the stdout and stderr.

        You should import any libraries that you wish to use. You have access to any libraries the user has installed.

        The code passed to this functuon is executed in isolation. It should be complete at the time it is passed to this function.

        You should interpret the output and errors returned from this function, and attempt to fix any problems.
        If you cannot fix the error, show the code to the user and ask for help

        It is not possible to return graphics or other complicated data from this function. If the user cannot see the output, save it to a file and tell the user.

        所有需要用到的数据都被储存在{BASE_PATH}/question/Final_TestSet/data文件夹下,请使用绝对路径访问
        
        """
)

doc_engine=create_query_engine()


query_engine_tool=QueryEngineTool(
    query_engine=doc_engine,
    metadata=ToolMetadata(
        name="DocEngine",
        description="提供 cdlib, graspologic, igraph, karateclub, littleballoffur, newworkx这6个包内函数或者类的使用方法。"
        "使用详细的纯文本问题作为工具的输入。例如:cdlib中NodeClustering类的conductance方法如何使用？"
        "一次最多只能同时查询1个文档"
    ),
)

def get_langchain_tools():
    tools=[code_interpreter_tool,query_engine_tool]
    langchain_tools=[t.to_langchain_tool() for t in tools]
    return langchain_tools

def get_tools():
    tools=[code_interpreter_tool,query_engine_tool]
    return tools