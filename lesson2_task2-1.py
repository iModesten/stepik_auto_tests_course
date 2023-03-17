from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value")
    x_calc = calc(x.text)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("window.scrollBy(0, 100);")
    
    browser.find_element(By.ID, "answer").send_keys(x_calc)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()
