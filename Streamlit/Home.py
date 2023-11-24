# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set page title and favicon
st.set_page_config(page_title="Awesome Streamlit Page", page_icon=":rocket:")

# Add a catchy title
st.title("Toronto Crime Type Predictor")
st.set_option('deprecation.showPyplotGlobalUse', False)
# Introduction
st.markdown("""
Explore the exciting features and visualizations below. Dive into the data-driven world with Streamlit!
""")

# Sidebar for customization
page = st.sidebar.selectbox("Select Page", ["Home", "EDA", "Models"])

# Conditional rendering based on the selected page
if page == "Home":
    st.sidebar.header("Customize Your Experience")
    user_name = st.sidebar.text_input("Enter Your Name:", "Streamlit Enthusiast")
    st.sidebar.info(f"Hello, {user_name}! 👋")
    st.write("Welcome to the Crime Analysis App. Use the sidebar to navigate.")
elif page == "EDA":
    st.sidebar.header("Exploratory Data Analysis (EDA)")
    # Add EDA content here
    st.write("This is the EDA page. Add your EDA content.")
elif page == "Models":
    st.sidebar.header("Models")
    # Add Models content here
    st.write("This is the Models page. Add your models or analysis content.")


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
df = load_data("./streamlit.csv")
df.drop('Unnamed: 0', axis=1, inplace= True)


df2 = load_data("../Data/FinalData.csv")
#df2.drop('Unnamed: 0', axis=1, inplace= True)
### C. Display the dataframe in the app
st.dataframe(df)


#######################################################################################################################################
### STATION MAP

st.subheader('Location Map - Crimes')      
map_df = df[(df['REPORT_MONTH'] == 12) & (df['D22'] == 1)]
st.map(map_df, size=30, color='#DF8877') 
#########################################################################################
# Create a Streamlit app
st.title('Crime Analysis App')

# Select a crime type
crime_type = st.selectbox('Select Crime Type', df2['CRIME_TYPE'].unique())

# Filter the DataFrame based on the selected crime_type
filtered_division_counts = df2['DIVISION'][df2['CRIME_TYPE'] == crime_type].value_counts()

# Create a bar plot using Seaborn
fig, ax = plt.subplots(figsize=(20, 9))
# Set the background color
ax.set_facecolor('#080719') 
sns.barplot(x=filtered_division_counts.index, y=filtered_division_counts, color='skyblue', ax=ax)
plt.title(f'Occurrence of Divisions in {crime_type}')
plt.xlabel('Division')
plt.ylabel('Count')
plt.xticks(rotation=45)

# Display the Seaborn plot in Streamlit
st.pyplot(fig)

#####################################################################################################
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
