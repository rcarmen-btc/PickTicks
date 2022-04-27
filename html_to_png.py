from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options

from PIL import Image
from pathlib import Path
import sys

def main():
    
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=1080,1080")

    path = Path('/home/riser/Downloads/Uchkuch/result_htmls')
    files = [i for i in path.iterdir() if i.is_file()]


    for file in files:
        driver.get(file.as_uri())
        driver.find_element_by_tag_name('html').send_keys(Keys.CONTROL, '-')
        driver.find_element_by_tag_name('html').send_keys(Keys.CONTROL, '-')
        driver.set_window_size(1000, 1130)
        sleep(1)
        print(file.as_posix())
        driver.get_screenshot_as_file(file.as_posix() + '.png')
        sleep(1)
        im = Image.open(file.as_posix() + '.png')
        im_crop = im.crop((10, 16, 1240, 1245))
        im_crop.save(file.as_posix() + '.png', quality=100)
        sleep(1)

    driver.quit()



if __name__ == '__main__':
    main()
