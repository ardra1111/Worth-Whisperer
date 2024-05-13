import streamlit as st
from joblib import load
import numpy as np


def load_model():
    # Load the model
    model = load("WorthWhisperer.joblibe")
    return model


def predict_price(features):
    # Load the model
    model = load_model()
    # Predict the price
    price = model.predict(features)
    return price


def main():
    st.title('Worth-Whisperer')
    st.header(' House Price Predictor')
    st.write('Enter the values for the input features below.')

    # Input features
    features = ['RM', 'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRTO', 'B', 'LSTAT']
    input_data = {}

    # Create a row-wide table for input features
    input_row = st.columns(len(features))
    for i, feature in enumerate(features):
        input_data[feature] = input_row[i].text_input(f'{feature}', value='')

    if st.button('Predict'):
        # Convert input data to array
        input_array = np.array([[float(input_data[feature]) for feature in features]])

        # Predict house price
        predicted_price = predict_price(input_array)

        # Display predicted price
        st.header(f'The predicted price of the house is $ {predicted_price[0]:,.2f} thousand.')


if __name__ == '__main__':
    main()


