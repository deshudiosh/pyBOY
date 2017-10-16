from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import logger
import vote_for_list

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--headless")


def loop(project:dict, cur_iter=0):
    driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=chrome_options)
    driver.get(project["url"])

    project["cur_iter"] = cur_iter

    try:
        driver.find_element_by_class_name("confirmVote").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "voteComplete")))
        logger.success(project)
        cur_iter += 1
    except:
        logger.fail(project)

    driver.close()

    if cur_iter < project["num_iter"]:
        loop(project, cur_iter)
    else:
        print("Finished!")

loop(vote_for_list.get_project_list()[0])
