# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set page title and favicon
st.set_page_config(page_title="Awesome Streamlit Page", page_icon=":rocket:")

# Add a catchy title
st.title("Welcome to My Cool Streamlit Page!")
st.set_option('deprecation.showPyplotGlobalUse', False)
# Introduction
st.markdown("""
Explore the exciting features and visualizations below. Dive into the data-driven world with Streamlit!
""")

# Sidebar for customization
st.sidebar.header("Customize Your Experience")
user_name = st.sidebar.text_input("Enter Your Name:", "Streamlit Enthusiast")
st.sidebar.info(f"Hello, {user_name}! 👋")

#######################################################################################################################################
### DATA LOADING

### A. define function to load data
@st.cache_data # <- add decorators after tried running the load multiple times
def load_data(path):

    df = pd.read_csv(path)

    # Streamlit will only recognize 'latitude' or 'lat', 'longitude' or 'lon', as coordinates

    df = df.rename(columns={'LAT_WGS84': 'lat', 'LONG_WGS84': 'lon'}) 
     
    return df

### B. Load first 50K rows
df = load_data("streamlit.csv")

### C. Display the dataframe in the app
st.dataframe(df)


#######################################################################################################################################
### STATION MAP

st.subheader('Location Map - NYC bike stations')      

st.map(df) 

# Create a simple plot
st.subheader("Interactive Plot")
selected_column = st.selectbox("Select a Column for Plotting", df.columns)
plt.figure(figsize=(8, 6))
sns.histplot(df[selected_column], kde=True)
st.pyplot()

# Display a cool map
st.subheader("Interactive Map")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

# Add a fun section
st.header("🚀 Blast Off!")
st.markdown("""
Thanks for exploring my Streamlit page! Feel free to connect with me on [LinkedIn](Your LinkedIn Link) and share your thoughts.

Happy Streamlit-ing! ✨
""")

# Add a footer
st.markdown("""
---
*Created with ❤️ by [Your Name]*  
*Check out the [source code on GitHub](Your GitHub Link)*
""")
