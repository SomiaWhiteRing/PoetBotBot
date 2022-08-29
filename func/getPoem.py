from random import randint
class getPoem():

    def func(self):
        res = open('data/poem.txt', 'r',encoding='utf-8').readlines()
        # 从poem.txt中随机选取一行
        line = res[randint(0,len(res)-1)]
        # 把<br />替换成\n
        status = line.replace('<br />', '\n')
        # 返回给main.py
        return status

    def do(self):
        return self.func()