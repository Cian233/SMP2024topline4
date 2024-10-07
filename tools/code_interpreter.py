import subprocess
import sys
import nest_asyncio

from config.env import CONDA_ENV_NAME
# 允许在已有的事件循环中再次运行事件循环
nest_asyncio.apply()

# async def code_interpreter_async(code:str):
#     # 清理代码
#     code = re.sub(r"^(\s|`)*(?i:python)?\s*", "", code)
#     code = re.sub(r"(\s|`)*$", "", code)
    
#     try:
#         # 获取当前 IPython 实例
#         ipython = get_ipython()
#         if ipython is None:
#             raise RuntimeError("No IPython instance found")
        
#         # 使用 asyncio.sleep 模拟异步处理
#         await asyncio.sleep(0)  # 在异步上下文中，这将让出控制权
        
#         # 执行代码并获取结果
#         result = ipython.run_cell(code)
#         output = result.result
        
#         if result.error_in_exec is not None:
#             return str(result.__repr__)
        
#         if result.error_before_exec is not None:
#             return str(result.__repr__)
        
#         return str(output)
#     except Exception as e:
#         return str(e)
# def code_interpreter(code:str):
#     loop = asyncio.get_event_loop()
#     return str(loop.run_until_complete(code_interpreter_async(code)))
#conda_env=CONDA_ENV_NAME
#subprocess.run(f'conda activate {conda_env}')
def code_interpreter(code):
    # 完整的命令，用于激活指定的conda环境并执行Python代码
    #full_command = f"conda activate {conda_env} && {sys.executable} -c \"{code}\""
    # full_command = f"""
    # conda activate {conda_env} && python -c \"{code}\"
    # """
    # 转义code中的双引号
    code = code.replace('"', '\\"')
    full_command = f"""{sys.executable} -c \"{code}\"
"""

    
    # 使用 subprocess.run 来同步运行子进程
    result = subprocess.run(
        full_command,
        capture_output=True,
        #text=True,
        #shell=True,
        #executable="/bin/bash",  # Linux/macOS的shell路径，Windows可能需要不同的路径
        #check=True
    )
    # 返回标准输出和标准错误
    if result.stderr.decode('utf-8')=='':
        return str(result.stdout.decode('utf-8'))
    else:
        return str(result.stderr.decode('utf-8'))

