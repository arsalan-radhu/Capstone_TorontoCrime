# Toronto Crime Rate Analysis

# Table of contents  
1. [Overview](#overview)  
2. [Problem Area](#problem-area)
3. [Those Affected](#those-affected)  
4. [Impact of the Solution](#impact-of-the-solution)
5. [Dataset](#dataset)
6. [Work Flow](#work-flow)
7. [Project Structure](#project-structure)
8. [Installation and Usage](#installation-and-usage)

## Overview
This GitHub repository hosts the code and documentation for a data science capstone project focused on analyzing the crime rates in different neighborhoods in Toronto over the years. This project is an extension of the initial "Areas of Interest Submission" and aims to provide a comprehensive understanding of the crime problem in Toronto, its impact on various communities, and a proposed data science solution.

## Problem Area
Crime is a critical concern for any city, and Toronto is no exception. Understanding crime trends, patterns, and their distribution across neighborhoods is crucial for policymakers, law enforcement, and the general public. This project's primary focus is to analyze and visualize crime data to identify areas with high crime rates and assess their changes over time. We aim to provide actionable insights to address this problem effectively.

## Those Affected
The impact of crime extends to everyone in a community. The insights generated from this project will be beneficial for various stakeholders:

<b>Policymakers</b>: To allocate resources, improve law enforcement, and implement community programs effectively.</br>
<b>Law Enforcement</b>: To strategically deploy resources and personnel to areas with high crime rates.</br>
<b>Residents</b>: To be aware of crime trends in their neighborhoods and take precautionary measures.</br>
<b>Businesses</b>: To make informed decisions about where to establish or expand their operations.</br>

<b><i>Proposed Data Science Solution</i></b></br>
Our approach to solving this problem is based on data science techniques. We will perform data analysis, visualization, and predictive modeling to gain insights into the following:
<ul>
    <li>Identifying neighborhoods with the highest and lowest crime rates.</li>
    <li>Analyzing temporal trends in crime data over the years.</li>
    <li>Predicting future crime rates in different areas.</li>
    <li>Evaluating the effectiveness of various law enforcement initiatives.</li>
    <li>This information will be used to suggest evidence-based strategies for reducing crime in high-risk areas.</li>
</ul>

## Impact of the Solution
The impact of this solution can be summarized as follows:

<b>Improved Safety</b>: By identifying high-crime areas, law enforcement can focus their efforts and resources more effectively, leading to reduced crime rates.</br>
<b>Informed Decision-Making</b>: Policymakers and community leaders can make data-driven decisions to implement preventive measures and allocate resources efficiently.</br>
<b>Aware Communities</b>: Residents and businesses in Toronto will have a better understanding of the crime landscape in their areas and can take proactive measures to enhance their safety.</br>

## Dataset
For this project, we will utilize the "Toronto Crime Data" dataset, which comprises crime reports collected over several years, categorized by crime type, location, and date. The dataset is publicly available and can be accessed through https://data.torontopolice.on.ca/pages/asr-open-data. Each crime was a different data sets which have been combined into one data set. It contains the following key attributes:
![App Screenshot](./References/Screenshot%202023-10-11%20153422.png) <br />
The working data set can be downloaded using the following link: <a href= "https://drive.google.com/file/d/1srE3AW51bbNYv88LudycGaU2dUwTHNKB/view?usp=sharing" target="_blank"> Preprossed Data</a>

## Work Flow
#### Done:
<ul>
    <li>
        The data has been collected, cleaned and advanced exploratory analysis has been done.
    </li>
    <li>
        The data was collected from Toronto Police's Opoen Data source. The data was collected divided into 9 files. Each file was concatenated and then cleaned.
    </li>
    <li>
        After cleaning some basic EDA was done using Tableau and some insights were gained like the general trend of crimes and their relationship with time of day, year, neighbourhood and location type.
    </li>
    <li>
        Some more in depth Analysis was done using python and the relationship between crime and Police division was explored. The data was then pre-processed using one-hot encoding and dropping non-usable columns.         The data was divided into test and train sets and `CRIME_TYPE` chosen as the target variable after being embedded.
    </li>
    <li>
        After the pre-processing, a basic Logistic Regression model was trained and tested on the data which after 6500 iterations gave us a score of 85% on test data.
    </li>
    <li>
        To raise the accuracy and reduce runtime, PCA and Scaling was performed but it dropped the accuracy to 65%.
    </li>
</ul>

#### To-do: 
<ul>
    <li>
        The next steps would be to increase the accuracy of our predictions.
    </li>
    <li>
        Create and fit KNN Model to see if it fits better to my data set.
    </li>
    <li>
        Researh more about what other models might fit my data set.
    </li>
</ul>

## Project Structure
<b>Data</b>: Contains the dataset used for analysis (or a link to the source).</br>
<b>Notebooks</b>: Jupyter notebooks documenting the data analysis and modeling process.</br>
<b>Reports</b>: Project reports, findings, and visualizations.</br>
<b>References</b>: Additional project documentation and resources.</br>
<b>Models</b>: All the models made.</br>
<b>Docs</b>: Additional documents required for the project.</br>

## Installation and Usage
To use this project, follow these steps:
<ul>
<li>

Clone the repository: 
~~~bash  
  git clone https://github.com/arsalan-radhu/Capstone_TorontoCrime.git 
~~~

</li>
<li>Set up the Python environment with the required packages. You can find the list in the requirements.txt file in the Docs directory.</li>
<li>Download the dataset from the link provided <a href= "https://drive.google.com/file/d/1srE3AW51bbNYv88LudycGaU2dUwTHNKB/view?usp=sharing" target="_blank">here</a>.</li>
<li>Run the Jupyter notebooks "Notebooks" directory.</li>
</ul>

## Contributors
Arsalan Arif Radhu

<b>
Feel free to contribute, open issues, or make suggestions to improve the analysis and its impact. Together, we can make Toronto safer and more secure for everyone.
</b>
