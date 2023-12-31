import joblib
import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from scipy.stats import uniform, randint

# Step 1: Load the dataset
data = pd.read_csv('combined_data.csv')

# Filter the data to include games with odds greater than 1.99
filtered_data = data[data['home_odds'] >= 1.99]

# replace 'x' with '0' and convert to int
filtered_data.loc[filtered_data['outcome'] == 'x', 'outcome'] = 0

# Split the data into features (X) and target (y)
x = filtered_data.drop(['game_id', 'Home_team', 'Away_team', 'home_score', 'away_score',
                       'half_time_score', '1/2', 'outcome', 'game_no', 'game_count'], axis=1)
y = filtered_data['1/2']

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42)

# Step 2: Define the Bernoulli Naive Bayes model
nb = BernoulliNB()

# Step 3: Define hyperparameter distributions for Randomized Search
param_dist = {
    # Randomly sample alpha from a uniform distribution between 0 and 1
    'alpha': uniform(0, 1),
}

# Step 4: Perform randomized search with cross-validation
randomized_search = RandomizedSearchCV(
    estimator=nb, param_distributions=param_dist, n_iter=10, cv=5, scoring='accuracy', random_state=42)
randomized_search.fit(x_train, y_train)

# Step 5: Get the best hyperparameters from the randomized search
best_alpha = randomized_search.best_params_['alpha']

print(f"Best Alpha: {best_alpha}")

# Step 6: Train the Bernoulli Naive Bayes model with the best hyperparameters
best_nb = BernoulliNB(alpha=best_alpha)
best_nb.fit(x_train, y_train)

# Step 7: Make predictions on the test set
y_pred = best_nb.predict(x_test)

# Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Create a Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:')
print(conf_matrix)

# Generate a Classification Report
class_report = classification_report(y_test, y_pred)
print('Classification Report:')
print(class_report)

# Step 8: Save the trained model to a file
model_filename = 'best_bernoulli_naive_bayes_model_1_2.pkl'
joblib.dump(best_nb, model_filename)

print(f"Trained model saved to {model_filename}")
# important varibales
draws = len(data[data['outcome'] == 'x'])
print(f"Number of draws with outcome 'x': {draws}")
away = len(data[data['outcome'] == '2'])
print(f"Number of draws with outcome '2': {away}")
home = len(data[data['outcome'] == '1'])
print(f"Number of draws with outcome '1': {home}")
print(f"Number of desired games :{len(filtered_data)}")
