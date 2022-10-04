import pandas as pd
import csv
from time import sleep
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException




# # writing the csv file line by line
# with open('data1.csv','w', newline='') as f:
#     wr=csv.writer(f)
#     #wr.writerow(["URLs"])
#     wr.writerow(["https://prabhjeetlearning.medium.com/linux-commands1-51b225d80364"])
#     wr.writerow(["https://prabhjeetlearning.medium.com/linux-commands1-51b225d80364"])
#     wr.writerow(["https://prabhjeetlearning.medium.com/linux-commands1-51b225d80364"])

# f.close()

# with open('data1.csv', 'r') as file:
#     rd = csv.reader(file)
#     print(type(rd))
#     for row in rd:
#         print(row)
# file.close()
def writeTocsv(URLs):
    with open('data1.csv','w', newline='') as f:
        wr=csv.writer(f)
        wr.writerow([URLs])

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r'./tools/chromedriver', options=options)

driver.maximize_window()
print("Navigating to the page")

driver.get("https://prabhjeetlearning.medium.com/")
driver.implicitly_wait(20)

elems = driver.find_elements(By.XPATH,"//a[@href]")

for elem in elems:
    url = elem.get_attribute("href")
    writeTocsv(url)