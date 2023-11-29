import pandas as pd
import streamlit as st

def data_field_descriptions():
    data = {
        #'Field': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        'Field Name': ['EVENT_UNIQUE_ID', 'REPORT_DATE', 'OCC_DATE', 'REPORT_YEAR', 'REPORT_MONTH', 'REPORT_DAY', 'REPORT_DOY', 'REPORT_DOW', 'REPORT_HOUR', 'OCC_YEAR', 'OCC_MONTH', 'OCC_DAY', 'OCC_DOY', 'OCC_DOW', 'OCC_HOUR', 'DIVISION', 'LOCATION_TYPE', 'PREMISES_TYPE', 'UCR_CODE', 'UCR_EXT', 'OFFENCE', 'MCI_CATEGORY', 'HOOD_158', 'NEIGHBORHOOD_158', 'HOOD_140', 'NEIGHBORHOOD_140', 'LONG_WGS84', 'LAT_WGS84'],
        'Description': ['Offence Number', 'Date Offence was reported', 'Date Offence occurred', 'Year Offence was reported', 'Month Offence was reported', 'Day of the month Offence was reported', 'Day of the Year Offence was reported', 'Day of the Week Offence was reported', 'Hour Offence was reported', 'Year Offence Occurred', 'Month Offence Occurred', 'Day of the month Offence occurred', 'Day of the Year Offence occurred', 'Day of the Week Offence occurred', 'Hour Offence occurred', 'Police Division where Offence occurred', 'Location type of Offence', 'Premises Type of Offence', 'UCR Code for Offence', 'UCR Extension for Offence', 'Title of Offence', 'MCI Category of Occurrence', 'Identifier of Neighborhood using City of Toronto\'s new 158 neighborhood structure', 'Name of Neighborhood using City of Toronto\'s new 158 neighborhood structure', 'Identifier of Neighborhood using City of Toronto\'s old 140 neighborhood structure', 'Name of Neighborhood using City of Toronto\'s old 140 neighborhood structure', 'Longitude Coordinates (Offset to nearest intersection)', 'Latitude Coordinates (Offset to nearest intersection)']
    }

    df = pd.DataFrame(data)

    return df
def show():
    st.title("Predicting Crime Rates Based on Neighborhoods in Toronto")
    st.markdown('<div style="padding-top:100.000%;position:relative;"><iframe src="https://gifer.com/embed/7h9e" width="100%" height="100%" style="position:absolute;top:0;left:0;" frameBorder="0" allowFullScreen></iframe></div><p><a href="https://gifer.com">via GIFER</a></p>', unsafe_allow_html=True)
    st.header("Problem Area")
    st.markdown("Crime is a critical concern for any city, and Toronto is no exception. Understanding crime trends, patterns, and their distribution across neighbourhoods is crucial for policymakers, law enforcement, and the general public.")

    st.header("Those Affected")
    st.markdown("The impact of crime extends to everyone in a community. The insights generated from this project will be beneficial for everyone in the community.")

    st.header("Proposed Data Science Solution")
    st.markdown("Our approach to solving this problem is based on data science techniques. We will perform data analysis, visualization, and predictive modelling to gain insights into identifying neighborhoods with the highest and lowest crime rates, analyzing temporal trends, predicting future crime rates, and evaluating the effectiveness of law enforcement initiatives.")

    st.header("Impact of the Solution")
    st.markdown("The impact of this solution includes improved safety, informed decision-making, and an aware communities.")

    st.header("Dataset")
    st.markdown("For this project, we utilized the 'Toronto Crime Data' dataset, which comprises crime reports collected between 2014 2022, categorized by crime type, location, and date.")
    st.markdown("Below is a table with descriptions of the data fields used in the Toronto Crime Analysis project.")

    field_descriptions = data_field_descriptions()
    
    st.table(field_descriptions)

    st.header("Work Flow")
    st.markdown(
        """
        - The data was sourced from the Toronto Police Services's Open Data Portal and was collected from 2014 to 2022. 
        - The files were split-up based on crime type. I had to join all of these tables for analysis.
        - I used Tableau for Exploratory Data Analysis (EDA). I gained insights on crime trends based on time of day, year, neighborhood, and location. 
        - Python was used to understand the relationship between crime type and police division (neighborhood).
        - After preprocessing the data, I trained a basic logistic regression model to predict the type of crime likely to happen based on location and time. 
        - My model achieved a 50% accuracy on test data. The low accuracy rate meant other models and optimization techniques were needed.
        - Ultimately, the xGBoost algorithm, after extensive training, testing, and optimization, emerged as the most effective. It delivered a final accuracy of 65%.
        - To enhance interpretability of the model, various performance metrics were needed like: generating a classification report, constructing a confusion matrix, revealing feature importance, and utilizing permutation importance. All of these metrics help us understand what columns have the most influence on the outcome and predictive accuracy.
        """
    )

    st.header("Contributors")
    st.markdown("Arsalan Arif Radhu")

    st.header("Get Involved")
    st.markdown("Feel free to contribute, open issues, or make suggestions to improve the analysis and its impact.")
    st.markdown("We can always work together to further improve the project!")
