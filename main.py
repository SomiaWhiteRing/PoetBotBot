from selenium.webdriver.chrome.service import Service
from apscheduler.schedulers.blocking import BlockingScheduler
import yaml
import requests

from func.postWeibo import Weibo
from func.getPoem import getPoem

def post_poem():
    # 获取配置
    config = yaml.load(open('config.yaml', 'r', encoding='utf-8').read(),Loader=yaml.FullLoader)
    try:
        # 获取poem
        poem = getPoem().do()
        print(poem)
        # 发送微博
        Weibo().post_weibo(driver, poem, config['oldWeibo'])
    except Exception as e:
        print(e)
        if config['sendKey']:
            requests.post('https://sctapi.ftqq.com/' + config['sendKey'], data={'title': e})

def login():
    # 获取service
    path = r'driver/chromedriver.exe'  # 指定驱动存放目录
    ser = Service(path)
    # 登录
    return Weibo().init_browser(ser)
    
# 登录微博

driver = login()
    
# 选择BlockingScheduler调度器
sched = BlockingScheduler(timezone='Asia/Shanghai')

# post_poem 每小时的第0分钟执行一次
sched.add_job(post_poem, 'cron', hour='*', minute='0')

# 启动定时任务
sched.start()
