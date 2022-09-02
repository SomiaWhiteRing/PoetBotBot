import time
from selenium import webdriver
 

class Weibo():
    # 初始化浏览器 登录微博
    def init_browser(self, ser):
        chrome_options = webdriver.ChromeOptions()
        # 把允许提示这个弹窗关闭
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(service=ser, options=chrome_options)
        driver.get('https://weibo.com/login.php')
        input('请登录微博，登录后按回车继续')
        driver.minimize_window()
        return driver

    # 发布微博
    def post_weibo(self, driver, content, oldWeibo, tryNum = 5):
        driver.maximize_window()
        attempts = 0
        success = False
        driver.refresh()
        while attempts < tryNum and not success:
            try:
                time.sleep(10)
                if oldWeibo:
                    weibo_content = driver.find_element("xpath", '//*[@id="v6_pl_content_publishertop"]/div/div[2]/textarea')
                else:
                    weibo_content = driver.find_element("xpath", '//*[@id="homeWrap"]/div[1]/div/div[1]/div/textarea')
                weibo_content.send_keys(content)
                success = True
            except:
                driver.refresh()
                attempts += 1
                if attempts == tryNum:
                    raise Exception
        time.sleep(5)
        if oldWeibo:
            bt_push = driver.find_element("xpath", '//*[@id="v6_pl_content_publishertop"]/div/div[3]/div[1]/a')
        else:
            bt_push = driver.find_element("xpath", '//*[@id="homeWrap"]/div[1]/div/div[4]/div/div[5]/button')
        bt_push.click()  # 点击发布
        time.sleep(5)
        driver.minimize_window()
