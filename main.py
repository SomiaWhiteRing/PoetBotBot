from os import access
from apscheduler.schedulers.blocking import BlockingScheduler

from func.weibo import weiboClient
from func.getPoem import getPoem

def every_day_nine():
    # 获取poem
    poem = getPoem().do()
    print(poem)
    # 获取access_token
    access_token = open('data/access_token.txt', 'r').read()
    # 发送微博
    weiboClient().post(poem, access_token)
    
# 测试调用一次

every_day_nine()
    
# 选择BlockingScheduler调度器
sched = BlockingScheduler(timezone='Asia/Shanghai')

# job_every_nine 每秒执行一次
sched.add_job(every_day_nine, 'interval', seconds=1000)

# 启动定时任务
sched.start()
