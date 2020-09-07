from selenium.webdriver import Chrome
from selenium import webdriver

def configuration():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.add_argument(r"user-data-dir=./driver/data")
    #options.set_headless = True
    return webdriver.Chrome(
                    chrome_options=options,
                    executable_path=r"./driver/chromedriver"
                )
    