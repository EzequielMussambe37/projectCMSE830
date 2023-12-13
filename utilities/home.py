import streamlit as st
from utilities import read_data, upload

import pandas as pd


def app():
    
    st.markdown(""" <h2 style="text-align:center;">Graduate Admission Prediction Using Linear Regression Model</h2>  <p style="text-align:center;">Author: Ezequiel Mussambe</p>""",unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1590012314607-cda9d9b699ae?auto=format&fit=crop&q=80&w=1171&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
             caption=f'blue and white academic hat (Joshua Hoehne)')
    st.subheader('Introduction')
    st.markdown("""
                For many undergraduate international students, the decision to pursue postgraduate studies is fraught with uncertainties. 
                The dilemma often pivots around continuing education immediately after their undergraduate degree or taking a break from academia.
                With the decision to persue a high education araise the question "Is my academic portfolio competitive for admission to a reputable universities or highly ranked institutions around the world.
                """
                )
    st.subheader('Objective')
    st.markdown("""
   The analysis begins with the hypothesis that chance of admission is significantly influenced by test 
   scores—specifically GRE, TOEFL, and CGPA. The primary aim is to present international graduate students 
   with an optimal default result achieved through the linear regression model. 
   Despite this default outcome, the application maintains flexibility to ensure an excellent user experience.
   """)
    st.markdown("""
                ✍🏻 <p style='background-color:rgb(255, 202, 0,0.3);'> It is crucial to acknowledge and address the inherent limitations and challenges 
    associated with employing predictive models for this purpose.
                </p>
                """,unsafe_allow_html=True)
    
    data = read_data.read_file("csv",",", "./utilities/admission.csv")
    st.session_state.data_file = data
    if "data_file" not in st.session_state:
        st.session_state["data_file"]= data
    tab1, tab2, tab3,tab4 = st.tabs(["DATA 📝", "COLUMN INFO ℹ️", "STATISTIC SUMMARY 🔢","CORRELATION MATRIX 📈"])

    with tab1:
        st.write(data)

    with tab2:
        st.markdown("""
        1.	Serial no (or Id)

        2.	GRE Scores (out of 340)

        3.	TOEFL Scores (out of 120)

        4.	University Rating (out of 5)

        5.	Statement of Purpose and Letter of Recommendation Strength (out of 5)

        6.	Letter of Recommendation (out of 5)

        7.	Undergraduate GPA (out of 9.92)

        8.	Research Experience (either 0 or 1)

        9.	Chance of Admit (ranging from 0 to 0.97)
                """)
        df = pd.DataFrame(data.dtypes)
        st.dataframe(df.T)
    with tab3:
        st.dataframe(data.describe())
        column1,column2 = st.columns(2)
        with column1:
            st.markdown(f"""<ul>
                <li>Number of Recors: {data.shape[0]} ✅</li>
                <li>Number of Attributes: {data.shape[1]} ✅</li>
            </ul>""",
            unsafe_allow_html=True)
            
        with column2:
            if data.isnull().values.any():
                st.markdown("""<ul>
                    <li>There is missing value ✅</li>
                </ul>""",unsafe_allow_html=True)
            else:
                st.markdown("""<ul>
                    <li>There is no missing value ✅</li>
                </ul>""",unsafe_allow_html=True)
    with tab4:
        st.dataframe(data.corr())
    st.markdown("___")

    st.subheader("Acknowledgements")
    st.markdown("""
                <p style='background-color:rgb(255, 202, 0,0.3);'> "This dataset is inspired by the UCLA Graduate Dataset. The test scores and GPA are in the older format. 
                The dataset is owned by Mohan S Acharya" (Acharya, M.S.).
                Also, I would like to mention <a href='https://github.com/aditya-sureshkumar/University-Recommendation-System'>Aditya Sureshkumar</a> who made the data available by scrapping it from Edulix.com.
                </p>
                """,unsafe_allow_html=True)
    
    st.markdown('*Please Go to EDA for Data Visualization*')