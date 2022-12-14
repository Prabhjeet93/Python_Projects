from time import sleep
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import csv

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r'./tools/chromedriver', options=options)

driver.maximize_window()
print("Navigating to the page")

driver.get("url")
driver.implicitly_wait(20)

with open('data1.csv','w', newline='') as f:
    wr=csv.writer(f)
    #wr.writerow(["URLs"])

with open('data1.csv', 'r') as file:
    rd = csv.reader(file)
    print(type(rd))
    for row in rd:
        print(row[0])
        driver.get(row[0])
        driver.implicitly_wait(20)
        print(driver.title)
        driver.implicitly_wait(20)
        print('Now clicking on the page')
        driver.implicitly_wait(10)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.implicitly_wait(20)        
file.close()
driver.quit()