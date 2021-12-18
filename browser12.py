from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from BrainBucket.utils.config_reader import ConfigReader


class Browser:
    """
    This class is wrapper around Selenium driver
    """

    def __init__(self, url, browser_name="", time_wait=10):
        # decide which browser to open, can be extended
        if browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            #AN my code starts Lesson 12.3.2
            configs = ConfigReader("config.ini")
            options.add_argument("--width={}".format(configs.get_width_viewport('environment')))
            options.add_argument("--height={}".format(configs.get_height_viewport('environment')))
            # AN my code ends


            firefox_profile = webdriver.FirefoxProfile()
            firefox_profile.set_preference("browser.urlbar.showPopup", True)

            self.driver = webdriver.Firefox(firefox_profile=firefox_profile, executable_path='../drivers/geckodriver')
            self.driver.maximize_window()
        else:
            options = webdriver.ChromeOptions()
            #options.add_argument("--start-maximized")
            # AN my code starts Lesson 12.3.2
            configs = ConfigReader("config.ini")
            options.add_argument("--window-size={},{}".format(configs.get_width_viewport('environment'), configs.get_height_viewport('environment')))
            print("--window-size={},{}".format(configs.get_width_viewport('environment'), configs.get_height_viewport('environment')))
            # AN my code stops
            options.add_argument("--incognito")
            #options.add_argument("--disable-popup-blocking")
            options.add_experimental_option("excludeSwitches", ['enable-automation'])
            self.driver = webdriver.Chrome(executable_path=r"C:\Users\Aleksei ThinkPad\PycharmProjects\chromedriver.exe", options=options)

        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.implicitly_wait(time_wait)  # by default 10, but we can add this like a parameter

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()
