import streamlit as st
import pandas as pd
from PIL import Image


st.title('Charge&Guess')
st.markdown('''
Please use input data
''')


st.sidebar.title("Operations on the Dataset")

#st.subheader("Checkbox")
w1 = st.sidebar.checkbox("Sample data ", False)
w2 = st.sidebar.checkbox('BMI calculator', False)

if w1:
    st.write('Sample data')
    image = Image.open('data_charges.png')
    st.image(image, 'Sample data')
    
if w2:
    st.write('BMI Calculator')
    img = Image.open('qrcode_www.calculator.net.png')
    st.image(img, 'BMI Calculator')

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Age")
    age = st.number_input('Insert age')
    st.write('The current number is ', age)
    
with col2:
    st.header("Sex")
    sex = st.selectbox(
     'gender',
     ('male', 'female'))

    st.write('You selected:', sex)
    if sex == 'male':
        sex = 1
    else:
        sex = 0
    st.write('You selected:', sex)
    
with col3:
    st.header("BMI")
    bmi = st.number_input('Insert bmi')
    st.write('The current number is ', bmi)

col4, col5, col6 = st.columns(3)
with col4:
    st.header("Child")
    children = st.number_input('Insert no of children')
    st.write('The current number is ', children)
    
with col5:
    st.header("smoker")
    smoker = st.selectbox(
     'smoker',
     ('yes', 'no'))

    st.write('You selected:', smoker)
    if smoker == 'yes':
        smoker = 1
    else:
        smoker = 0
    st.write('You selected:', smoker)
    
    
with col6:
    st.header("region")
    region = st.selectbox(
     'Region',
     ('southeast', 'southwest','northeast','northwest'))
    
    st.write('You selected:', region)
    if region == 'northeast':
        region = 0
    if region == 'northwest':
        region = 1
    if region == 'southeast':
        region = 2
    else:
        region = 3
    st.write('You selected:', region)


features ={'age': age, 'sex': sex ,
           'bmi': bmi, 'children': children,
           'smoker': smoker, 'region': region}
features_df  = pd.DataFrame([features])


ok = st.button("Tabulate")

if ok:
    st.write(features_df)
    st.write([[age,sex,bmi,children,smoker,region]])
    
