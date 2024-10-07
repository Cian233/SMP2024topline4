from .base import *
#o1 node
class O1Chat:
    def __init__(self,model=model_o1) -> None:
        self.model=model
        
    
    def __call__(self,state:State):
        state['o1_count']+=1
        #subproblem=state['subproblem']
        question=state['question']
        qes_type=state['question_type']
        doc=state['doc']
        code_ans=state['code_ans']
        code=state['code']
        reason=state['reflect_reason']
        res=self.model.invoke(o1_chat_prompt.format(question=question,qes_type=qes_type,doc=doc,code_ans=code_ans,code=code,reason=reason))
        res=query_engine_struct.query(f"{res.content},answer要保留完整,你需要确保清洗出来的code可以运行")
        state['code']=res.code
        state['answer']=res.answer
        if state['verbose']==True:
            print('o1chatNode被调用:')
            print(f'code:{res.code}')
            print(f'answer:{res.answer}')
        return res
    async def arun(self, state: State):
        state['o1_count'] += 1
        #subproblem = state['subproblem']
        question=state['question']
        qes_type=state['question_type']
        doc = state['doc']
        code_ans = state['code_ans']
        code = state['code']
        reason = state['reflect_reason']

        # 异步调用model的ainvoke方法
        res = await self.model.ainvoke(o1_chat_prompt.format(question=question,qes_type=qes_type ,doc=doc, code_ans=code_ans, code=code, reason=reason))

        # 异步调用query方法
        res = await query_engine_struct.aquery(f"{res.content},answer要保留完整,你需要确保清洗出来的code可以运行")

        state['code'] = res.code
        state['answer'] = res.answer

        if state['verbose']:
            print('o1chatNode被调用:')
            print(f'code: {res.code}')
            print(f'answer: {res.answer}')
        
        return res