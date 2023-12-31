import csv
from selenium import webdriver
from edge_logging_config import configure_edge_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Initialize the Edge WebDriver and supress the errrors
log_file_path = "webdriver.log"
driver = configure_edge_driver(log_file_path)
try:
    # navigate to get the odds and the odds elements
    driver.get('https://www.betpawa.rw/virtual-sports?virtualTab=upcoming')

    # Wait for odds elements to load, with a timeout of 10 seconds
    odds_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'span.event-odds'))
    )

    # Extract the odds
    odds = [odds_element.text for odds_element in odds_elements]

    # Loop to get the odds
    with open('output.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['game_no', 'home_odds', 'draw_odds', 'away_odds'])
        for j in range(0, 30, 3):
            home_odds, draw_odds, away_odds = tuple(odds[j:j+3])
            game_no = (j//3)+1
            # Write the data to the CSV
            writer.writerow([game_no, home_odds, draw_odds, away_odds])

except TimeoutException:
    print("Timeout error: The page did not load within the expected time.")

finally:
    # Always quit the driver to close the browser window
    driver.quit()
