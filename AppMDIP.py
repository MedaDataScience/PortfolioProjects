# necessary libraries

import pandas as pd
import numpy as np
import pickle as pkl
import streamlit as st

model = pkl.load(open('InsuranceRFRG.pkl', 'rb'))

st. header('Medical Insurance Premium Prediction Algorithm')

sex = st.selectbox('Sex of Insuree', ['--Select Option--','Male', 'Female'])
age = st.number_input('Age of Insuree', 10, 80)
BMI = st.slider('BMI of Insuree', 15, 50)
smoker = st.selectbox('Smoking Status', ['--Select Option--','Yes', 'No'])
children = st.slider('Number of Children', 0, 5)
region = st.selectbox('Region of Residence', ['--Select Option--','Northeast','Southeast','Southwest','Northwest'])

if sex == 'Female':
    sex = 0
elif sex == 'Male':
    sex = 1
else:
    print('Please select sex') 

if smoker == 'Yes':
    smoker = 1
elif smoker == 'No':
    smoker = 0
else:
    print('Please select smoking status') 

if region == 'Northeast':
    region = 1
elif region == 'Southeast':
    region = 2
elif region == 'Southwest':
    region = 3
elif region == 'Northwest':
    region = 4
else:
    print('Please select region')

input_data = (age, sex, BMI, children, smoker, region)
input_data = np.asarray(input_data)
input_data = input_data.reshape(1,-1)

if st.button('Predict'):
    predict_premium = model.predict(input_data)

    display_string = 'Calculated Premium is $' + str(round(predict_premium[0],2)) + ' USD'

    st.markdown(display_string)
else:
    st.markdown('Please fill out required information')