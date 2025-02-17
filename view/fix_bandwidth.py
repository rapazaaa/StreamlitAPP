import streamlit as st

def run():
    st.subheader("Bandwidth Fix")
    st.text_input("Target IP Address")
    st.number_input("Upload Speed (Mbps)", min_value=0.0)
    st.number_input("Download Speed (Mbps)", min_value=0.0)
    st.button("Submit")
