import time

from selenium import webdriver
import math


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')
    time.sleep(3)
    button = browser.find_element_by_class_name('btn.btn-primary')
    button.click()
    time.sleep(3)
    confirm = browser.switch_to_alert()
    confirm.accept()
    x = browser.find_element_by_id('input_value')
    x = x.text
    input_field = browser.find_element_by_id('answer')
    x_calc = str(math.log(abs(12 * math.sin(int(x)))))
    input_field.send_keys(x_calc)
    submit_button = browser.find_element_by_class_name('btn.btn-primary')
    submit_button.click()
    alert = browser.switch_to_alert()
    alert_text = alert.text
    print(alert_text)


finally:
    time.sleep(3)
    browser.quit()