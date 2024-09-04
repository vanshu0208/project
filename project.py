import streamlit as st
st.title('Welcome to the ABC Bank')
st.header('Loan Calculator')
st.text_input('Enter your name: ')
x=st.text_input('Enter your 4-digit pin: ')
n=1
if len(x)==4:
    st.write('Login Successful')
    n+=1
    if n==2:
        st.radio("Are you self-employed or salaried employed?",options=['self-employed','salaried employed'])
        a=st.number_input('Enter the loan amount: ')
        t=st.number_input('Enter the time period: ')
        st.write('INTEREST RATE: 6% p.a')
        c=st.button('Calculate')
        if c==1:
            SI=(a*6*t)/100
            SI_final=a+SI
            m=(a*6*t)/(100*12)
            st.write('Total amount to be paid after given time is : ',SI_final)
            st.write('Total yearly Interest is : ',SI)
            st.write('Total monthly EMI is : ', m)
            st.balloons()
            o=st.button('Show documents')
            if o==1:
                st.write('**Here are the documents you need to deposit**: ')
                st.write('Aadhar Card')
                st.write(' Pan Card')
                st.write('Bank Account details')
                st.write('Salary slip')
                st.write('')
                st.write('Pay EMI on time 😡')
                st.write('Thanks for your visit')

elif len(x)==0:
    st.write('')
else:
    st.write('Re-enter')



