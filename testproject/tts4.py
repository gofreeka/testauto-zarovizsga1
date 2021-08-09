from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://black-moss-0a0440e03.azurestaticapps.net/tts4.html'

try:
    # Oldal betöltése
    driver.get(URL)
    time.sleep(3)

    # Elements
    penzfeldobas_button = driver.find_element_by_id('submit')
    last_result = driver.find_element_by_id("lastResult")
    results = driver.find_elements_by_xpath('//ul[@id="results"]/li')

    # TC001
    # Gombnyomas 100x
    for i in range(100):
        penzfeldobas_button.click()
        i += 1
        for r in results:
            print(str(r))
            r += 1


finally:
    driver.quit()
