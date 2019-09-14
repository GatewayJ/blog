# coding:utf-8
# author:JiHW

import os
from logging.handlers import SMTPHandler

logfile_dir = os.path.dirname(os.path.abspath(__file__))

# 定义日志文件的路径
LOG_PATH = os.path.join(logfile_dir, 'log.log')
BOSS_LOG_PATH =os.path.join(logfile_dir, 'boss.log')
# log文件的全路径
logfile_name = 'all2.log'
logfile_path = os.path.join(logfile_dir, logfile_name)


# 定义三种日志输出格式 开始
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][%(filename)s:%(funcName)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'
# 定义日志输出格式 结束

mail_handler = SMTPHandler(
    mailhost='127.0.0.1',
    fromaddr='server-error@example.com',
    toaddrs=['admin@example.com'],
    subject='Application Error'
)

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'id_simple': {
            'format': id_simple_format
        },
    },
    'filters': {},
    'handlers': {
        'stream': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'access': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        'boss': {
                    'level': 'ERROR',
                    'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
                    'formatter': 'id_simple',
                    'filename': BOSS_LOG_PATH,  # 日志文件
                    'maxBytes': 300,
                    'backupCount': 5,
                    'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
                },
        'critical_mail': {
                    'level': 'CRITICAL',
                    'class': 'logging.handlers.SMTPHandler',  # log to mailbox
                    'mailhost': '127.0.0.1',
                    'fromaddr': 'server-error@example.com',
                    'toaddrs': ['admin@example.com'],
                    'subject': 'Application Error',
                    'credentials': ('user@qq.com','password'),
                    'formatter': 'standard',
                }
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        'root': {
            'handlers': ['stream', 'access'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}
