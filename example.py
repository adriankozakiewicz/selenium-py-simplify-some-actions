from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common import By

import seleniumSimplifySomeActions as simplify

# browser init
firefox_binary = FirefoxBinary(r'C:/Program Files/Mozilla Firefox/firefox.exe')

options = Options()
options.binary = FirefoxBinary('geckodriver.exe')

browser = webdriver.Firefox(firefox_binary=firefox_binary,options=options)

browser.get('https://example.com/')

#simple check, css query selector
el = simplify.findCheck(browser, ".my-element")
if not el:
    print("Element not found")

#change check method
el = simplify.findCheck(browser, "my-id", command=By.ID)
if not el:
    print("Element not found")


# 3 tries
el = simplify.findCheckRepeat(browser, ".my-element")
if not el:
    print("Element not found")

# 5 tries; custom delay
el = simplify.findCheckRepeat(browser, ".my-element")
if not el:
    print("Element not found")


# try for 10s wait 2s before first try, delay 0.2s
el = simplify.findCheckRepeat(browser, ".my-element", max_tries=None, max_time=10, delay=0.2, wait=2)
if not el:
    print("Element not found")


