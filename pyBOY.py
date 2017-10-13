from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

success, fail = 0, 0


def establish():
    global success, fail

    driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=chrome_options)
    driver.get("https://boyawards.secure-platform.com/a/gallery/rounds/12/vote/10266")

    driver.find_element_by_class_name("confirmVote").click()

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "voteComplete")))
        success +=1
        print("success/fail", success, fail)
        sleep(1)
        driver.quit()
    except:
        fail +=1
        print("success/fail", success, fail)
        sleep(1)
        driver.quit()

    establish()

establish()
