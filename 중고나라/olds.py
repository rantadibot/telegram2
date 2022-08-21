from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=options)

browser.get("https://cafe.naver.com/joonggonara.cafe")
def olds(update, context):
    user_text = update.message.text
    user_text1=user_text[5:]
    elem1 =browser.find_element(By.ID,'topLayerQueryInput')
    elem1.send_keys(user_text1)
    elem1.send_keys(Keys.RETURN)
    browser.switch_to.frame(browser.find_element(By.ID,'cafe_main'))
    elem2= browser.find_elements(By.CLASS_NAME,'article-board')[1]
    rows=elem2.find_elements(By.XPATH,'./table/tbody/tr')
    for row in rows[0:5]:
        elem3=row.find_element(By.CLASS_NAME,'article')
        elem4=row.find_element(By.CLASS_NAME,'td_date')
        update.message.reply_text('제목 : '+ elem3.text+'\n작성일 : '+elem4.text)
        sleep(0.5)
        update.message.reply_text('링크 : '+elem3.get_attribute('href'))
    browser.switch_to.default_content()
    sleep(3)
