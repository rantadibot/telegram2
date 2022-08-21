from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.common.by import By



def carrot2(update, context):
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(options=options)
    user_text = update.message.text
    user_text1=user_text[9:]
    browser.get(f"https://www.daangn.com/search/{user_text1}")
    elem2= browser.find_elements(By.CLASS_NAME,'flea-market-article-link')
    for row in elem2[0:10]:
        link=row.get_attribute('href')
        img=row.find_element(By.TAG_NAME,'img').get_attribute('src')
        title=row.find_element(By.CLASS_NAME,'article-title')
        region=row.find_element(By.CLASS_NAME,'article-region-name')
        price=row.find_element(By.CLASS_NAME,'article-price ')
        update.message.reply_text('제목 : '+ title.text+'\n지역 : '+region.text+'\n가격 : '+price.text)
        sleep(1)
        update.message.reply_photo(img)
        sleep(2)
        update.message.reply_text('링크 : '+link)
    browser.switch_to.default_content()
    sleep(3)
    