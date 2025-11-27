from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    print("Installing ChromeDriver...")
    service = Service(ChromeDriverManager().install())

    print("Launching Chrome...")
    driver = webdriver.Chrome(service=service)

    print("Opening website...")
    driver.get("https://google.com")

    print("Browser should be visible now.")
    
    time.sleep(1)
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium learning beginner level")
    time.sleep(1)
    search_box.submit()
    time.sleep(2)
    input("Press Enter to exit...")

except Exception as e:
    print("ERROR OCCURRED:")
    print(e)
