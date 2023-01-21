""" this code is going to open a chrome browser and hit the urls"""


from argparse import Action
from time import sleep
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import csv
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(executable_path=r'./tools/chromedriver.exe', options=options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
print("Navigating to the page")

driver.get("url")
driver.implicitly_wait(20)
print(driver.title)
#driver.implicitly_wait(20)
sleep(10)
print('Now clicking on the page')
driver.implicitly_wait(10)

#click on question1
driver.findElement(By.XPATH("xpath")).click()



      

# closing the browser
# driver.quit()