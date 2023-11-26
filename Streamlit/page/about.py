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
    st.title("Toronto Crime Type Analysis")
    st.markdown("This Streamlit app provides insights into crime types in different neighborhoods in Toronto.")
    st.markdown('<div style="padding-top:100.000%;position:relative;"><iframe src="https://gifer.com/embed/7h9e" width="100%" height="100%" style="position:absolute;top:0;left:0;" frameBorder="0" allowFullScreen></iframe></div><p><a href="https://gifer.com">via GIFER</a></p>', unsafe_allow_html=True)
    st.header("Problem Area")
    st.markdown("Crime is a critical concern for any city, and Toronto is no exception. Understanding crime trends, patterns, and their distribution across neighborhoods is crucial for policymakers, law enforcement, and the general public.")

    st.header("Those Affected")
    st.markdown("The impact of crime extends to everyone in a community. The insights generated from this project will be beneficial for various stakeholders.")

    st.header("Proposed Data Science Solution")
    st.markdown("Our approach to solving this problem is based on data science techniques. We will perform data analysis, visualization, and predictive modeling to gain insights into identifying neighborhoods with the highest and lowest crime rates, analyzing temporal trends, predicting future crime rates, and evaluating the effectiveness of law enforcement initiatives.")

    st.header("Impact of the Solution")
    st.markdown("The impact of this solution includes improved safety, informed decision-making, and aware communities.")

    st.header("Dataset")
    st.markdown("For this project, we utilized the 'Toronto Crime Data' dataset, which comprises crime reports collected over several years, categorized by crime type, location, and date.")
    st.markdown("Below is a table with descriptions of the data fields used in the Toronto Crime Analysis project.")

    field_descriptions = data_field_descriptions()
    
    st.table(field_descriptions)

    st.header("Work Flow")
    st.markdown("I collected and cleaned the data from the Toronto Police's Open Data source, breaking it into nine files, concatenating them, and performing cleaning processes. Utilizing Tableau for basic exploratory data analysis (EDA), I gained insights into crime trends concerning the time of day, year, neighborhood, and location type. Further, in-depth Python analysis delved into the relationship between crime and Police division. After preprocessing involved one-hot encoding, dropping non-usable columns, and embedding the target variable, 'CRIME_TYPE,' I trained a basic Logistic Regression model. Despite achieving an 85% accuracy on the test data after 6500 iterations, I explored techniques like PCA and Scaling. Ultimately, the XGBoost algorithm, after extensive training, testing, and optimization, emerged as the most effective, delivering a final accuracy of 65%. To enhance the model's interpretability, I conducted a comprehensive analysis, including generating a classification report, revealing feature importance, constructing a confusion matrix, and utilizing permutation importance to understand the impact of individual features on predictive accuracy. These steps provided valuable insights into the strengths and limitations of the XGBoost model for crime prediction.")


    st.header("Installation and Usage")
    st.markdown("## To use this project, follow these steps:")
    st.markdown("1. **Clone the repository:**")
    st.code("git clone https://github.com/arsalan-radhu/Capstone_TorontoCrime.git", language="bash")

    st.markdown("2. **Set up the Python environment with the required packages.**")
    st.code("pip install -r Docs/requirements.txt", language="bash")

    st.markdown("3. **Download the cleaned and formated dataset from the link provided [here](https://drive.google.com/file/d/150CoI-976T7_jVDGR9KmNvVGDsOM4ZcV/view?usp=sharing).**")

    st.markdown("4. **Run the Jupyter Notebooks in the 'Notebooks' directory.**")

    st.header("Contributors")
    st.markdown("Arsalan Arif Radhu")

    st.header("Get Involved")
    st.markdown("Feel free to contribute, open issues, or make suggestions to improve the analysis and its impact.")
    st.markdown("Together, we can make Toronto safer and more secure for everyone.")