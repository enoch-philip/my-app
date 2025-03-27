import streamlit as st
import joblib
st.title('loan approval process automation')
model=joblib.load('loan_data1.joblib')
gender=st.number_input('enter your gender')
married=st.number_input('Are you married 1,0')
income=st.number_input('enter your income')
la=st.number_input('enter loan ammount in thousands')
if st.button ('loan predict'):
    prediction =model.predict([[gender,married,income,la]])
    if prediction=='y':
        print('approved')
    else:
        print("not approved")
        
