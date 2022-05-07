from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary


from time import sleep



options=Options()
options.add_argument('--incognito')

url='https://www.youtube.com/'

drive=webdriver.Chrome(options=options)
drive.get(url)

sleep(10)

drive.quit()