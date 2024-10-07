from langchain.prompts import PromptTemplate

CODE_RUNNER_TEMPLATE="""
    请你根据代码执行器的运行结果{code_ans}
    判断代码是否运行成功
    注意只有在出现报错信息时才是运行失败
    如果没有运行成功
    你需要根据题目:{question}
    代码:{code}
    判断可能需要查询的文档
    你必须按如下格式返回
    ```
    run_state:(True/False)
    ```
"""
# """
# 你必须按如下格式返回
#     ```
#     run_state:(True/False)
#     doc_keywords:(需要查询的文档关键字)
#     ```
# """

code_runner_prompt = PromptTemplate(
    template=CODE_RUNNER_TEMPLATE,
    input_variables=["code_ans","question",'code'],
)