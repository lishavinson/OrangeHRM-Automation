from selenium import webdriver

print("===================================")
print("   Welcome to OrangeHRM Automation")
print("===================================")

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")

print("OrangeHRM website opened")
print("Page Title:", driver.title)

driver.quit()