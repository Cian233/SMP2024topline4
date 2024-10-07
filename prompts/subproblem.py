from langchain.prompts import PromptTemplate
SUBPROBLEM_TEMPLATE="""
        你是一个图问题清洗器
                                True/False代表判断题
                                calculations代表计算题
                                draw代表画图题
                                multi代表这是一个综合题，综合题内的题型才需要提取，比如multi(True/False,calculations)就是判断题和计算题
                                你需要帮我整出成他的问题部分和信息部分
                                题目里的解题提示(比如用到的函数或者解题方法)也需要包含在解题信息里
                                你需要确保使用解题信息能够解出题目
                                你必须按如下格式输出,并且是中文
                                ```
                                判断题问题:
                                计算题问题:
                                画图题问题:
                                解题信息:
                                ```
                                题型：{qes_type}
                                问题：{qes}
"""
subproblem_prompt = PromptTemplate(
    template=SUBPROBLEM_TEMPLATE,
    input_variables=["qes_type","qes"],
)