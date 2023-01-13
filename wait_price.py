from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    button = browser.find_element(By.ID, "book")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    ap_price = WebDriverWait(browser, 15).until(
             EC.text_to_be_present_in_element((By.ID, "price"), '100') # говорим Selenium ожидать 15 сек; при появлении нужного нам текста (100) в элементе - выполняется следующая строка кода
    )
    button.click()
    browser.find_element(By.ID, "solve").click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    print(y)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(10)
    browser.quit()
    #print(browser.switch_to.alert.text) # выводит финальное сообщение с кодом из alert в командную строку

