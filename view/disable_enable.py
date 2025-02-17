import streamlit as st

def run():
    st.subheader("Disable/Enable Interfaces")
    st.selectbox("Select Interface", ["ether1", "ether2", "ether3", "wlan1", "wlan2"])
    st.selectbox("Action", ["Disable", "Enable"])
    if st.button("Submit"):
        st.write("Submit button clicked.")

