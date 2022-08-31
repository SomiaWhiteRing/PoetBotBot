from selenium.webdriver.chrome.service import Service
from apscheduler.schedulers.blocking import BlockingScheduler

from func.postWeibo import Weibo
from func.getCookie import Cookie
from func.getPoem import getPoem

def post_poem():
    # 存储名称
    name = ''
    # 获取poem
    poem = getPoem().do()
    print(poem)
    # 获取service
    path = r'driver/chromedriver.exe'  # 指定驱动存放目录
    ser = Service(path)
    # 获取cookies
    try:
        cookies = Cookie().read_cookies()
    except:
        Cookie().get_cookies(ser)
        sched.shutdown()
    # 验证cookies是否有效
    if Cookie().check_cookies(name):
        # 发送微博
        Weibo().run(ser, poem, cookies)
    else:
        sched.shutdown()

    
# 测试调用一次

post_poem()
    
# 选择BlockingScheduler调度器
sched = BlockingScheduler(timezone='Asia/Shanghai')

# post_poem 每小时的第0分钟执行一次
sched.add_job(post_poem, 'cron', hour='*', minute='0')

# 启动定时任务
sched.start()
