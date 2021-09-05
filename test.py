from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

PATH = "D:\VS Code\Scraper\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://drsquatch.com/collections/bar-soaps");
# driver.get("https://techwithtim.net")
print(driver.title)
chrome_options = Options() 
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)

buyButton = False

while buyButton is False: 

    # test = driver.find_element_by_class_name('')
    # check if product is in store
    a = 1
    a1 = driver.find_element_by_class_name('qty-add-to-cart')
    print(a1)
    time.sleep(5)
    a1.click()
    time.sleep(5)
    a2 = driver.find_element_by_class_name('icon-cross')
    a2.click(); 
    time.sleep(5)