import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from edge_logging_config import configure_edge_driver
# Initialize the Edge WebDriver and remove the errors
log_file_path = "webdriver.log"
driver = configure_edge_driver(log_file_path)
try:
    # Navigate to the URL to get live scores
    driver.get(
        'https://www.betpawa.rw/virtual-sports/matchday/9843/354374')

    # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//h3[@class="title"]'))
    )

    # Find team name elements using XPath
    team_name_elements = driver.find_elements(By.XPATH, '//h3[@class="title"]')

    # Extract team names
    team_names = [team.text.strip() for team in team_name_elements]

    # Find live score elements
    score_elements = driver.find_elements(By.CSS_SELECTOR, 'div.score')

    # Extract live scores
    live_scores = [score.text for score in score_elements]

    # Open a CSV file for writing
    with open('training_set.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['game_no', 'Home_team', 'Away_team',
                         'half_time_score', 'home_score', 'away_score', 'home_odds', 'draw_odds', 'away_odds'])

        # Iterate through the lists and write data to the CSV
        for i in range(0, 10):
            # Extract team names from teams
            home_team, away_team = (team_names[i]).split(' - ')

            # Extract scores from live_scores
            scores = (live_scores[i]).split(' ')
            half_time = tuple(scores[:3])  # Extract the score in brackets
            formatted_data = ''.join(half_time)

            # Remove any unnecessary characters
            half_time_score = formatted_data.replace('(', '').replace(')', '')

            home_score = scores[3]
            away_score = scores[5]
            game_no = i + 1
            if (game_no == 10):
                pass
            writer.writerow(
                [game_no, home_team, away_team, half_time_score, home_score, away_score])

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit the WebDriver
    driver.quit()
