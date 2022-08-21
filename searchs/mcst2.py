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
    url=f'https://www.mcst.go.kr/kor/s_about/organ/staff/staffGuide01.jsp?pMenuCD=0603050000&pCurrentPage=1&pSearchType=01&pSearchWord={query}'
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

def mcst(update:Update,context:CallbackContext):
    user_text=update.message.text
    user_text1=user_text.split(' ')[1]
    names=get_name(user_text1)
    update.message.reply_text(f'문체부에 현재 {user_text1}이 {a}명 있습니다')
    for i in range(0,a):
        update.message.reply_text(names[1]+' : '+names[5*i+6]+'\n'+names[2]+' : '+names[5*i+7]+'\n'+names[3]+' : '+names[5*i+8]+'\n'+names[4]+' : '+names[5*i+9]+'\n')
