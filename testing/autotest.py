from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def click_button_100_times():
    driver = webdriver.Edge()
    driver.maximize_window()
    try:
        driver.get("https://uzum.uz/uz/product/smartfon-tecno-spark-901159")

        button_locator = (By.XPATH, "/html/body/div/main/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/button")


        time.sleep(5)
        for i in range(100):
            button = driver.find_element(*button_locator)
            button.click()
            time.sleep(1)
    finally:
        driver.quit()


click_button_100_times()
