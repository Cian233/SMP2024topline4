from .base import *
from .coderunner import CodeRunner
from .subproblem import Subproblem
from .doc_retriever import DocRetriever,DocRetrieverFirst
from .o1chat import O1Chat
from .o1_reflection import O1Reflection
class CustomAgent:
    def __init__(self,state:State):
        self.state=state
        
    def run(self):
        doc_retriever_first=DocRetrieverFirst()
        o1_chat=O1Chat()
        code_runner=CodeRunner()
        doc_retriever=DocRetriever()
        o1_reflect=O1Reflection()
        max_o1_turns=4
        doc_retriever_first(self.state)
        while self.state['o1_count']<=max_o1_turns:
            o1_chat(self.state)
            code_runner(self.state)
            if self.state['code_run_state']==False:
                doc_retriever(self.state)
            else:
                o1_reflect(self.state)
                if int(self.state['point'])>=9:
                    self.state['is_verify']=True
                    break
        return self.state
    async def arun(self):
        doc_retriever_first=DocRetrieverFirst()
        o1_chat = O1Chat()
        code_runner = CodeRunner()
        doc_retriever = DocRetriever()
        o1_reflect = O1Reflection()
        max_o1_turns = 3

        # 异步调用 Subproblem
        #await subproblem.arun(self.state)
        await doc_retriever_first.arun(self.state)
        while self.state['o1_count'] <= max_o1_turns:
            await o1_chat.arun(self.state)
            await code_runner.arun(self.state)
            if self.state['code_run_state'] == False:
                await doc_retriever.arun(self.state)
            else:
                await o1_reflect.arun(self.state)
                if int(self.state['point']) >= 9:
                    self.state['is_verify'] = True
                    break

        return self.state
