from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://black-moss-0a0440e03.azurestaticapps.net/rv4.html'

try:
    # Oldal betöltése
    driver.get(URL)
    time.sleep(1)

    # Elements
    textarea = driver.find_element_by_id('cites')
    random_cities = driver.find_elements_by_xpath('//*[@id="randomCities"]/li')
    missing_city = driver.find_element_by_id('missingCity')
    check_btn = driver.find_element_by_id('submit')

    # A testarea-ban szereplo varosokat listaba gyujteni, vesszok menten elvagni,
    # random_cities lista tartalmaval osszehasonlitani

    for rc in random_cities:
        # Print if displayed
        if rc.is_displayed():
            print(rc.text)

    print(len(random_cities))
    textarea_list = list(textarea.text)
    print(len(textarea_list))

    # Idezojeleket kivenni, vesszok menten uj sort beszurni a listaba, majd kivenni a vesszoket is
    new_list = []
    for clear in textarea_list:
        # '\n'.join()
        new_char = clear.replace('"', '')
        new_list.append(new_char)

    print(new_list)
    print(len(new_list))

    # A megtalalt varos
    secret_city = ""
    missing_city.send_keys(secret_city)
    check_btn.click()

finally:
    driver.quit()
