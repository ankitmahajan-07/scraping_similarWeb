from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
import json
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
dataList=[]
options = Options()
ua = UserAgent()
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
print(userAgent)
options.add_argument('user-agent='+userAgent)
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


driver = webdriver.Chrome(r'C:\\Users\\acer\\Downloads\\chromedriver_win32\\chromedriver.exe',chrome_options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",{
    "source":'''
    Object.defineProperty(navigator, 'webdriver', {
      get: () => false,
    });
    '''})

def checkTitle(driver):
    if driver.title != 'Pardon Our Interruption':
        time.sleep(10)
        div = driver.find_element_by_id('js-headerMenu')
        ul = div.find_element_by_class_name('headerNav')
        btn = ul.find_element_by_class_name('headerNav-item--login')
        print(btn.text)
        my_btn = btn
        return my_btn
    else:
        time.sleep(30)
        checkTitle(driver)

def checkTitleAgain(driver):
    if driver.title != 'Pardon Our Interruption':
        time.sleep(7)
        my_div = driver.find_element_by_class_name('wwo-web-ranks')
        return my_div
    else:
        time.sleep(30)
        checkTitle(driver)

driver.get('https://similarweb.com')
time.sleep(3)
if driver.title != 'Pardon Our Interruption':
    time.sleep(7)
    div = driver.find_element_by_id('js-headerMenu')
    ul = div.find_element_by_class_name('headerNav')
    btn = ul.find_element_by_class_name('headerNav-item--login')
    print(btn.text)
    my_btn = btn
else:
    my_btn = checkTitle(driver)

my_btn.click()
driver.implicitly_wait(10)
div = driver.find_element_by_class_name('login__social')
div.find_element_by_class_name('social-form__social-button--google').click()
time.sleep(4)
driver.find_element_by_id('identifierId').send_keys('an')
time.sleep(.2)
driver.find_element_by_id('identifierId').send_keys('ki')
time.sleep(.2)
driver.find_element_by_id('identifierId').send_keys('tm')
time.sleep(.2)
driver.find_element_by_id('identifierId').send_keys('ah')
time.sleep(.2)
driver.find_element_by_id('identifierId').send_keys('aj')
time.sleep(.2)
driver.find_element_by_id('identifierId').send_keys('an')
time.sleep(.2)
driver.find_element_by_id('identifierId').send_keys('47')
time.sleep(.2)
driver.find_element_by_id('identifierId').send_keys('8@')
time.sleep(.2)
driver.find_element_by_id('identifierId').send_keys('gm')
time.sleep(.2)
driver.find_element_by_id('identifierId').send_keys('ai')
time.sleep(.2)
driver.find_element_by_id('identifierId').send_keys('l.')
time.sleep(.2)
driver.find_element_by_id('identifierId').send_keys('com')
driver.find_element_by_id('identifierId').send_keys(Keys.RETURN)
time.sleep(5)
driver.find_element_by_name('password').send_keys('an')
time.sleep(.2)
driver.find_element_by_name('password').send_keys('ki')
time.sleep(.2)
driver.find_element_by_name('password').send_keys('t4')
time.sleep(.2)
driver.find_element_by_name('password').send_keys('78')
time.sleep(.2)
driver.find_element_by_name('password').send_keys('@g')
time.sleep(.2)
driver.find_element_by_name('password').send_keys('ma')
time.sleep(.2)
driver.find_element_by_name('password').send_keys('il')
time.sleep(.2)
driver.find_element_by_name('password').send_keys('.c')
time.sleep(.2)
driver.find_element_by_name('password').send_keys('om')
driver.find_element_by_name('password').send_keys(Keys.RETURN)
time.sleep(60)
abc = pd.read_excel('C:\\Users\\acer\\Downloads\\cds\\mat.xls', header=None, index_col=False)
f = open('data.csv', 'a')
var=0
continueCheck = False
for item in abc.index:
    print(abc[0][item])
    website = str(abc[0][item])
    if website == '6annonce.com':
        continueCheck = True
        continue

    if continueCheck:
        driver.get('https://pro.similarweb.com/#/website/worldwide-overview/'+website+'/*/999/3m?webSource=Total')
        # try:
        if driver.title != 'Pardon Our Interruption':
            wait = WebDriverWait(driver, 40)
            my_div = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "wwo-web-ranks")))
        else:
            my_div = checkTitleAgain(driver)
        # except:
        #     my_div = ''

        try:
            divs = my_div.find_elements_by_class_name('ranks-row')
            category = divs[2].text
            category = category.split('\n')
            cat_name = category[1]
            print(cat_name)
            f.write(website + '--->>>' + cat_name)
            f.write('\n')
        except:
            print('not done')
            category = ''
            txtfile = open('notDone.txt', 'a')
            txtfile.write(website)
            txtfile.write('\n')
            txtfile.close()
        var += 1
        time.sleep(12)


