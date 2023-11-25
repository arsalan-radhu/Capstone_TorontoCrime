# contact.py
import streamlit as st

def show():
    # Add a catchy title
    st.title("Contact Page")
    st.write("This is the contact page.")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Introduction
    st.markdown("""
    Explore the exciting features and visualizations below. Dive into the data-driven world with Streamlit!
    """)