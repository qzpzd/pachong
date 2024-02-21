# # -*- coding: utf-8 -*-
# import urllib
# import urllib.request
# import json
# import http.cookiejar as cookielib
# import re
# import zlib


# #获取Cookiejar对象（存在本机的cookie消息）
# cookie = cookielib.CookieJar()
# #自定义opener,并将opener跟CookieJar对象绑定
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
# #安装opener,此后调用urlopen()时都会使用安装过的opener对象
# urllib.request.install_opener(opener)


# home_url = 'http://bj.lianjia.com/'
# # auth_url = 'https://passport.lianjia.com/cas/login?service=http%3A%2F%2Fbj.lianjia.com%2F'
# auth_url = 'http://bj.lianjia.com/chengjiao/'
# chengjiao_url = 'http://bj.lianjia.com/chengjiao/'
 
 
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Encoding': 'gzip, deflate, sdch',
#     'Accept-Language': 'zh-CN,zh;q=0.8',
#     'Cache-Control': 'no-cache',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Host': 'passport.lianjia.com',
#     'Pragma': 'no-cache',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
# }

# # 获取lianjia_uuid
# req = urllib.request.Request('http://bj.lianjia.com/')
# opener.open(req)
# # 初始化表单
# req = urllib.request.Request(auth_url, headers=headers)
# result = opener.open(req)


# # 获取cookie和lt值
# pattern = re.compile(r'JSESSIONID=(.*)')
# jsessionid = pattern.findall(result.info().getheader('Set-Cookie').split(';')[0])[0]

# html_content = result.read()
# gzipped = result.info().getheader('Content-Encoding')
# if gzipped:
#     html_content = zlib.decompress(html_content, 16+zlib.MAX_WBITS)
# pattern = re.compile(r'value=\"(LT-.*)\"')
# lt = pattern.findall(html_content)[0]
# pattern = re.compile(r'name="execution" value="(.*)"')
# execution = pattern.findall(html_content)[0]
 

# # data
# data = {
#     'username': '18579725436', #替换为自己账户的用户名
#     'password': '5201314qzp', #替换为自己账户的密码
#     'execution': execution,
#     '_eventId': 'submit',
#     'lt': lt,
#     'verifyCode': '',
#     'redirect': '',
# }

# # urllib进行编码
# post_data=urllib.urlencode(data)


# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'zh-CN,zh;q=0.8',
#     'Cache-Control': 'no-cache',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Host': 'passport.lianjia.com',
#     'Origin': 'https://passport.lianjia.com',
#     'Pragma': 'no-cache',
#     'Referer': 'https://passport.lianjia.com/cas/login?service=http%3A%2F%2Fbj.lianjia.com%2F',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
#     'Upgrade-Insecure-Requests': '1',
#     'X-Requested-With': 'XMLHttpRequest',
# }
 

# req = urllib.request.Request(auth_url, post_data, headers)


# try:
#     result = opener.open(req)
# except urllib.request.HTTPError as e:
#     print (e.getcode())  
#     print (e.reason)  
#     print (e.geturl())  
#     print (e.info())
#     req = urllib.request.Request(e.geturl())
#     result = opener.open(req)
#     req = urllib.request.Request(chengjiao_url)
#     result = opener.open(req).read()
#     #print result


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# # 创建一个新的Chrome浏览器实例（需确保已安装对应驱动）
# driver = webdriver.Chrome(executable_path='path/to/chromedriver')

# # 访问链家首页并定位到登录按钮
# driver.get('http://bj.lianjia.com/')
# login_button = driver.find_element_by_css_selector("CSS_SELECTOR_FOR_LOGIN_BUTTON")
# login_button.click()

# # 等待登录窗口加载完成
# time.sleep(3)  # 使用sleep简单等待，也可以使用WebDriverWait等更精确的方法

# # 在登录窗口中填写用户名和密码
# username_input = driver.find_element_by_id("ID_OF_USERNAME_INPUT")
# password_input = driver.find_element_by_id("ID_OF_PASSWORD_INPUT")

# username_input.send_keys("18579725436")
# password_input.send_keys("5201314qzp")

# # 提交表单或点击登录按钮
# submit_button = driver.find_element_by_css_selector("CSS_SELECTOR_FOR_SUBMIT_BUTTON")
# submit_button.click()

# # 等待登录成功，然后访问成交房源页面
# time.sleep(3)  # 同样，可以使用更精准的等待方法
# driver.get('http://bj.lianjia.com/chengjiao/')

# # 这时你可以对页面进行进一步操作或抓取数据...

# # 最后记得关闭浏览器
# driver.quit()

import requests
from bs4 import BeautifulSoup

# 登录URL
login_url = 'https://clogin.lianjia.com/login?service=https%3A%2F%2Fwww.lianjia.com%2Fuser%2Fchecklogin%3Fredirect%3Dhttps%253A%252F%252Fbj.lianjia.com%252Fchengjiao%252F'  # 替换成实际登录接口地址

# 请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
}

# 获取登录页面内容以获取可能存在的动态参数（如XSRF token）
response = requests.get(login_url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 提取表单字段值（手机号和密码）
username_input = soup.find('input', {'id': 'username'})
password_input = soup.find('input', {'id': 'password'})

username = '18579725436'
password = '5201314qzp'

# 构造登录数据
login_data = {
    'username': username,
    '_xsrf': '',  # 如果存在XSRF token，则在这里添加从页面中提取的内容
    'password': password,
    # 其他可能需要的隐藏字段，根据实际页面分析确定
}

# 发送POST请求进行登录
response_post = requests.post(login_url, headers=headers, data=login_data)

if response_post.status_code == 200:
    print("登录请求发送成功，但是否登录成功需进一步分析响应内容")
else:
    print(f"登录失败，HTTP状态码：{response_post.status_code}")