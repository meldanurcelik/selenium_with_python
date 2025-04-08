from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("./chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()


def login(username, password):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()
    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text
    return message


message = login("tom", "SuperSecretPassword!")
assert "Your username is invalid!" in message
message = login("tomsmith", "SuperSecretPassword")
assert "Your password is invalid!" in message
message = login("tomsmith", "SuperSecretPassword!")
assert "You logged into a secure area!" in message
link = driver.current_url
assert "secure" in link

driver.quit()
