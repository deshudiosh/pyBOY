from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import count_check
import logger
import vote_for_list

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--headless")


def loop(project:dict):
    driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=chrome_options)
    driver.get(project["url"])

    try:
        driver.find_element_by_class_name("confirmVote").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "voteComplete")))
        logger.success(project)
    except:
        logger.fail(project)

    driver.close()

    #TODO: count successes on file copy (so write acces wont fail in logs_counter)
    counted_successes = count_check.get_success_num(project["url"])
    print(counted_successes, "/", project["num_iter"])

    if counted_successes < project["num_iter"]:
        loop(project)
    else:
        print("Finished!")


for project in vote_for_list.get_project_list():
    loop(project)
