from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import time


def test_user_can_see_the_adding_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    try:
        assert WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME,
                                'btn.btn-lg.btn-primary.btn-add-to-basket')))
        # process the exception...
    except (TimeoutException):
        raise TimeoutException("Within 5 seconds, the element doesn't found")
    # uncomment this string for additional checking...
    # time.sleep(30)
