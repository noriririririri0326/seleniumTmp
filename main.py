# selenium4.6以上ならドライバのDLとパス指定もいらなくなった。
# ↓だけでおｋ
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL :str = "https://www.yahoo.co.jp/"

class selenium_contllorer:
    def __init__(self):
        print("selenium_contllorer init")
        self.driver = webdriver.Chrome()

    def site_open(self):
        self.driver.get(URL)

    def end(self):
        self.driver.close()

    def get_element(self):
        pass

    def save_image(self):
        pass


def main():
    print("in main")
    sc = selenium_contllorer()
    sc.site_open()
    sc.end()

if __name__ == "__main__":
    main()
