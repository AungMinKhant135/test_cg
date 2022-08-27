import os
import numpy as np
import cv2
from tensorflow.keras.models import load_model
import streamlit as st
from streamlit_drawable_canvas import st_canvas


st.title('Charge&Guess')
st.markdown('''
Please use input data
''')

ok = st.button("Calculate Salary")

#model = load_model('CV_RF_Regression')
#model = models.load_model('CV_RF_Regression.h5')
#model =load_model('CV_RF_Regression.h5')
model =load_model('CV_RF_Regression')
#model = load_model('cnn.h5')


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
