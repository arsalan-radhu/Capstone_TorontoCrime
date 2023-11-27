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
    df = load_data("./streamlit.csv")
    #df = load_data("./Streamlit/streamlit.csv")
    df.drop('Unnamed: 0', axis=1, inplace= True)


    df2 = load_data("./FinalDataFiltered.csv")
    #df2 = load_data("./Streamlit/FinalDataFiltered.csv")
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


    # Define the division and neighborhood data
    data = {
        'Division': ['D51', 'D14', 'D32', 'D31', 'D52', 'D41', 'D43', 'D55', 'D22', 'D23', 'D42', 'D53', 'D33', 'D11', 'D12', 'D13', 'D54', 'NSA'],
        'Neighborhoods': [
            'South Riverdale, Church-Yonge Corridor, Waterfront Communities-The Island, North St.James Town, Regent Park, Cabbagetown-South St.James Town, Moss Park, St. Lawrence-East Bayfront-The Islands, Downtown Yonge East',
            'South Parkdale, Trinity-Bellwoods, Waterfront Communities-The Island, Kensington-Chinatown, Annex, University, Dovercourt-Wallace Emerson-Junction, Niagara, Palmerston-Little Italy, Dufferin Grove, Little Portugal, Fort York-Liberty Village',
            'York University Heights, Lansing-Westgate, Yorkdale-Glen Park, St.Andrew-Windfields, Westminster-Branson, Clanton Park, Newtonbrook West, Englemount-Lawrence, Bathurst Manor, Oakdale Beverley Heights, Willowdale East, Willowdale West, Bedford Park-Nortown, Bridle Path-Sunnybrook-York Mills, Lawrence Park North, Newtonbrook East',
            'York University Heights, Humber Summit, Humbermede, Glenfield-Jane Heights, Oakdale Beverley Heights, Black Creek, Pelmo Park-Humberlea',
            'Waterfront Communities-The Island, Kensington-Chinatown, University, Bay Street Corridor',
            'Clairlea-Birchmount, Cliffcrest, Ionview, Kennedy Park, Dorset Park, Oakridge, Wexford/Maryvale, Eglinton East, Bendale, Birchcliffe-Cliffside',
            'Scarborough Village, Centennial Scarborough, Cliffcrest, Guildwood, West Hill, Highland Creek, Eglinton East, Bendale, Rouge, Woburn, Morningside',
            'The Beaches, Danforth East York, Danforth, South Riverdale, Taylor-Massey, Flemingdon Park, Broadview North, North Riverdale, Greenwood-Coxwell, Victoria Village, O\'Connor-Parkview, Old East York, Blake-Jones, East End-Danforth, Playter Estates-Danforth, Woodbine-Lumsden, Woodbine Corridor, Leaside-Bennington',
            'Stonegate-Queensway, Islington-City Centre West, Princess-Rosethorn, Etobicoke West Mall, Kingsway South, Humber Heights-Westmount, Edenbridge-Humber Valley, Eringate-Centennial-West Deane, Alderwood, New Toronto, Long Branch, Markland Wood, Mimico (includes Humber Bay Shores)',
            'Thistletown-Beaumond Heights, Humbermede, West Humber-Clairville, Kingsview Village-The Westway, Humber Heights-Westmount, Edenbridge-Humber Valley, Elms-Old Rexdale, Eringate-Centennial-West Deane, Mount Olive-Silverstone-Jamestown, Rexdale-Kipling, Willowridge-Martingrove-Richview',
            'Tam O\'Shanter-Sullivan, Centennial Scarborough, Agincourt North, Agincourt South-Malvern West, L\'Amoreaux, Rouge, Malvern, Steeles, Milliken',
            'Yonge-St.Clair, Thorncliffe Park, Broadview North, Forest Hill North, Casa Loma, Forest Hill South, Annex, Rosedale-Moore Park, Mount Pleasant East, Mount Pleasant West, Bedford Park-Nortown, Bridle Path-Sunnybrook-York Mills, Lawrence Park South, Yonge-Eglinton, Leaside-Bennington',
            'St.Andrew-Windfields, Victoria Village, Bayview Woods-Steeles, Henry Farm, Hillcrest Village, Banbury-Don Mills, Parkwoods-Donalda, Bayview Village, Bridle Path-Sunnybrook-York Mills, Don Valley Village, Pleasant View, Leaside-Bennington',
            'South Parkdale, Junction Area, Runnymede-Bloor West Village, Roncesvalles, Dovercourt-Wallace Emerson-Junction, High Park North, High Park-Swansea, Weston-Pelham Park, Lambton Baby Point, Rockcliffe-Smythe, Dufferin Grove, Little Portugal',
            'Rustic, Junction Area, Keelesdale-Eglinton West, Mount Dennis, Beechborough-Greenbrook, Weston-Pelham Park, Pelmo Park-Humberlea, Rockcliffe-Smythe, Weston'
        ]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Split the neighborhoods into separate rows
    df['Neighborhoods'] = df['Neighborhoods'].apply(lambda x: [neighborhood.strip() for neighborhood in x.split(',')])
    df = df.explode('Neighborhoods')

    # Display the DataFrame
    st.table(df)



    
#########################################################################################################################    
    
    
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