from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.common.by import By

def get_pic(query):
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(options=options)
    url=f'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={query}'
    browser.get(url)

    sleep(2)
    get_imgs=browser.find_elements(By.CSS_SELECTOR,'div.thumb')
    imgs=[]
    for i in get_imgs[0:3]:
        img=i.find_element(By.TAG_NAME,'img')
        src=img.get_attribute('src')
        imgs.append(src)
    browser.quit()
    return imgs