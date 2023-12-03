import streamlit as st
import pandas as pd
import numpy as np
import pickle


st.header('Penguin Prediction App')

st.write(
    """

    This is an app that predicts the **Palmer Penguins** species

    Data obtained from the [palmerpenguins library](https://github.com/allisonhorst/palmerpenguins) in R by Allison Horst.
    """
)

st.sidebar.header("User Input Features")

st.sidebar.markdown(
    """
    [Example CSV input]
    """
)

# Collect user input features into dataframe

def user_input_features():
    island = st.sidebar.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
    sex = st.sidebar.selectbox('Sex', ('male', 'female'))
    bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1, 59.6, 43.9)
    bill_depth_mm = st.sidebar.slider('Bill depth', 13.1, 21.5, 17.2)
    flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
    body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
    data = {
        'island': island,
        'sex': sex,
        'bill_length_mm': bill_length_mm,
        'bill_depth_mm': bill_depth_mm,
        'flipper_length_mm': flipper_length_mm,
        'body_mass_g': body_mass_g
    }
    features = pd.DataFrame(data, index=[0])
    return features

uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

if uploaded_file:
    input_df = pd.read_csv(uploaded_file)
else:
    input_df = user_input_features()


# Combine user input features with entire penguins dataset

penguins_raw = pd.read_csv('penguins_cleaned.csv')
penguins = penguins_raw.drop(columns=['species'])
df = pd.concat([input_df, penguins], axis=0)

# Encoding of ordinal features

encode = ['sex', 'island']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df, dummy], axis=1)
    del df[col]

df = df[:1] # Select only the first row 

# Display user input features
st.subheader('User Input features')

if uploaded_file:
    st.write(df)
else:
    st.write('Awaiting CSV file. Currently using example input parameters')
    st.write(df)

# Read in saved classification model
load_clf = pickle.load(open('penguins_clf.pkl', 'rb'))

# Apply model to make predictions
prediction = load_clf.predict(df)
prediction_probability = load_clf.predict_proba(df)

st.subheader('Prediction')
penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
st.write(penguins_species[prediction])

st.subheader('Prediction Probability')
st.write(prediction_probability)
