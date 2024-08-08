import streamlit as st
import helper
import pickle
model=pickle.load(open('model11.pkl','rb'))
st.header('Duplicate Question Pairs')
q1=st.text_input('Enter question1')
q2=st.text_input('Enter question2')


if st.button('Find'):
    query=helper.query_point_creator(q1,q2)
    result=model.predict(query)[0]


    if result:
        st.header('Duplicate')

    else :
        st.header('Not Duplicate')

