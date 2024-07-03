import streamlit as st
import pickle
import json
import pandas as pd

# Load the model from the pickle file
def load_model():
    with open('model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

# Load column names from JSON file
def load_columns():
    with open("columns.json", "r") as f:
        columns = json.load(f)['data_columns']
    return columns

def show_predict_page():
    st.title("Total Cost Prediction")
    st.sidebar.header('Input Features')

    columns = load_columns()

    input_values = {}

    for col in columns:
        if col.lower() not in ['discount', 'create_date', 'quote_amount', 'total_cost']:
            input_values[col] = st.sidebar.number_input(f"{col.capitalize().replace('_', ' ')}", value=0.0)

    # When 'Predict' button is clicked
    if st.sidebar.button("Predict Total Cost"):
        input_df = pd.DataFrame([input_values])

        model = load_model()
        try:
            prediction = model.predict(input_df)
            st.write(f"### Predicted Total Cost: ${prediction[0]:,.2f}")
        except Exception as e:
            st.error(f"Prediction error: {e}")

def main():
    st.set_page_config(page_title="Total Cost Prediction", layout="wide")

    show_predict_page()

if __name__ == "__main__":
    main()
