from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(options=options)


driver.get('https://food.grab.com/ph/en/')


time.sleep(5)


load_more_button = driver.find_element(By.XPATH, "//button[@data-test-id='load-more-button']")
while load_more_button.is_displayed():
    action = ActionChains(driver)
    action.move_to_element(load_more_button).perform()
    load_more_button.click()
    time.sleep(2)


restaurant_elements = driver.find_elements(By.XPATH, "//div[@class='cXIPh _3O_kR']")


for restaurant in restaurant_elements:
    try:
        
        action = ActionChains(driver)
        action.move_to_element(restaurant).perform()

        
        tooltip = driver.find_element(By.XPATH, "//div[@class='_2ZQhq']")
        latitude, longitude = tooltip.get_attribute('innerHTML').split(',')

        print(f'Latitude: {latitude.strip()} - Longitude: {longitude.strip()}')
    except:
        continue


driver.quit()
