import time
from BrainBucket.webelements.browser12 import Browser

URL = 'https://techskillacademy.net/brainbucket/index.php?route=common/home'


browser = Browser(URL)
driver = browser.get_driver()

time.sleep(2)
driver.quit()