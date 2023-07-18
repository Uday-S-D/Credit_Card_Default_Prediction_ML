import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Import pickle model file
model = pickle.load(open('credit_card_default.pkl1','rb'))

# Home Page for the Streamlit app
def home():
    st.title("Credit Card Default Prediction")
    st.write("Please enter the following information:")
    limit_bal = st.number_input("Credit Limit (in dollars)")
    sex = st.selectbox("Sex", ['Male', 'Female'])
    age = st.number_input("Age")
    education = st.selectbox("Education", ['Uneducated', 'Middle School', 'High School', 'Undergraduate', 'Postgraduate', 'PhD', 'Others'])
    marriage = st.selectbox("Marital Status", ['Unmarried', 'Married', 'Divorced', 'Widowed'])
    payment_history_april = st.selectbox("Payment Status of April", [0,-1,-2,1,2,3,4,5,6,7,8,9])
    payment_history_may = st.selectbox("Payment Status of may",[0,-1,-2,1,2,3,4,5,6,7,8,9])
    payment_history_june =  st.selectbox("Payment Status of June",[0,-1,-2,1,2,3,4,5,6,7,8,9])
    payment_history_july = st.selectbox("Payment Status of july",[0,-1,-2,1,2,3,4,5,6,7,8,9])
    payment_history_aug = st.selectbox("Payment Status of august",[0,-1,-2,1,2,3,4,5,6,7,8,9])
    payment_history_sep = st.selectbox("Payment Status of september",[0,-1,-2,1,2,3,4,5,6,7,8,9])
    april_bill = st.number_input("Average april Bill Amount (in dollars)")
    may_bill = st.number_input("Average may Bill Amount (in dollars)")
    june_bill = st.number_input("Average june Bill Amount (in dollars)")
    july_bill = st.number_input("Average july Bill AmountA(in dollars)")
    aug_bill = st.number_input("Average august Bill Amount (in dollars)")
    sep_bill = st.number_input("Average september Bill Amount (in dollars)")
    april_payment = st.number_input("April Payment Amount (in dollars)")
    may_payment = st.number_input("May Payment Amount (in dollars)")
    june_payment = st.number_input("June Payment Amount (in dollars)")
    july_payment = st.number_input("July Payment Amount(in dollars)")
    aug_payment = st.number_input("August Payment Amount (in dollars)")
    sep_payment = st.number_input("September Payment Amount (in dollars)")
   
    # Module to convert categorical sex values to numerical values
    if sex == 'Male':
        sex = 1
    else:
        sex = 2

    # Education module to convert categorical values into numerical
    education_dict = {
        'Uneducated': 0,
        'Middle School': 1,
        'High School': 2,
        'Undergraduate': 3,
        'Postgraduate': 4,
        'PhD': 5,
        'Others': 6
    }
    education = education_dict[education]

    # Marriage module to assign the numerical value for categorical inputs
    marriage_dict = {
        'Unmarried': 0,
        'Married': 1,
        'Divorced': 2,
        'Widowed': 3
    }
    marriage = marriage_dict[marriage]

    # Payment module to assign the numerical value for categorical inputs
#    payment_dict = {
#        'On Time': 0,
#        'Advance One Month': -1,
#       'Advance Two Months': -2,
#        'Delay One Month': 1,
#       'Delay Two Months': 2,
#        'Delay Three Months': 3,
#        'Delay Four Months': 4,
#        'Delay Five Months': 5,
#        'Delay Six Months': 6,
#        'Delay Seven Months': 7
#    }
#    payment_history = payment_dict[payment_history]

    # Module to predict the outcome using ML algorithm
    prediction = model.predict([[limit_bal, sex, education, marriage, age,
                                april_bill,may_bill,june_bill,july_bill,aug_bill,sep_bill,april_payment, may_payment, june_payment,july_payment,aug_payment,sep_payment,
                                payment_history_april,payment_history_may,payment_history_june,payment_history_july,payment_history_aug,payment_history_sep]])

    # Converting the categorical values into integers
#    if prediction == 1:
#        output = 'The credit card holder WILL BE DEFAULTER in the next month'
#    else:
#        output = 'The Credit card holder WILL NOT BE DEFAULTER in the next month'
    
    if st.button("Predict"):
        if prediction == 1:
            output = 'The credit card holder WILL BE DEFAULTER in the next month'
            st.write("Prediction: {}".format(output))
        else:
            output = 'The credit card holder WILL NOT BE DEFAULTER in the next month'
            st.write('Prediction:{}'.format(output))


# Driver Code
if __name__ == '__main__':
    home()

