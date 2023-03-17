from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("qqq@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '111.txt')
    browser.find_element(By.ID, "file").send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
