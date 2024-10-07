from .base import *
#代码运行 node
class CodeRunner:
    def __init__(self,model=model_4o) -> None:
        self.model=model
    def __call__(self,state) -> Any:
        code=state['code']
        code_ans=code_interpreter_tool.call(code)
        question=state['question']
        state['code_ans']=code_ans
        res=self.model.invoke(code_runner_prompt.format(code_ans=code_ans,question=question,code=code))
        # # 使用正则表达式提取 doc_keywords 的内容
        # match = re.search(r'doc_keywords:\s*\((.*?)\)', res.content, re.DOTALL)
        # print(res)
        # if match:
        #     keywords = match.group(1)
        #     state['doc_keywords']=str(keywords)   
        if 'True' in res.content:
            state['code_run_state']=True
            state['answer']=code_ans.content
        else:
            #state['doc_keywords']=res.content.replace('run_state:','').replace('False','').replace('doc_keywords:','')
            state['code_run_state']=False
        if state['verbose']==True:
            print('代码运行Node被调用:')
            print(f'代码是否运行成功:{res.content}')
            print(f'报错:{code_ans}')
        return res
    async def arun(self, state) -> Any:
        code = state['code']
        
        # 假设 code_interpreter_tool.call 也有异步版本
        code_ans = await code_interpreter_tool.acall(code)
        state['code_ans'] = code_ans
        question=state['question']
        # 异步调用模型的 invoke
        res = await self.model.ainvoke(code_runner_prompt.format(code_ans=code_ans,question=question,code=code))

        # 根据返回内容更新 state
        if 'True' in res.content:
            state['code_run_state'] = True
            state['answer'] = code_ans.content
        else:
            #state['doc_keywords'] = res.content.replace('run_state:', '').replace('False', '').replace('doc_keywords:', '')
            state['code_run_state'] = False

        # 打印输出（如果启用了 verbose）
        if state['verbose']:
            print('代码运行Node被调用:')
            print(f'代码是否运行成功: {res.content}')
            print(f'报错:{code_ans}')
        
        return res