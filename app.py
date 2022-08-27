import streamlit as st
#from pycaret.regression import *
import pandas as pd
import keras
from keras.models import load_model


st.title('Charge&Guess')
st.markdown('''
Please use input data
''')

ok = st.button("Calculate Salary")

#model = load_model('CV_RF_Regression')
model = models.load_model('CV_RF_Regression.h5')

age = 20
sex = 0
bmi = 25.2
children = 3 
smoker = 0
region = 2

features ={'age': age, 'sex': sex ,
           'bmi': bmi, 'children': children,
           'smoker': smoker, 'region': region}
features_df  = pd.DataFrame([features])

if ok:
    #st.write([age,sex,bmi,children,smoker,region])
    st.write(features_df)
    #charges = reg_model.predict(data_pre)
    #charges = model_file.predict(features_df)
    
    charges = predict_model(model, data=features_df)
    st.write(charges)
