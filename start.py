from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/login")

username_textfield = driver.find_element(By.ID, "userName")
username_textfield.send_keys("Ingrid")
password_textfield = driver.find_element(By.ID, "password")
password_textfield.send_keys("P@ssw0rd")

login_button = driver.find_element(By.ID, "login")
login_button.click()
time.sleep(300)
#search_button.click()
#time.sleep(100)

print("H")
