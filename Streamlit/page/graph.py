import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import pydeck as pdk

#import os

#def file_selector(folder_path='./Streamlit'):
#    filenames = os.listdir(folder_path)
#    selected_filename = st.selectbox('Select a file', filenames)
#    return os.path.join(folder_path, selected_filename)



def show():

    #filename = file_selector()
    #st.write('You selected `%s`' % filename)

    # Add a catchy title
    st.title("Getting to know the Data")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    ############################################################## DATA LOADING ############################################################################ 

    ### A. define function to load data
    @st.cache_data # <- add decorators after tried running the load multiple times
    def load_data(path):

        df = pd.read_csv(path)

        # Streamlit will only recognize 'latitude' or 'lat', 'longitude' or 'lon', as coordinates

        df = df.rename(columns={'LAT_WGS84': 'lat', 'LONG_WGS84': 'lon'}) 
        
        return df

    ### B. Load first 50K rows
    df = load_data("./Streamlit/streamlit.csv")
    df.drop('Unnamed: 0', axis=1, inplace= True)


    df2 = load_data("./Streamlit/FinalDataFiltered.csv")
    #df2.drop('Unnamed: 0', axis=1, inplace= True)
    ### C. Display the dataframe in the app

    st.markdown("### Final Data Set")
    st.dataframe(df)


    ################################################################### STATION MAP ######################################################################### 

    # Set the initial focus to Toronto (latitude, longitude)
    st.markdown("### Crime in Toronto")

    neighbourhood = st.selectbox('Select Neighbourhood', df2['NEIGHBOURHOOD_158'].unique())
    month = st.selectbox('Select Month', df2['REPORT_MONTH'].unique())
    crime_type = st.selectbox('Select Crime Type', df2['CRIME_TYPE'].unique())
    toronto_center = [43.70, -79.42]

    # Filter the DataFrame based on the selected crime_type
    map_df = df2[(df2['REPORT_MONTH'] == month) & (df2['NEIGHBOURHOOD_158'] == neighbourhood) & (df2['CRIME_TYPE'] == crime_type)]

    # Use PyDeck to create a map centered on Toronto
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/streets-v12',
        initial_view_state=pdk.ViewState(
            latitude=toronto_center[0],
            longitude=toronto_center[1],
            zoom=10.5,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=map_df,
                get_position='[lon, lat]',
                get_radius=50,
                get_color='[200, 30, 0, 160]',
                pickable=True,
                
            ),
        ],
    ))

#############################################################################################################################################################################
    st.markdown("### Amount of Crimes by Division")
    # Select a crime type
    crime_type = st.selectbox('Select Crime Type', df2['CRIME_TYPE'].unique(),key=1)

    # Filter the DataFrame based on the selected crime_type
    filtered_division_counts = df2['DIVISION'][df2['CRIME_TYPE'] == crime_type].value_counts()

    

    # Create a bar plot using Plotly Express
    fig = px.bar(x=filtered_division_counts.index, y=filtered_division_counts, color=filtered_division_counts.index,
             labels={'x': 'Division', 'y': 'Count'},
             title=f'Occurrence of {crime_type} in Divisions',
             template='plotly_dark')

    # Rotate x-axis labels for better readability
    fig.update_layout(xaxis=dict(tickangle=45))

    # Display the Plotly Express plot in Streamlit
    st.plotly_chart(fig)