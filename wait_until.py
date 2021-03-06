from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element_by_css_selector('button#book')

    book = WebDriverWait(browser, 16).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
    button.click()
    browser.execute_script("window.scrollBy(0, 100);")
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    field = browser.find_element_by_css_selector('input.form-control')
    field.send_keys(y)
    submit = browser.find_element_by_css_selector('button#solve')
    submit.click()
finally:
    time.sleep(4)
    browser.quit()
