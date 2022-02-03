from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

# i am  using selenium concept to display the  search results

chromedriver = webdriver.Chrome("C:\\Users\\15145\\Documents\\chromedriver_win32\\chromedriver.exe")
chromedriver.get("https://www.google.ca")

element = chromedriver.find_element_by_name("q")
element.send_keys("do epic shit")
element.submit()

results = chromedriver.find_elements_by_xpath("//div[@class='g'] //a[not(@class)]")
for result in results:
    print(result.get_attribute("href"))

    result.click()
    time.sleep(4.0)
    chromedriver.back()







