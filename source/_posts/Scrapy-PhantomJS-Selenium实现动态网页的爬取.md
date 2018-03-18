---
title: Scrapy+PhantomJS+Selenium实现动态网页的爬取
date: 2018-02-08 21:01:53
tags:
- 爬虫
- Python
- Web
- javascript
categories:
- 爬虫
copyright: true
---
-----------------------
{% note info %}
网络爬虫是数据挖掘的重要前提，通过网络爬虫可以自动化批量获取互联网上你需要的有用信息。爬虫于静态页面的爬取十分简单，但Ajax的出现实现了网页的局部动态加载，网页不需每次返回重复Html而只要局部刷新，简单的静态页面爬虫只能解析单一url而对它就无能为力了。PhantomJS+Selenium，再加上Scrapy爬虫框架，就可以实现动态爬虫。
{% endnote %}
<!--more-->

## PhantomJS
### PhantomJS是什么？
- [PhantomJS](http://blog.csdn.net/libsyc/article/details/78199850)是一个基于webkit的JavaScript API。它使用QtWebKit作为它核心浏览器的功能，使用webkit来编译解释执行JavaScript代码。任何你可以在基于webkit浏览器做的事情，它都能做到。它不仅是个隐形的浏览器，提供了诸如CSS选择器、支持Web标准、DOM操作、JSON、HTML5、Canvas、SVG等，同时也提供了处理文件I/O的操作，从而使你可以向操作系统读写文件等。PhantomJS的用处可谓非常广泛，诸如网络监测、网页截屏、无需浏览器的 Web 测试、页面访问自动化等。
- [PhantomJS官方地址](http://phantomjs.org/)
- [PhantomJS官方API](http://phantomjs.org/api/)
- [PhantomJS官方示例](http://phantomjs.org/examples/。)
- [PhantomJS GitHub](https://github.com/ariya/phantomjs/。)

### PhantomJS的使用
PhantomJS的安装不再赘述，在windows平台下安装好的phantomjs.exe即可可通过JS与webkit内核交互。
```js
// GetHtml.js
var page = require('webpage').create(), //获取操作dom或web网页的对象
    system = require('system'),         //获取操作系统对象
    address;
if (system.args.length === 1) {
    phantom.exit(1);
} else {
    address = system.args[1];
    page.open(address, function (status) {   //访问url
        console.log(page.content);
        phantom.exit();
    });
}
```
控制台输入
```
phantomjs ./test.js http://baidu.com
```
即打印输出百度的html页面
### PhantomJS参考链接
- [ PhantomJS快速入门](http://blog.csdn.net/libsyc/article/details/78199850)
- [phantomjs2.1 初体验](https://www.jianshu.com/p/9efe08a8e99e)

## Selenium
### 什么是Selenium？
- selenium 是一套完整的web应用程序测试系统，包含了测试的录制（selenium IDE）,编写及运行（Selenium Remote Control）和测试的并行处理（Selenium Grid）。Selenium的核心Selenium Core基于JsUnit，完全由JavaScript编写，因此可以用于任何支持JavaScript的浏览器上。selenium可以模拟真实浏览器，自动化测试工具，支持多种浏览器，爬虫中主要用来解决JavaScript渲染问题。

### Selenium的使用
安装直接使用pip安装，详细使用详解参见参考链接，以下为简单使用介绍，即完全加载一个url（未考虑人工加载）
```py
// test.py
from selenium import webdriver
 
driver = webdriver.PhantomJS(/path/to/PhantomJS.excuatable)    # 获取浏览器对象
driver.get('http://www.baidu.com/')
print (driver.page_source)
```
### 参考链接
- [selenium用法详解](https://www.cnblogs.com/themost/p/6900852.html)

## Scrapy
不再赘述，直接丢出[文档](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)
![](http://wx1.sinaimg.cn/large/005B4KCngy1fo9ecirwzcj30jg0dqgnu.jpg)
## PhantomJS+Selenium+Scrapy
### 在`爬虫.py`中的request加入meta
    ```
    request.meta['PhantomJS'] = True
    ```
### 定义中间件
```py
//JSMiddleware.py
from selenium import webdriver
from scrapy.http import HtmlResponse

class PhantomJSMiddleware(object):
    @classmethod
    def process_request(cls, request, spider):

        if request.meta.has_key('PhantomJS'):
            driver = webdriver.PhantomJS(executable_path='/path/to/phantomjs') 
            driver.get(request.url)
            content = driver.page_source.encode('utf-8')
            driver.quit()  
            return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
```
### settings中开启中间件
```
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    '[爬虫名字].middlewares.PhantomJSMiddleware': 500,
}
```
### 改进-实现滚动刷新
- js代码如下
```js
// scrollToBottom.js
function scrollToBottom() {

    var Height = document.body.clientHeight,  //文本高度
        screenHeight = window.innerHeight,  //屏幕高度
        INTERVAL = 100,  // 滚动动作之间的间隔时间
        delta = 500,  //每次滚动距离
        curScrollTop = 0;    //当前window.scrollTop 值

    var scroll = function () {
        curScrollTop = document.body.scrollTop;
        window.scrollTo(0,curScrollTop + delta);
    };

    var timer = setInterval(function () {
        var curHeight = curScrollTop + screenHeight;
        if (curHeight >= Height){   //滚动到页面底部时，结束滚动
            clearInterval(timer);
        }
        scroll();
    }, INTERVAL)
}

```
- 重新定义中间件
```py
js = """
// scrollToBottom.js
function scrollToBottom() {
    ....
}
scrollToBottom()
"""

class PhantomJSMiddleware(object):
    @classmethod
    def process_request(cls, request, spider):

        if request.meta.has_key('PhantomJS'):
            driver = webdriver.PhantomJS() 
            driver.get(request.url)

            driver.execute_script(js)   
            time.sleep(1)  # 等待JS执行

            content = driver.page_source.encode('utf-8')
            driver.quit()  
            return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
```
`time.sleep(<wait_time>)`
为了解决等待JS执行的时间过短会导致爬取的页面靠近底部的图片没能加载，因为滚动函数还未执行到此处。所以需要预留一个稍微长一点的等待时间。
## 实战参考链接
- [在Scrapy框架下使用Selenium+PhantomJS](https://zhuanlan.zhihu.com/p/25511551)