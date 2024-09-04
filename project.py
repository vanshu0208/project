import streamlit as st
st.header('Welcome to the ABC Bank')
st.title('Loan Calculator')
st.text_input('Enter your name: ')
x=st.text_input('Enter your 4-digit pin: ')
if len(x)==4:
    st.write('Login Successful')
elif len(x)==0:
    st.write('')
else:
    st.write('Re-enter')
st.radio("Do you want to take Loan?",['Yes','No'])
a=st.number_input('Enter the loan amount: ')
t=st.number_input('Enter the time period: ')
st.write('INTEREST RATE: 6% p.a')
c=st.button('Calculate')
z=1
if c==1:
    SI=(a*6*t)/100
    SI_final=a+SI
    m=(a*6*t)/(100*12)
    st.write('Total amount to be paid after given time is : ',SI_final)
    st.write('Total yearly Interest is : ',SI)
    st.write('Total monthly EMI is : ', m)
    st.balloons()
    z+=1
if z==2:
    st.write('Pay EMI on time 😡')
    st.write('Thanks for your visit')
