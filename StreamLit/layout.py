import streamlit as st
st.header("Registration Form", text_alignment="center")
col1,col2,col3=st.columns(3,border=True)
fn=col1.text_input("First Name",placeholder="First Name")
mn=col2.text_input("Middle Name",placeholder="Middle Name")
ln=col3.text_input("Last Name",placeholder="Last Name")
#First name is not allowed empty
if(fn==""):
    st.error("Please enter your first name")

if(fn!=""):
    fullname=fn+" "+mn+" "+ln
    st.success(f"Welcome on board! {fullname}")

email,code,number=st.columns([9,5,5],border=True)
email.text_input("Enter Email Address",placeholder="abc@company.com")
code.selectbox("Enter your country code",placeholder="+91",options=["+91","+92"])
num=number.text_input("Enter your phone number",placeholder="XXXXXXXXXX",max_chars=10)

st.text_input("Enter username")
pas,repass= st.columns(2,border=True)
passw=pas.text_input("Enter your password",type='password')
repassw=repass.text_input("Renter your password",type="password")
if(passw!=repassw):
    st.error("Incorrect password")
else:
    st.checkbox("I Agree to T&C",value=False)
    with st.expander("See Terms and COndition",expanded=False):
        st.write("Terms and conditions (T&Cs) are legally binding agreements between a service provider and users, setting rules for using a website, app, or service. They outline rights, obligations, prohibited behavior, and legal liabilities to protect both parties. Common clauses include intellectual property, payment terms, account termination, and governing law.")
    if(st.button("Submit")):
        st.success(f"Congrats {fn}!, Application successfully submitted")
        st.balloons()