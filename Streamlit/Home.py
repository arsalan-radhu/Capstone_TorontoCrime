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

# Load sample data
@st.cache
def load_data():
    data = pd.DataFrame(np.random.randn(100, 3), columns=['A', 'B', 'C'])
    return data

df = load_data()

# Show a random sample of the data
st.subheader("Random Sample of Data")
st.dataframe(df.sample(5))

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
