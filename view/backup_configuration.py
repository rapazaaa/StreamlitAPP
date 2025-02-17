import streamlit as st

def run():
    st.subheader("Backup Configuration")
    st.text_input("Backup name")


    col1, col2, col3 = st.columns([0.5, 0.5, 0.5])

    with col1:
        if st.button("Save"):
            st.success("Konfigurasi berhasil disimpan.")

    with col2:
        if st.button("Download"):
            st.success("File berhasil diunduh.")

    with col3:
        if st.button("Cancel"):
            st.warning("Input dibatalkan.")
