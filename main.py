from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("./chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://useinsider.com/")
driver.maximize_window()
link = driver.current_url
baslik = driver.title
print('sayfa başlığı : ' + baslik)
driver.save_screenshot("./Screenshots/hata.png")
if "useinsider.com" in link:
    print('doğru sayfadayız : ' + link)

# şuanki pencereyi kapatır
driver.close()

# driver.quit() seleniumun kullandığı tüm pencereleri kapatır
