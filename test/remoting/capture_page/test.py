import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("nwapp=" + os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Chrome(executable_path=os.environ['CHROMEDRIVER'], chrome_options=chrome_options)
try:
    print driver.current_url
    time.sleep(5)
    driver.switch_to_window(driver.window_handles[-1])
    img = driver.find_element_by_id('png')
    assert(img.size['width'] > 50 and img.size['height'] > 50)
    img2 = driver.find_element_by_id('jpg')
    assert(img.size['height'] == img2.size['height'] and img.size['width'] == img2.size['width'])
finally:
    driver.quit()
