from langchain.prompts import PromptTemplate
from pydantic import BaseModel,Field
from langchain.output_parsers import PydanticOutputParser

O1_CHAT_TEMPLATE="""
        你是一个高级图论专家,精通基础图论、图统计学习和图嵌入三个方面的知识
        你现在需要使用工具帮我编写出代码,你需要优先使用文档检索到的函数,必须使用题目中提到的函数,使用文档函数时严格按照文档示例中的方法使用
        有小数的需要保留两位 
        {question}
        题型:{qes_type}
        True/False代表判断题,calculations代表计算题,draw代表画图题
        multi代表综合题,综合题括号内代表综合题拥有的题型
        例如multi(calculations, draw)代表该综合题内有计算题和画图题两个子问题
        multi(calculations, True/False)代表该综合题内有计算题和判断题两个子问题
        含有判断题的问题答案必须要包含一个True或False来判断判断题的正误
        综合题内的两种问题都需要给出答案
        最后必须给出解题代码
        所有数据文件都被放在question/Final_TestSet/data文件夹下
        注意这并不是jupyter环境,你必须使用print来输出才能得到返回值，例如print(a)可以得到a变量的值
        可能要用到的文档
        {doc}
        上一次编写的代码
        {code}
        上一次代码运行的报错
        {code_ans}
        上一次可能存在的问题
        {reason}
        你最后需要按如下格式给出答案
        ```
        "code":""(代码)
        "answer":""(代码的运行结果)
        ```
"""

o1_chat_prompt = PromptTemplate(
    template=O1_CHAT_TEMPLATE,
    input_variables=["question",'qes_type',"doc","code","code_ans",'reason'],
)

class Reflect(BaseModel):
            reason: str = Field(description="理由")
            count: str = Field(description="分数,只能为数字,不能包含其他任何文字")
reflect_output_parser = PydanticOutputParser(pydantic_object=Reflect)
# 获取输出格式指示
reflect_format_instructions = reflect_output_parser.get_format_instructions()
O1_REFLECT_PROMPT="""
        你是一个高级图论专家,精通基础图论、图统计学习和图嵌入三个方面的知识
        你需要根据问题来判断我的答案和代码是否正确,并且给出分数
        如果完全正确则为10分,完全不正确则为0分,分数只能为整数,并且你需要给出打出这个分数的理由
        问题:{question}
        题型:{qes_type}
        True/False代表判断题,calculations代表计算题,draw代表画图题
        multi代表综合题,综合题括号内代表综合题拥有的题型
        例如multi(calculations, draw)代表该综合题内有计算题和画图题两个子问题
        multi(calculations, True/False)代表该综合题内有计算题和判断题两个子问题
        综合题内的两种问题都需要给出答案
        含有判断题的问题答案必须要包含一个True或False来判断判断题的正误
        画图题不用观察图像，代码正确即可
        答案:{ans}
        代码:{code}
        你只需要返回一个json
        count的值只能为数字不能包含其他任何字符
        如下格式
        ```
        'reason':''
        'count':''
        ```
"""

o1_reflect_prompt = PromptTemplate(
    template=O1_REFLECT_PROMPT,
    input_variables=["question",'qes_type',"ans","code"],
)