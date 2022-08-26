from datetime import datetime, timezone
import logging
import os
 
#設定 logs 目錄
dir_path = 'D:/pythonProject/itkm/logger/logs/'
#設定檔名
filename = "{:%Y-%m-%d}".format(datetime.now(timezone.utc) + '.log'
 
def create_logger():
    #log config
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # file handler
    fileHandler = logging.FileHandler(dir_path + log_folder + '/' + filename, 'a', 'utf-8')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
 
    # console handler
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)
    consoleHandler.setFormatter(formatter)
    logger.addHandler(consoleHandler)
 
    return logger

def check_or_create_folder(log_folder):
  
    # 如果目錄不存，則建新的
    if not os.path.exists(dir_path + log_folder):
        os.makedirs(dir_path + log_folder)
