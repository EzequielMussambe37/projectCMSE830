import streamlit as st
from utilities import read_data 

import pandas as pd


def app():
    
    data = read_data.read_file("csv",",", "./utilities/chances.csv")
    #column5, column6 = st.columns([.7,.3])
    ######################################################
    st.markdown('*Data Science Project CMSE 830*')
    st.markdown('''
    **Ezequiel Mussambe**

    *Graduate Student at Michigan State University, https://portfolio-em.streamlit.app*

    ''')
    st.title('Graduate Admission Prediction')
    st.image("https://images.unsplash.com/photo-1590012314607-cda9d9b699ae?auto=format&fit=crop&q=80&w=1171&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
             caption=f'blue and white academic hat (Joshua Hoehne)')
    

    
    
    st.subheader('Introduction')
    
    st.markdown("""
                For many undergraduate students, the decision to pursue postgraduate studies is fraught with uncertainties. 
                The dilemma often pivots around continuing education immediately after their undergraduate degree or taking a break from academia.
                With the decision to persue a high education araise the question "Is my academic portfolio competitive for admission to a reputable universities or highly ranked institutions.
                """
                )
    

    st.subheader('Objective')
    st.markdown("""
                Objectives
    The fundamental objective of this project is to develop a predictive model for graduate admission based on quantitative factors, measure the influence of different components of an applicant's portfolio on admission, 
    and discuss the limitations and challenges associated with using predictive models for this purpose.
                """)



    st.subheader("First Phase")
    st.markdown("""
                The first phase of the project is based on initial exploratory data analysis (EDA), including plotting pair plots to visualize the relationships between attributes, to understand the data distribution and correlations, and to identify any outlier  that could affect the project's overall objectives.
                The web application is user-friendly, it allows users to interact with various features of the dataset and visualize the major attributes that  affect admission chances.
                **<span style='color:blue'>Below is the Overview of the Data.</span>**
                """,unsafe_allow_html=True)
    st.subheader("Column name and data types")
    st.markdown("""
                
        1.	Serial no (or Id)

        2.	GRE Scores (out of 340)

        3.	TOEFL Scores (out of 120)

        4.	University Rating (out of 5)

        5.	Statement of Purpose and Letter of Recommendation Strength (out of 5)

        6.	Letter of Recommendation

        7.	Undergraduate GPA (out of 10)

        8.	Research Experience (either 0 or 1)

        9.	Chance of Admit (ranging from 0 to 1)
                """)
    
    df = pd.DataFrame(data.dtypes)
    st.dataframe(df)

    st.caption('**Table 1.** DataFrame.')
    st.dataframe(data)
    
    st.markdown("""___""")
    st.markdown("<h4 style='text-align:center;'>Statistics Summary</h4>",unsafe_allow_html=True)
    #st.header("",divider="green")
    
    column1,column2 = st.columns(2)
    with column1:
        st.markdown("""<ul>
            <li>Number of Recors: 400 ✅</li>
            <li>Number of Attributes: 9 ✅</li>
        </ul>""",
        unsafe_allow_html=True)
        
    with column2:
        st.markdown("""<ul>
            <li>There is no missing value ✅</li>
            <li>The dataset has been preproccessed ✅</li>
        </ul>""",
        unsafe_allow_html=True)  
    st.caption('**Table 2.** Summary of the Data.')
    st.dataframe(data.describe())
    
    st.markdown("""___""")
    st.markdown("<h4 style='text-align:center;'>Correlation</h4>",unsafe_allow_html=True)

    st.write("Dataset  overall correlation")
    st.caption('**Table 3.** Correlation between attributes.')
    st.dataframe(data.corr())
    #AgGrid(data.corr(),fit_columns_on_grid_load=True,height=min(MIN_HEIGHT + len(data) * ROW_HEIGHT, MAX_HEIGHT))
    st.markdown("""___""")
    
    st.subheader("Acknowledgements")
    st.markdown("""
                <p style='background-color:rgb(255, 202, 0,0.3);'> "This dataset is inspired by the UCLA Graduate Dataset. The test scores and GPA are in the older format. 
                The dataset is owned by Mohan S Acharya" (Acharya, M.S.).
                Also, I would like to mention <a href='https://github.com/aditya-sureshkumar/University-Recommendation-System'>Aditya Sureshkumar</a> who made the data available by scrapping it from Edulix.com.
                </p>
                """,unsafe_allow_html=True)
    
    st.markdown('*Please Go to EDA for Data Visualization*')