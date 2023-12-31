import pandas as pd

# Load your DataFrame from the CSV file (combined_data.csv in your case)
df = pd.read_csv('combined_data.csv')

# Function to calculate 'game_id' based on the number of games played by each unique pair of teams


def calculate_game_id(dataframe):
    # Create a dictionary to keep track of the game_id for each unique pair of teams
    game_id_dict = {}
    game_id_list = []
    current_game_id = 0

    for index, row in dataframe.iterrows():
        home_team = row['Home_team']
        away_team = row['Away_team']
        pair = (home_team, away_team)

        # Check if the pair is in the dictionary, if not, assign a new game_id
        if pair not in game_id_dict:
            game_id_dict[pair] = current_game_id
            current_game_id += 1

        # Append the game_id to the list
        game_id_list.append(game_id_dict[pair])

    return game_id_list


# Calculate 'game_id' and add it as a new column
df['game_id'] = calculate_game_id(df)

# Function to determine the outcome based on home_score and away_score


def determine_outcome(row):
    if row['home_score'] > row['away_score']:
        return '1'
    elif row['home_score'] < row['away_score']:
        return '2'
    else:
        return 'x'


# Apply the determine_outcome function to each row and create a new 'outcome' column
df['outcome'] = df.apply(determine_outcome, axis=1)

# Function to create a new column '1/2' based on 'outcome'


def add_1_2_column(dataframe):
    # Create a new column '1/2' and set it to 0 by default
    dataframe['1/2'] = 0

    # Where 'outcome' is not 'x' (1 or 2), set '1/2' column to 1
    dataframe.loc[dataframe['outcome'] != 'x', '1/2'] = 1


# Call the function to add the '1/2' column
add_1_2_column(df)

# Function to calculate statistics for each unique game combination


def calculate_game_statistics(dataframe):
    # Create new columns to store the statistics
    dataframe['home_wins'] = 0
    dataframe['draws_no'] = 0
    dataframe['away_wins'] = 0
    dataframe['game_count'] = 0

    # Iterate through unique game combinations
    for index, game_row in dataframe.iterrows():
        home_team = game_row['Home_team']
        away_team = game_row['Away_team']

        # Filter the DataFrame to get rows for the current game combination
        game_rows = dataframe[(dataframe['Home_team'] == home_team) & (
            dataframe['Away_team'] == away_team)]

        # Calculate statistics for the current game combination
        home_wins = len(game_rows[game_rows['outcome'] == '1'])
        draws_no = len(game_rows[game_rows['outcome'] == 'x'])
        away_wins = len(game_rows[game_rows['outcome'] == '2'])
        game_count = len(game_rows)

        # Update the corresponding rows in the DataFrame
        dataframe.loc[(dataframe['Home_team'] == home_team) & (
            dataframe['Away_team'] == away_team), 'home_wins'] = home_wins
        dataframe.loc[(dataframe['Home_team'] == home_team) & (
            dataframe['Away_team'] == away_team), 'draws_no'] = draws_no
        dataframe.loc[(dataframe['Home_team'] == home_team) & (
            dataframe['Away_team'] == away_team), 'away_wins'] = away_wins
        dataframe.loc[(dataframe['Home_team'] == home_team) & (
            dataframe['Away_team'] == away_team), 'game_count'] = game_count


# Calculate game statistics for your dataset
game_statistics = calculate_game_statistics(df)

# Save the updated DataFrame to a new CSV file
df.to_csv('combined_data.csv', index=False)
