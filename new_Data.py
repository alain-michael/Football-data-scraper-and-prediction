import pandas as pd

# Define a tolerance level for comparing odds
tolerance = 0.01

# Read the 'output.csv' and 'combined_data.csv' files with explicit data types
output_data = pd.read_csv('output.csv')
combined_data = pd.read_csv('combined_data.csv', dtype={
    'home_odds': float,
    'draw_odds': float,
    'away_odds': float,
    'home_wins': int,
    'draws_no': int,
    'away_wins': int,
    'outcome': str  # Read 'outcome' as a string
})

# Initialize an empty DataFrame for new_data
new_data = pd.DataFrame(columns=['home_odds', 'draw_odds',
                        'away_odds', 'home_wins', 'draws_no', 'away_wins', '1/2'])

# Iterate through the rows of the 'output.csv' file
for index, row in output_data.iterrows():
    # Extract odds from the current row
    home_odds = row['home_odds']
    draw_odds = row['draw_odds']
    away_odds = row['away_odds']

    # Search for the corresponding game in 'combined_data.csv' based on odds
    matching_game = combined_data[
        (abs(combined_data['home_odds'] - home_odds) < tolerance) &
        (abs(combined_data['draw_odds'] - draw_odds) < tolerance) &
        (abs(combined_data['away_odds'] - away_odds) < tolerance)
    ]

    # Check if a matching game was found
    if not matching_game.empty:
        # Extract the required columns from the matching game
        relevant_data = matching_game[[
            'home_odds', 'draw_odds', 'away_odds', 'home_wins', 'draws_no', 'away_wins', '1/2']]

        # Concatenate the relevant data to the 'new_data' DataFrame
        new_data = pd.concat([new_data, relevant_data], ignore_index=True)

# Remove duplicate rows
new_data.drop_duplicates(inplace=True)

# Save the 'new_data' DataFrame to a new CSV file ('new_data.csv')
new_data.to_csv('new_data.csv', index=False)
