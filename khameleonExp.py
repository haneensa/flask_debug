#!/usr/bin/env python2.7

# Things you need for micerobot.py to work:
#
#   1. You need the Google Chrome browser.
#
#   2. You need Selenium.
#
#       pip install selenium
#
#   3. You need to put the ChromeDriver binary in your PATH.
#
#       https://sites.google.com/a/chromium.org/chromedriver/downloads
import time

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from os import system, getcwd


# system("make multi")

def wait_for(condition_function):
    start_time = time.time()
    while time.time() < start_time + 600:
        alert = condition_function()
        if alert:
            return True
        else:
            time.sleep(1)
    raise Exception(
        'Timeout waiting for {}'.format(condition_function.func_name)
    )


class wait_for_alert(object):

    def __init__(self, browser):
        self.browser = browser

    def __enter__(self):
        self.browser.get("http://100.64.0.1:8000/")

    def __exit__(self, *_):
        wait_for(self.show_alert)
        print "finish test", self.arguments

    def show_alert(self):
        try:
            alert = self.browser.switch_to.alert
            return alert
        except NoAlertPresentException:
            return False


def testLatency():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
    with wait_for_alert(browser):
        print "start"

if __name__ == "__main__":
    from werkzeug.serving import WSGIRequestHandler, BaseWSGIServer
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    BaseWSGIServer.protocol_version = "HTTP/1.1"
    testLatency()
