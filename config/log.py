from datetime import datetime
import logging
import sys
import os
# 指定日志文件夹
log_directory = 'log'

# 创建日志文件夹（如果不存在）
os.makedirs(log_directory, exist_ok=True)

# 生成日志文件名，包含时间戳
log_file_name = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
log_file_path = os.path.join(log_directory, log_file_name)
# 配置日志
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # 设置日志级别

# 移除默认的StreamHandler
for handler in logger.handlers[:]:
    if isinstance(handler, logging.StreamHandler):
        logger.removeHandler(handler)
# 创建一个文件处理器，将日志写入指定的文件
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.DEBUG)  # 设置日志级别
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# 获取根日志记录器并添加文件处理器
logger = logging.getLogger()
logger.addHandler(file_handler)