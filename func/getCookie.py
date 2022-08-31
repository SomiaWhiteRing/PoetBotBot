

from selenium import webdriver
import json
import requests

class Cookie():
    # 获取cookies 到本地
    def get_cookies(self, ser):
        chrome_options = webdriver.ChromeOptions()
        # 把允许提示这个弹窗关闭
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(service=ser, options=chrome_options)
        driver.get('https://weibo.com/login.php')
        input('请登录微博，登录后按回车继续')
        Cookies = driver.get_cookies() # 获取list的cookies
        jsCookies = json.dumps(Cookies) # 转换成字符串保存
        with open('data/cookies.txt', 'w') as f:
            f.write(jsCookies)
        print('cookies已写入！')
        driver.quit()
        
    # 读取本地的cookies
    def read_cookies(self):
        with open('data/cookies.txt', 'r', encoding='utf8') as f:
            Cookies = json.loads(f.read())
        cookies = []
        for cookie in Cookies:
            cookie_dict = {
                'domain': '.weibo.com',
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                'expires': '',
                'path': '/',
                'httpOnly': False,
                'HostOnly': False,
                'Secure': False
            }
            cookies.append(cookie_dict)
        return cookies

    # 检测cookies的有效性
    def check_cookies(self, name="", SendKey=None):
        # 读取本地cookies
        cookies = self.read_cookies()
        s = requests.Session()
        for cookie in cookies:
            s.cookies.set(cookie['name'], cookie['value'])
        response = s.get("https://weibo.com")
        html_t = response.text
        # 检测页面是否包含微博用户名
        if name in html_t:
            return True
        else:
            if SendKey:
                requests.post('https://sctapi.ftqq.com/' + SendKey, data={'title': '微博登录失败'})
            self.get_cookies()
            return False