import streamlit as st

st.title("ToxiShield AI")

text = st.text_area("Enter a comment")

if st.button("Analyze"):
    st.write("Prediction will appear here")
