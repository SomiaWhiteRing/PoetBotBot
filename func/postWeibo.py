import time
from selenium import webdriver
 

class Weibo():
    # 初始化浏览器 打开微博登录页面
    def init_browser(self, ser):
        chrome_options = webdriver.ChromeOptions()
        # 把允许提示这个弹窗关闭
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(service=ser, options=chrome_options)
        driver.get('https://weibo.com/login.php')
        return driver

    # 登录微博
    def login_weibo(self, driver, cookies):
        driver.refresh()  # 刷新网页
        for cookie in cookies:
            driver.add_cookie(cookie)
        print('cookies已添加！')

    # 发布微博
    def post_weibo(self, driver, content):
        time.sleep(10)
        driver.refresh()
        time.sleep(3)
        weibo_content = driver.find_element("xpath", '//*[@id="homeWrap"]/div[1]/div/div[1]/div/textarea')
        weibo_content.send_keys(content)
        time.sleep(2)
        bt_push = driver.find_element("xpath", '//*[@id="homeWrap"]/div[1]/div/div[4]/div/div[5]/button')
        bt_push.click()  # 点击发布
        time.sleep(5)
        driver.close()  # 关闭浏览器

    # 集成操作
    def run(self, ser, content, cookies):
        driver = self.init_browser(ser)
        self.login_weibo(driver, cookies)
        self.post_weibo(driver, content)
