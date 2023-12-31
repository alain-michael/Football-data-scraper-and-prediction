import csv
# Load odds data
with open('output.csv', mode='r') as odds_file:
    odds_reader = csv.DictReader(odds_file)
    odds_data = list(odds_reader)

# Load scores data
with open('training_set.csv', mode='r') as scores_file:
    scores_reader = csv.DictReader(scores_file)
    scores_data = list(scores_reader)

# Create a new list to store the combined data
combined_data = []

# Iterate through the rows and combine the data
for game_no in range(1, 11):  # Assuming there are 10 games
    # Find the corresponding rows in odds and scores data
    odds_match = odds_data[game_no - 1]
    scores_match = scores_data[game_no - 1]

    # Extract the relevant information from each file
    home_team = scores_match['Home_team']
    away_team = scores_match['Away_team']
    half_time_score = scores_match['half_time_score']
    home_score = scores_match['home_score']
    away_score = scores_match['away_score']
    home_odds = odds_match['home_odds']
    draw_odds = odds_match['draw_odds']
    away_odds = odds_match['away_odds']

    # Create a dictionary to represent the combined data
    combined_match = {
        'game_no': game_no,
        'Home_team': home_team,
        'Away_team': away_team,
        'half_time_score': half_time_score,
        'home_score': home_score,
        'away_score': away_score,
        'home_odds': home_odds,
        'draw_odds': draw_odds,
        'away_odds': away_odds
    }

    # Append the combined data to the list
    combined_data.append(combined_match)

# Save the combined data to a new CSV file
with open('combined_data.csv', mode='a', newline='') as combined_file:
    fieldnames = ['game_no', 'Home_team', 'Away_team', 'half_time_score',
                  'home_score', 'away_score', 'home_odds', 'draw_odds', 'away_odds']
    writer = csv.DictWriter(combined_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(combined_data)
