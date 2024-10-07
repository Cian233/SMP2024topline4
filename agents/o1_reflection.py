from .base import *
#o1 反思 node
class O1Reflection:
    def __init__(self,model=model_o1) -> None:
        self.model=model
    def __call__(self, state:State):
        state['o1_count']+=1
        question=state['question']
        qes_type=state['question_type']
        answer=state['answer']
        code=state['code']
        prompt=o1_reflect_prompt#.format(question=question,ans=answer,code=code)
        chain = prompt | self.model
        res=chain.invoke({'question':question,'qes_type':qes_type,'ans':answer,'code':code})
        res=res.content.replace('```json','').replace('```','')
        res=json.loads(res)
        res== {
            "reason": res["reason"],
            "count": int(res["count"])  # 将字符串 "10" 转换为整数
        }
        reason=res['reason']
        count=res['count']
        state['point']=res['count']
        state['reflect_reason']=res['reason']
        if state['verbose']==True:
            print('o1reflectNode被调用:')
            print(f'resaon:{reason}')
            print(f'count:{count}')
        return res
    async def arun(self, state: State):
        state['o1_count'] += 1
        question = state['question']
        qes_type=state['question_type']
        answer = state['answer']
        code = state['code']
        prompt = o1_reflect_prompt  # 保留原始prompt

        # 构建链并异步调用模型
        chain = prompt | self.model
        res = await chain.ainvoke({'question': question,'qes_type':qes_type ,'ans': answer, 'code': code})

        # 清洗返回内容
        res = res.content.replace('```json', '').replace('```', '')
        res = json.loads(res)

        # 将结果映射到state中
        res = {
            "reason": res["reason"],
            "count": int(res["count"])  # 将字符串转换为整数
        }
        reason = res['reason']
        count = res['count']
        
        state['point'] = count
        state['reflect_reason'] = reason

        # 如果启用了verbose模式，则打印输出
        if state['verbose']:
            print('o1reflectNode被调用:')
            print(f'reason: {reason}')
            print(f'count: {count}')
        
        return res