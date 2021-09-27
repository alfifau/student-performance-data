import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib as plt
from matplotlib.figure import Figure

def main():
    df = pd.read_csv('StudentsPerformance.csv')
    gender = df['gender'].unique()
    ethnic = df['race/ethnicity'].unique()
    parent_edu = df['parental level of education'].unique()
    lunch = df['lunch'].unique()
    course = df['test preparation course'].unique()

    st.sidebar.title('**Select Criteria**')
    gender_select = st.sidebar.multiselect('Gender', gender)
    ethnic_select = st.sidebar.multiselect('Race/Ethnicity', ethnic)
    parent_edu_select = st.sidebar.multiselect('Parental Education', parent_edu)
    lunch_select = st.sidebar.multiselect('Lunch', lunch)
    course_select = st.sidebar.multiselect('Test Preparation Course', course)

    data = df[df['gender'].isin(gender_select if gender_select else gender) &
            df['race/ethnicity'].isin(ethnic_select if ethnic_select else ethnic) &
            df['parental level of education'].isin(parent_edu_select if parent_edu_select else parent_edu) &
            df['lunch'].isin(lunch_select if lunch_select else lunch) &
            df['test preparation course'].isin(course_select if course_select else course)]

    if gender_select or ethnic_select or parent_edu_select or lunch_select or course_select:
        st.subheader('Data by Selected Criteria')
        st.dataframe(data)
        
        sns.set_theme(style="white", palette="pastel")
        st.subheader('Math Score Distribution')
        fig = Figure()
        ax_math = fig.subplots()
        sns.histplot(pd.to_numeric(data['math score']), ax=ax_math, bins=5, color="green")
        ax_math.set_xlabel('Math Score')
        ax_math.set_ylabel('Number of Students')
        st.pyplot(fig)

        st.subheader('Reading Score Distribution')
        fig = Figure()
        ax_read = fig.subplots()
        sns.histplot(pd.to_numeric(data['reading score']), ax=ax_read, bins=5, color="blue")
        ax_read.set_xlabel('Reading Score')
        ax_read.set_ylabel('Number of Students')
        st.pyplot(fig)

        st.subheader('Writing Score Distribution')
        fig = Figure()
        ax_write = fig.subplots()
        sns.histplot(pd.to_numeric(data['writing score']), ax=ax_write, bins=5, color="orange")
        ax_write.set_xlabel('Writing Score')
        ax_write.set_ylabel('Number of Students')
        st.pyplot(fig)
    else:
        st.title('Student Performance Data Visualization')
        st.write("I used dataset from Kaggle, check out [here](https://www.kaggle.com/spscientist/students-performance-in-exams)!")

if __name__ == '__main__':
    main()