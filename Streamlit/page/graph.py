import streamlit as st
import pandas as pd
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
    #df = load_data("./streamlit.csv")
    df = load_data("./Streamlit/streamlit.csv")
    df.drop('Unnamed: 0', axis=1, inplace= True)


    #df2 = load_data("./FinalDataFiltered.csv")
    df2 = load_data("./Streamlit/FinalDataFiltered.csv")
    ### C. Display the dataframe in the app

    st.markdown("### Final Data Set")
    st.dataframe(df,height=420)


    ################################################################### STATION MAP ######################################################################### 

    # Checkbox for each option in the sidebar
    map_view = st.sidebar.checkbox("Map View")
    crime_analysis = st.sidebar.checkbox("Crime Analysis")
    crime_over_months = st.sidebar.checkbox("Crime Distribution over the Months")

    if map_view:
        # Set the initial focus to Toronto (latitude, longitude)
        st.markdown("### Crime in Toronto")

        neighbourhood = st.selectbox('Select Neighbourhood', df2['NEIGHBOURHOOD_158'].unique())
        month = st.selectbox('Select Month', df2['REPORT_MONTH'].unique())
        crime_type = st.selectbox('Select Crime Type', df2['CRIME_TYPE'].unique())
        toronto_center = [43.70, -79.42]

        # Filter the DataFrame based on the selected crime_type
        map_df = df2[(df2['REPORT_MONTH'] == month) & (df2['NEIGHBOURHOOD_158'] == neighbourhood) & (df2['CRIME_TYPE'] == crime_type)]

        # Use PyDeck to create a map centered on Toronto
        deck = pdk.Deck(
        map_style='mapbox://styles/mapbox/streets-v12',
        initial_view_state=pdk.ViewState(
            latitude=toronto_center[0],
            longitude=toronto_center[1],
            zoom=10.5,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ColumnLayer',
                data=map_df,
                get_position='[lon, lat]',
                get_elevation='height',
                elevation_scale=50,
                get_fill_color='[200, 30, 0, 160]',
                pickable=True,
                auto_highlight=True,
                ),
            ],
        )

        st.pydeck_chart(deck)

#############################################################################################################################################################################



    
#########################################################################################################################    
    
    if crime_analysis:
        st.markdown("### Amount of Crimes by Neighbourhoods")
        
        # Select a neighborhood
        selected_neighborhood = st.selectbox('Select Neighborhood', df2['NEIGHBOURHOOD_158'].unique(), key=2) 

        # Filter the DataFrame based on the selected crime_type and neighborhood
        filtered_crime_counts = df2[df2['NEIGHBOURHOOD_158'] == selected_neighborhood]['CRIME_TYPE'].value_counts()

        # Create a bar plot using Plotly Express
        fig = px.bar(
            x=filtered_crime_counts.index,
            y=filtered_crime_counts,
            color=filtered_crime_counts.index,
            labels={'x': 'Crime Type', 'y': 'Count'},
            title=f'Occurrence of Crime Types in {selected_neighborhood}',
            template='plotly_dark'
        )

        # Change the bar color to #4a7ba6
        fig.update_traces(marker_color='#4a7ba6')

        # Rotate x-axis labels for better readability
        fig.update_layout(xaxis=dict(tickangle=45))

        # Display the Plotly Express plot in Streamlit
        st.plotly_chart(fig)

#######################################################################################################################################
    if crime_over_months:
        st.markdown("### Distribution of Occurrences of Crimes over the Months")
        # Get unique crime types for checkboxes
        crime_types = df2['CRIME_TYPE'].unique()

        # Divide the page into three columns
        col1, col2, col3 = st.columns(3)

        # Create checkboxes in-line
        selected_crimes = []
        for i, crime_type in enumerate(crime_types):
            if i % 3 == 0:
                checkbox_container = col1
            elif i % 3 == 1:
                checkbox_container = col2
            else:
                checkbox_container = col3
            
            if checkbox_container.checkbox(crime_type):
                selected_crimes.append(crime_type)

        # Filter the DataFrame based on selected crime types
        filtered_df = df2[df2['CRIME_TYPE'].isin(selected_crimes)]

        # Group by 'OCC_MONTH' and 'CRIME_TYPE', count occurrences for each crime type
        grouped = filtered_df.groupby(['OCC_MONTH', 'CRIME_TYPE'])['EVENT_UNIQUE_ID'].count().reset_index(name='Count')

        # Create a line graph using Plotly Express with multiple lines for each selected crime type
        line_chart = px.line(grouped, x='OCC_MONTH', y='Count', color='CRIME_TYPE',
                            labels={'OCC_MONTH': 'Month', 'Count': 'Count of Occurrences of Crimes'},
                            title=f'Count of Occurrences of Selected Crimes by Month')
        # Display the line graph
        st.plotly_chart(line_chart)