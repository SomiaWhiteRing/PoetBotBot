# PoetBotBot

微博自动推送bot

用于[@诗人botbot](https://weibo.com/u/7429317732)

## 运行环境

* python3
* Chrome

## 准备工作

1. 下载运行环境Chrome对应版本的[chromedriver](https://chromedriver.chromium.org/downloads)，放置在`/driver`目录下
2. 在程序目录下执行`pip install -r requirements.txt`，安装所需的依赖。
3. （可选）在`config.yaml`中配置微博名称`"weiboName"`与[Server酱](https://sct.ftqq.com/)的SendKey`"sendKey"`，配置后会在cookie失效时自动发送通知。

## 启动

```python
python main.py
```

初次启动或cookie失效时，需要进行一次扫码登录。

推荐使用新版微博，若需使用旧版微博，请将`config.yaml`中的`"oldWeibo"`配置为`true`。

发送的内容存储在`/data/poem.txt`中，可以根据使用需求自行修改。

## 参考

[【github】SinaWeiboBot](https://github.com/chaiqingao/SinaWeiboBot)

[【github】weiboSpider](https://github.com/dataabc/weiboSpider)

[【CSDN】用 Python 自动化实战，自动登录并发送微博](https://blog.csdn.net/dQCFKyQDXYm3F8rB0/article/details/124357643)

## To-Do

* [ ] 吞吐稿件功能
