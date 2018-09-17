# tripforcrawlers
<span style="color:red;">waiting for update examples...</span>
##### 基本原理
模拟http请求，获取网页源码、json或xml，抽取、结构化数据入库。

##### 反爬虫
1、设置headers
2、获取cookies
3、设置爬取间隔
4、使用proxy代理
5、使用浏览器获取，一般用来加载ajax、或者比较难解析cookies的网页 selenium + Web browser（headless） or chromeless（node.js）  
......

##### 爬虫库
###### Python
    1、requests_html（requests的基础上，整合了bs、xpath等解析方式）  
        https://github.com/kennethreitz/requests-html
    2、scrapy（Python爬虫框架、基于异步twist框架）  
        https://github.com/scrapy/scrapy
    3、selenium （自动化测试工具，用来启动浏览器）
        https://selenium-python.readthedocs.io/api.html
###### Node.js
    1、chromeless
        https://github.com/prisma/chromeless
    2、puppeteer
        https://github.com/GoogleChrome/puppeteer
###### useful blog
    https://cuiqingcai.com/
    http://www.lining0806.com/category/spider/