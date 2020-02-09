# **pyUnit-log** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 日志处理模块集合
[![](https://img.shields.io/badge/Python-3.7-green.svg)](https://pypi.org/project/pyunit-log/)

## 安装
    pip install pyunit-log

## 亮点
    快速简单的函数日志模块，只需要在函数头上写一个装饰器即可，一行代码解决日志问题。
    @Log.log(log_file='./logs')

### 日志装饰器
```python
from pyunit_log import Log

if __name__ == '__main__':
    #config_file是日志模板地址,不写默认加载
    @Log.log(log_file='./logs',config_file=None)
    def division():
        pass
```

### 加载默认日志配置
```python
from pyunit_log import Log
import logging

if __name__ == '__main__':
    log = Log()

    log.get_log_config()  # 加载默认配置文件
    logging.info('默认加载到root下')

    info = logging.getLogger('info')
    info.info('日志文件写道info.log文件下')

    error = logging.getLogger('error')
    error.error('日志文件写道error.log文件下')
```

### 修改日志配置文件
```python
from pyunit_log import Log
import logging

if __name__ == '__main__':
    log=Log()
    # log_save_dir 修改保存日志文件夹地址
    # config_path 修改配置文件地址
    config=log.log_config(log_save_dir='/temp/logs',config_path=None) 
    log.set_log_config(config)

    info = logging.getLogger('info')
    info.info('日志文件写道info.log文件下')

    error = logging.getLogger('error')
    error.error('日志文件写道error.log文件下')
```

### [修改配置文件格式](https://docs.python.org/zh-cn/3.7/library/logging.handlers.html?highlight=timedrotatingfilehandler)
```log
[loggers]
keys = root,info,error

[handlers]
keys = console,info,error

[formatters]
keys = simpleFormatter

[formatter_simpleFormatter]
format = %(asctime)s - %(module)s - %(thread)d - %(levelname)s : %(message)s
datefmt = %Y-%m-%d %H:%M:%S

[logger_root]
level = INFO
handlers = info,console

[handler_console]
class = StreamHandler
level = INFO
formatter = simpleFormatter
args = (sys.stdout,)

[logger_info]
level = INFO
handlers = info
qualname = info
propagate = 0

[handler_info]
class = handlers.RotatingFileHandler
formatter = simpleFormatter
args = ('logs/info.log', 'a', 1048576, 30, 'UTF-8')

[logger_error]
level = ERROR
handlers = error
qualname = error
propagate = 0

[handler_error]
class = handlers.TimedRotatingFileHandler
formatter = simpleFormatter
args = ('logs/error.log', 'D', 1, 30, 'UTF-8')
```

#### 日志大小说明
    默认：info日志是1M（1048576）分割
    error日志是每天分割

***
[1]: https://blog.jtyoui.com