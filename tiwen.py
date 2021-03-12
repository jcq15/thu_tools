# -*- coding: UTF-8 -*-

from selenium import webdriver
import random
import datetime
import requests
import time
from selenium.webdriver.chrome.options import Options


def _inform(txt):
    requests.get('http://sctapi.ftqq.com/SCT9581Tvt7wb7L9ytz4yMmNmhx9RjN2.send?title=%s' % txt)


def upload(user, password):
    options = Options()
    #options.add_argument('--disable-extensions')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    #option.add_argument('--disable-dev-shm-usage')
    #option.add_argument('blink-settings=imagesEnabled=false')
    ua = 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    #ua = 'Mozilla/5.0 (Linux; Android 10; HMA-AL00 Build/HUAWEIHMA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/200901 Mobile Safari/537.36 MMWEBID/2435 MicroMessenger/7.0.19.1760(0x27001353) Process/appbrand1 WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64'
    options.add_argument('user-agent=%s' % ua)

    try:

        driver = webdriver.Chrome(options=options)
        #driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        
        print('启动！')
        driver.get("https://zijing.tsinghua.edu.cn")

        driver.find_element_by_id("i_user").send_keys(user)
        driver.find_element_by_id("i_pass").send_keys(password)
        driver.find_element_by_class_name("btn").click()

        print('下面上报')
        
        # 开始上报
        driver.find_element_by_id("temp_report").click()

        t = random.randint(1, 9)
        driver.find_element_by_id("TWI").send_keys('36.%d' % t)
        driver.find_element_by_id("submit_btn").click()

        print('报完了')
        
    except Exception as e:
        _inform('完犊子，上报体温失败了，快去看看咋回事吧！')
    else:
        _inform('恭喜！上报体温大成功！')
        
        '''
        # 上报完成，下面检查
        driver.find_element_by_id("temp_report")          # 找这个元素，为了让他等待加载完成
        driver.get("https://zijing.tsinghua.edu.cn/tp_jp/h6?m=jp#act=jp/record")
        txt = driver.find_elements_by_class_name('place-block-item')[0].find_element_by_class_name('tit-box').get_attribute('textContent')
        txt = txt.split('\n')[0]
        last_time = datetime.datetime.strptime(txt, '%Y-%m-%d %H:%M:%S')
        cur = datetime.datetime.now()
        if cur - last_time < datetime.timedelta(minutes=5):        # 最近一次提交在5分钟内
            requests.get('https://sc.ftqq.com/SCU105083Ta4a614d21a112a95d1af9bb9bc8163035f07d9376dc7c.send?text=Success-%s' % user)
        else:
            requests.get('https://sc.ftqq.com/SCU105083Ta4a614d21a112a95d1af9bb9bc8163035f07d9376dc7c.send?text=Fail!')
        '''
    finally:
        driver.quit()
