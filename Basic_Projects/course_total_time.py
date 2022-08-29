"""
 take any course and calculate the total time taken to watch all videos by adding the timing of each video.
 We need to use
 1. selenium
 2. reg ex.

 Below code is specific to particular website.
 It will count the time of each lecture and return the total time taken in each course with course names.

"""
import re
import time

from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('./chromedriver')
driver.get('login page of the website')
print(driver.title)

# entering username and password on the Login page and logging into the website
username = 'emailid'
password = 'password'

username = driver.find_element(By.XPATH,"//input[@type='email']").send_keys(username)
pswd = driver.find_element(By.XPATH,"//input[@type='password']").send_keys(password)
login_btn = driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(5)

# method to find the time of each lecture with regex and returning sum of the each lectures time.
def findTime():
    coursename = driver.find_element(By.XPATH, "//div[@class = 'course-sidebar']/h2").text
    print("coursename:",coursename)
    lecturenames = driver.find_elements(By.XPATH, "//span[@class='lecture-name']")
    print("Total Lectures:", len(lecturenames))
    sum = 0
    for el in lecturenames:
        lecture = el.text
        # if result3:
        result = lecture.split('(')
        #result2= result[-1].split(')')
        result2 = result[-1].split(':')
            # print(result[0])
        if result2[0].isnumeric():
            sum = sum + int(result2[0])

        # print(result)
    sum = sum + len(lecturenames) / 3
    print("Total time {} minutes".format(sum))

# callling above method for each course url
list_courses = [] # list of courses's url
for course in list_courses:
    driver.get(course)
    findTime()
    time.sleep(5)

#release the browser resiurces
driver.quit()
