import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:/Users/Q1/Desktop/Derss8/chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get("https://userinyerface.com/game.html")

wait = WebDriverWait(driver, 10)
eleCookiesDiv = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.cookies')))


background_color = eleCookiesDiv.value_of_css_property("background-color")
height = float(eleCookiesDiv.size['height'])
print(background_color == "rgba(255, 0, 0, 1)")
print(height == 155.2)

width = eleCookiesDiv.value_of_css_property("width")
height = float(eleCookiesDiv.size['height'])  
print(width == '300px')
print(height == 175)