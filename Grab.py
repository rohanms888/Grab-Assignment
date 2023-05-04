from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(options=options)

# Navigate to the Grab food page
driver.get('https://food.grab.com/ph/en/')

# Wait for the page to load
time.sleep(5)

# Find the "Load more" button and click it until all restaurants are displayed
load_more_button = driver.find_element(By.XPATH, "//button[@data-test-id='load-more-button']")
while load_more_button.is_displayed():
    action = ActionChains(driver)
    action.move_to_element(load_more_button).perform()
    load_more_button.click()
    time.sleep(2)

# Find all the restaurant elements
restaurant_elements = driver.find_elements(By.XPATH, "//div[@class='cXIPh _3O_kR']")

# Loop through each restaurant element and extract the latitude and longitude
for restaurant in restaurant_elements:
    try:
        # Hover over the restaurant element to reveal the hidden latitude and longitude
        action = ActionChains(driver)
        action.move_to_element(restaurant).perform()

        # Extract the latitude and longitude from the tooltip
        tooltip = driver.find_element(By.XPATH, "//div[@class='_2ZQhq']")
        latitude, longitude = tooltip.get_attribute('innerHTML').split(',')

        print(f'Latitude: {latitude.strip()} - Longitude: {longitude.strip()}')
    except:
        continue

# Close the browser window
driver.quit()
