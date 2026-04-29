import streamlit as st
from datetime import date
tod=date.today()
#print(tod.month)

min_date=date(tod.year-125,1,1)
max_date=tod
dob=st.date_input("Enter date of birth",min_value=min_date,max_value=tod,value="today",format="DD/MM/YYYY")
if(st.button("Submit")):
    prage=tod.year-dob.year
    if((dob.month,dob.day)>(tod.month,tod.day)):
        diff=1
    else:
        diff=0
    prage=prage-diff
    if(prage>18):
        st.success("Congratulation you can vote")
        st.balloons()
    else:
        st.error(f":disappointed:, Sorry you can't vote, present age is {prage}, please wait for another {18-prage} year")