from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.common.by import By
from telegram import Update
from telegram.ext import CallbackContext

def get_name(query):
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(options=options)
    url=f'https://www.mois.go.kr/frt/a07/searchStaff.do?pageIndex=1&searchWrd={query}'
    browser.get(url)
    
    sleep(2)
    
    descs=browser.find_element(By.TAG_NAME,'thead')
    desc=descs.find_elements(By.TAG_NAME,'th')
    
    names=[]
    for i in desc:
        names.append(i.text)
    
    get_names=browser.find_element(By.TAG_NAME,'tbody')
    get_name=get_names.find_elements(By.TAG_NAME,'td')
    global a
    a=round(len(get_name)/5)
    for i in get_name:
        names.append(i.text)
    browser.quit()
    return names

def mois(update:Update,context:CallbackContext):
    user_text=update.message.text
    user_text1=user_text.split(' ')[1]
    names=get_name(user_text1)
    update.message.reply_text(f'행안부에 현재 {user_text1}이 {a}명 있습니다')
    for i in range(0,a):
        update.message.reply_text(names[0]+' : '+names[5*i+5]+'\n'+names[1]+' : '+names[5*i+6]+' '+names[5*i+8]+'\n'+names[2]+' : '+names[5*i+7]+'\n'+names[4]+' : '+names[5*i+9])
        