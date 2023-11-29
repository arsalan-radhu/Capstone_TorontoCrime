import streamlit as st
import joblib
import pandas as pd
import plotly.graph_objects as go
#import os

#def file_selector(folder_path='../'):
#    filenames = os.listdir(folder_path)
#    selected_filename = st.selectbox('Select a file', filenames)
#    return os.path.join(folder_path, selected_filename)

def show():
        
#    filename = file_selector()
#    st.write('You selected `%s`' % filename)
    def load_data(path):

        df = pd.read_csv(path)

        # Streamlit will only recognize 'latitude' or 'lat', 'longitude' or 'lon', as coordinates

        df = df.rename(columns={'LAT_WGS84': 'lat', 'LONG_WGS84': 'lon'}) 
        
        return df
    
    ###########################################################################################################################################
    # Load the XGBoost model
    #model = joblib.load('../Models/xgb_model.joblib')
    model = joblib.load('./Models/xgb_model.joblib') 
     
    ### B. Load first 50K rows
    #df = load_data("./streamlit.csv")
    df = load_data("./Streamlit/streamlit.csv")

    df.drop('Unnamed: 0', axis=1, inplace= True)
    
    #df2 = load_data("./FinalDataFiltered.csv")
    df2 = load_data("./Streamlit/FinalDataFiltered.csv")

    ########################################################################################################################################
    # Function to predict probabilities
    def predict_crime_probability(features):
        # Process the features as needed
        # Example: Convert the input dictionary into a DataFrame
        input_data = pd.DataFrame([features])

        # Predict probabilities using the loaded model
        probabilities = pd.DataFrame(model.predict_proba(input_data), columns=model.classes_)
        
        
        # Mapping of old column names to new column names
        column_mapping = {
            0: 'Assault',
            1: 'Break and Enter',
            2: 'Robbery',
            3: 'Theft'
        }

        # Rename columns according to the mapping
        probabilities.rename(columns=column_mapping, inplace=True)
        return probabilities
    
    ############################################################################################################################################
    # Streamlit app
    st.title('Crime Type Prediction')

    # Input fields for selected features
    selected_neighborhood = st.sidebar.selectbox('Select Neighbourhood', df2['NEIGHBOURHOOD_158'].unique())
    # Assuming df is your DataFrame
    unique_months = df['OCC_MONTH'].unique()
    sorted_months = sorted(unique_months)

    selected_month = st.sidebar.selectbox('Select Month', sorted_months)    

    # Filter divisions based on the selected neighborhood
    filtered_divisions = df2[df2['NEIGHBOURHOOD_158'] == selected_neighborhood]['DIVISION'].unique()
    
    # Display the first division from the filtered divisions
    if len(filtered_divisions) > 0:
        division = {filtered_divisions[0]}
    else:
        division = {filtered_divisions}

    # Dynamic default values for D(Number) features based on the 'division' variable
    default_d22 = 1.0 if division == 'D22' else 0.0
    default_d33 = 1.0 if division == 'D33' else 0.0
    default_d53 = 1.0 if division == 'D53' else 0.0
    default_NSA = 1.0 if division == 'NSA' else 0.0
    default_d32 = 1.0 if division == 'D32' else 0.0
    default_d52 = 1.0 if division == 'D52' else 0.0
    default_d14 = 1.0 if division == 'D14' else 0.0
    default_d11 = 1.0 if division == 'D11' else 0.0
    default_d23 = 1.0 if division == 'D23' else 0.0
    default_d51 = 1.0 if division == 'D51' else 0.0
    default_d13 = 1.0 if division == 'D13' else 0.0
    default_d31 = 1.0 if division == 'D31' else 0.0    
    default_d55 = 1.0 if division == 'D55' else 0.0
    default_d12 = 1.0 if division == 'D12' else 0.0
    default_d41 = 1.0 if division == 'D41' else 0.0
    default_d43 = 1.0 if division == 'D43' else 0.0
    default_d42 = 1.0 if division == 'D42' else 0.0


    # Predict button
    if st.sidebar.button('Predict',):
        # Combine selected features with input values
        feature_inputs = {
        'REPORT_YEAR': 2023, 'REPORT_MONTH': selected_month, 'REPORT_DAY': 1,
        'OCC_YEAR': 2023, 'OCC_MONTH': selected_month, 'OCC_DAY': 1,
        'LONG_WGS84': -79.42, 'LAT_WGS84': 43.70,
        'DEATH': 0, 'INJURIES': 0,
        'D11': default_d11, 'D12': default_d12, 'D13': default_d13, 'D14': default_d14,
        'D22': default_d22, 'D23': default_d23, 'D31': default_d31, 'D32': default_d32,
        'D33': default_d33, 'D41': default_d41, 'D42': default_d42, 'D43': default_d43,
        'D51': default_d51, 'D52': default_d52, 'D53': default_d53, 'D55': default_d55,
        'NSA': default_NSA, 'Apartment': 0, 'Commercial': 0, 'Educational': 0,
        'House': 0, 'NotApplicable': 0, 'Other': 0, 'Outside': 1, 'Transit': 0,
        }

        st.subheader(f"")
        # Predict probabilities
        probabilities = predict_crime_probability(feature_inputs)
        
        # Get the category names and probabilities
        category_names = probabilities.columns.tolist()  # Get column names as category names
        prob_values = probabilities.iloc[0].values  # Extract the values from the first row

        # Divide the layout into a 2x2 grid
        col1, col2 = st.columns(2)

        # Display probabilities in a 2x2 grid of gauge charts
        for i, (category, prob_value) in enumerate(zip(category_names, prob_values * 100)):
            if i < 2:
                col = col1
            else:
                col = col2
            
            with col:
                fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=prob_value,
                    title={'text': f"% Probability of {category}"},
                    number={'suffix': '%'},  # Adding a percentage sign to the number
                    gauge={'axis': {'range': [0, 100]}, 'bar': {'color': '#4a7ba6'}},
                ))
                st.plotly_chart(fig, use_container_width=True)

            

