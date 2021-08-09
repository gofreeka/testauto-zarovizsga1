from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html'

try:
    # Oldal betöltése
    driver.get(URL)
    time.sleep(1)

    # Elements
    num1 = driver.find_element_by_id('num1').text
    num2 = driver.find_element_by_id('num2').text
    op = driver.find_element_by_id('op').text
    kalkulacio_button = driver.find_element_by_id('submit')
    eredmeny = driver.find_element_by_id("result").text

    # TC001
    # A kiolvasott operatot alapjan vegzi el a megfelelo muveletet a kiolvasott operandusokkal
    def mat():
        print(op)
        if op == "+":
            kalkulacio_button.click()
            # Float-ta alakitom a kiolvasott stringet es azzal vegzem el a muveletet
            var = float(num1) + float(num2)
            assert str(var) == eredmeny
        elif op == "-":
            kalkulacio_button.click()
            var = float(num1) - float(num2)
            assert str(var) == eredmeny
        elif op == "*":
            kalkulacio_button.click()
            var = float(num1) * float(num2)
            assert str(var) == eredmeny
        elif op == "/":
            kalkulacio_button.click()
            var = float(num1) / float(num2)
            assert str(var) == eredmeny

    mat()

finally:
    driver.quit()
