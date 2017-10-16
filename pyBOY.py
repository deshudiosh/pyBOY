from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import counter

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

url = "https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10991"

def loop():
    driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=chrome_options)
    driver.get(url)

    try:
        driver.find_element_by_class_name("confirmVote").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "voteComplete")))
        counter.success(url)
        sleep(1)
    except:
        counter.fail(url)
        sleep(1)

    driver.close()
    loop()

loop()
