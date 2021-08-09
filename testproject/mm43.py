from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://black-moss-0a0440e03.azurestaticapps.net/mm43.html'

try:
    # Oldal betöltése
    driver.get(URL)
    time.sleep(1)

    # Elements
    e_mail = driver.find_element_by_id('email')
    submit_button = driver.find_element_by_id('submit')
    # error_msg =
    # assert driver.find_element_by_class_name('validation-error').is_displayed()
    # Clear elements

    def clear_elements():
        e_mail.clear()

    # Test data
    tc001_test_data = ['teszt@elek.hu', '']
    tc002_test_data = ['teszt@', "Please enter a part following '@'. 'teszt@' is incomplete."]
    tc003_test_data = ['', 'Please fill out this field.']

    # TC001 - helyes kitoltes

    def tc001():
        # Beviteli mezo kitoltese tesztadattal
        e_mail.send_keys(tc001_test_data[0])
        submit_button.click()
        time.sleep(1)

        # Az eredmeny ellenorzese, osszehasonlitasa tesztadattal
        assert not driver.find_element_by_xpath("//div[@class='validation-error']").is_displayed()
        time.sleep(1)
        # Beviteli mezo tartalmanak torlese
        clear_elements()

    # TC002 - Helytelen kitoltes

    def tc002():
        # Beviteli mezo kitoltese tesztadattal
        e_mail.send_keys(tc002_test_data[0])
        submit_button.click()
        time.sleep(2)

        # Az eredmeny ellenorzese, osszehasonlitasa tesztadattal
        assert tc002_test_data[1] == driver.find_element_by_class_name('validation-error').get_attribute("value")
        time.sleep(1)
        # Beviteli mezo tartalmanak torlese
        clear_elements()

    # TC003 - Ures

    def tc003():
        # Beviteli mezo kitoltese tesztadattal
        e_mail.send_keys(tc003_test_data[0])
        submit_button.click()
        time.sleep(1)

        # Az eredmeny ellenorzese, osszehasonlitasa tesztadattal
        assert tc003_test_data[1] == driver.find_element_by_class_name('validation-error').get_attribute("value")
        time.sleep(1)
        # Beviteli mezo tartalmanak torlese
        clear_elements()

    tc001()
    tc002()
    tc003()

finally:
    driver.quit()
