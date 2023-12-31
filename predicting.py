import joblib
import pandas as pd

# Load the trained model
model_filename = 'best_bernoulli_naive_bayes_model_1_2.pkl'
best_nb = joblib.load(model_filename)

# Load new data for prediction (replace 'new_data.csv' with your actual data file)
new_data = pd.read_csv('new_data.csv')
# Drop the '1/2' columns
x_new = new_data.drop(['1/2'], axis=1)

# Make predictions on the new data
y_pred_new = best_nb.predict(x_new)
# Print the predictions
print("Predictions:")
print(y_pred_new)
