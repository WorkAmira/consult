# Example: Ensure column names and order match during prediction
import pandas as pd
import pickle
import json

# Load your model
with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Load your column names from JSON
with open('columns.json', 'r') as file:
    columns = json.load(file)['data_columns']

# Create a sample input dataframe (adjust according to your actual input)
input_data = {
    'QTY_QUOTED': 10,
    'QUOTED_PRICE': 100,
    'QUOTE_ADDRESSID': 12345,
    'QUOTE_EXCHRATE': 1.2
}

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Ensure columns are in the same order as during training
input_df = input_df.reindex(columns=columns)

# Predict using the loaded model
prediction = loaded_model.predict(input_df)

print(f"Predicted value: {prediction[0]}")

# Ensure column names in input_df match X_train.columns
input_df.columns = X_train.columns

# Make sure to convert categorical columns to the appropriate format (if needed)
# Example: input_df['QUOTE_ADDRESSID'] = input_df['QUOTE_ADDRESSID'].astype(float)

# Ensure the input data is in the same format as during training (e.g., numeric types)

# Now, you can proceed with prediction
prediction = loaded_model.predict(input_df)

# Display or use the prediction results as needed
print(prediction)
