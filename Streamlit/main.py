import streamlit as st
from page import graph, about, contact, model

def main():
    # Set page title and favicon
    st.set_page_config(page_title="Toronto Crime Type Predictor", page_icon="👮‍♂️")
    # Remove Streamlit default menu
    hide_streamlit_style = """
            <style>
                #MainMenu {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    pages = {
        "About": about.show,
        "EDA": graph.show,
        "Predictor": model.show,
        "Contact": contact.show,
        
    }

    # Create a sidebar for navigation
    #page = st.sidebar.selectbox("Select a page", list(pages.keys()))
    # Create a sidebar for navigation
    page_options = list(pages.keys())
    page = st.sidebar.selectbox("Select a page", page_options)

    # Display the selected page
    pages[page]()

if __name__ == "__main__":
    main()