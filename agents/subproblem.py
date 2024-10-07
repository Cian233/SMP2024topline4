from .base import *

#子问题分解node
class Subproblem:
    def __init__(self,model=model_4o) -> None:
        self.model=model
    def __call__(self,state:State):
        res=self.model.invoke(subproblem_prompt.format(qes_type=state['question_type'],qes=state['question']))
        state['subproblem']=res.content
        if state['verbose']==True:
            print('子问题Node被调用:')
            print(res.content)
        return res.content
    async def arun(self, state: State):
        res = await self.model.ainvoke(subproblem_prompt.format(qes_type=state['question_type'], qes=state['question']))
        state['subproblem'] = res.content
        if state['verbose']:
            print('子问题Node被调用:')
            print(res.content)
        return res.content