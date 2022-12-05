import pandas as pd
import csv
from time import sleep
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException




# writing the csv file line by line
with open('data1.csv','w', newline='') as f:
    wr=csv.writer(f)
    #wr.writerow(["URLs"])
    wr.writerow(["url1"])
    wr.writerow(["url2"])
    wr.writerow(["url3"])

f.close()

with open('data1.csv', 'r') as file:
    rd = csv.reader(file)
    print(type(rd))
    for row in rd:
        print(row)
file.close()
def writeTocsv(URLs):
    with open('./Basic_Projects/automation/data1.csv','a', newline='') as f:
        wr=csv.writer(f)
        wr.writerow([URLs])

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r'./Basic_Projects/tools/chromedriver.exe', options=options)

driver.maximize_window()
print("Navigating to the page")
main_url = 'url'
driver.get(main_url)
driver.implicitly_wait(20)
driver.refresh()
driver.implicitly_wait(20)
elems = driver.find_elements(By.CSS_SELECTOR,"a")
print('Total number of URLs : ',len(elems))

for elem in elems:
    url = elem.get_attribute('href')
    writeTocsv(url)

