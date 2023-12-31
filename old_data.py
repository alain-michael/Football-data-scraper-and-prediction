import pandas as pd

# Read the training_set.csv and combined_data.csv files into DataFrames
training_set = pd.read_csv('training_set.csv')
combined_data = pd.read_csv('combined_data.csv')

# Create empty lists to store the odds for each game
home_odds_list = []
draw_odds_list = []
away_odds_list = []

# Iterate through the rows of the training_set DataFrame
for index, row in training_set.iterrows():
    home_team = row['Home_team']
    away_team = row['Away_team']

    # Search for the corresponding game in combined_data
    matching_game = combined_data[
        (combined_data['Home_team'] == home_team) &
        (combined_data['Away_team'] == away_team)
    ]

    if not matching_game.empty:
        # Get the odds for the matching game
        home_odds = matching_game.iloc[0]['home_odds']
        draw_odds = matching_game.iloc[0]['draw_odds']
        away_odds = matching_game.iloc[0]['away_odds']
        # Append the odds to the lists
        home_odds_list.append(home_odds)
        draw_odds_list.append(draw_odds)
        away_odds_list.append(away_odds)
    else:
        # If the game is not found, you can decide what to do (e.g., fill with NaN or raise an error)
        home_odds_list.append(None)
        draw_odds_list.append(None)
        away_odds_list.append(None)

# Add the odds columns to the training_set DataFrame
training_set['home_odds'] = home_odds_list
training_set['draw_odds'] = draw_odds_list
training_set['away_odds'] = away_odds_list

# Concatenate the DataFrames
combined_data = pd.concat([combined_data, training_set], ignore_index=True)

# Save the updated combined_data back to the combined_data.csv file
combined_data.to_csv('combined_data.csv', index=False)
