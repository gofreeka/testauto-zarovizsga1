from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://black-moss-0a0440e03.azurestaticapps.net/x234.html'

try:
    # Oldal betöltése
    driver.get(URL)
    time.sleep(3)

    # Elements
    input_a = driver.find_element_by_id('a')
    input_b = driver.find_element_by_id('b')
    calc_button = driver.find_element_by_id('submit')
    result = driver.find_element_by_id("result")

    # Clear elements
    def clear_elements():
        input_a.clear()
        input_b.clear()

    # Test data
    tc001_test_data = [99, 12, 222]
    tc002_test_data = ['kiskutya', 12, 'NaN']
    tc003_test_data = ['', '', 'NaN']

    # TC001 - helyes kitoltes
    input_a.send_keys(tc001_test_data[0])
    input_b.send_keys(tc001_test_data[1])
    calc_button.click()
    time.sleep(1)

    # Az eredmeny ellenorzese
    assert result.text == str(tc001_test_data[2])
    time.sleep(1)
    clear_elements()

    # TC002 - Nem szamokkal valo kitoltes
    input_a.send_keys(tc002_test_data[0])
    input_b.send_keys(tc002_test_data[1])
    calc_button.click()
    time.sleep(1)

    # Az eredmeny ellenorzese
    assert result.text == str(tc002_test_data[2])
    time.sleep(1)
    clear_elements()

    # TC003 - Ures kitoltes
    input_a.send_keys(tc003_test_data[0])
    input_b.send_keys(tc003_test_data[1])
    calc_button.click()
    time.sleep(1)

    # Az eredmeny ellenorzese
    assert result.text == str(tc003_test_data[2])
    time.sleep(1)
    clear_elements()

finally:
    driver.quit()
