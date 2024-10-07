from .base import *
#文档召回 node
class DocRetriever:
    def __call__(self, state):
        error_info=state['answer']
        doc=state['doc']
        res=agent.chat(f"""
            你是一个文档提查询器，精通精通基础图论、图统计学习和图嵌入三个方面的知识
            你需要根据报错{error_info}和已经有的文档{doc}来帮我寻找还需要使用到的文档，注意已经有了的就不用返回了
            重点观察文档中使用到的函数或者算法
            函数一般含有_,算法开头一般是大写
            最后你必须且只要按json格式给出答案，包含所有文档,包含所属的包,参数,返回值,示例,描述
            """)
        state['doc']+=res.response
        if state['verbose']==True:
            print('文档召回Node被调用:')
            print(f'检索到文档:{res.response}')
        return res.response
    async def arun(self, state):
        error_info=state['answer']
        doc=state['doc']
        res=await agent.achat(f"""
            你是一个文档提查询器，精通精通基础图论、图统计学习和图嵌入三个方面的知识
            你需要根据报错{error_info}和已经有的文档{doc}来帮我寻找还需要使用到的文档，注意已经有了的就不用返回了
            重点观察文档中使用到的函数或者算法
            函数一般含有_,算法开头一般是大写
            最后你必须且只要按json格式给出答案，包含所有文档,包含所属的包,参数,返回值,示例,描述
            """)
        state['doc']+=res.response

        # 如果启用了 verbose 模式，打印检索结果
        if state['verbose']:
            print('文档召回Node被调用:')
            print(f'检索到文档: {res.response}')
        
        return res.response
    
class DocRetrieverFirst:
    def __call__(self, state):
        query_str=state['question']
        res=agent.chat(f"""
            你是一个文档提查询器，精通精通基础图论、图统计学习和图嵌入三个方面的知识
            你需要根据问题{query_str}来帮我抽取出他可能需要使用到的文档
            重点观察文档中使用到的函数或者算法
            函数一般含有_,算法开头一般是大写
            最后你必须且只要按json格式给出答案，包含所有文档,包含所属的包,参数,返回值,示例,描述
            """)
        state['doc']+=res.response
        if state['verbose']==True:
            print('文档召回Node被调用:')
            print(f'检索到文档:{res.response}')
        return res.response
    async def arun(self, state):
        query_str=state['question']
        res=await agent.achat(f"""
            你是一个文档提取器，精通精通基础图论、图统计学习和图嵌入三个方面的知识
            你需要根据问题{query_str}来帮我抽取出他可能需要使用到的文档
            重点观察文档中使用到的函数或者算法
            函数一般含有_,算法开头一般是大写或者全部大写
            最后你必须且只要按json格式给出答案，包含所有文档,包含所属的包,参数,返回值,示例,描述
            """)
        state['doc']+=res.response

        # 如果启用了 verbose 模式，打印检索结果
        if state['verbose']:
            print('文档召回FirstNode被调用:')
            print(f'检索到文档: {res.response}')
        
        return res.response