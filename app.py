import streamlit as st
import joblib
st.title('Loan Approval Process Automation')
model = joblib.load('loan_data1.joblib')
gender = st.number_input('Enter your gender (1 for Male, 0 for Female)', min_value=0, max_value=1)
married = st.number_input('Are you married? (1 for Yes, 0 for No)', min_value=0, max_value=1)
income = st.number_input('Enter your income', min_value=0)
loan_amount = st.number_input('Enter loan amount in thousands', min_value=0)
if st.button('Predict Loan Approval'):
    prediction = model.predict([[gender, married, income, loan_amount]])
    if prediction == 'y':  
        st.write('Loan Approved!')
    else:
        st.write('Loan Not Approved')
