#測試http://kennethhutw.github.io/demo/Selenium/Signin.html 並且點擊find_element_by_id("signin")進入登入頁面
from selenium import webdriver
path ="chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("http://kennethhutw.github.io/demo/Selenium/Signin.html")
driver.find_element_by_id("signin").click()

driver.close()
driver.quit()

