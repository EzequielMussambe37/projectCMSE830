import streamlit as st
from utilities import projectPlots as pp, read_data,EDA



def app():
    st.header("Conclusion of the First Part of the Project")


    st.header("",divider="green")

    st.write("""
            The project aimed to create a user-friendly tool for data exploration, 
            helping users identify potential attributes that could serve as strong predictors for graduate program admission chances. 
            Upon exploration and visualization, we found that test attributes exhibit a positive correlation with the admission probability, 
            suggesting their suitability as potential predictors.
            """)

    st.markdown("___")
    st.write("""This project aims to provide invaluable insights to potential postgraduate 
            aspirants through Data Science tools and web user interface. 
            Staring with EDA(Exploration Data Analysis ) web application, which empower 
            users to explore and gain insights from the chance of admission  dataset
            in a interactive and visually informative way, helping to make the decision-making
            more accessible and efficient. 
            Next Part will be the implementation of Regression Analysis.
            
            """)

    st.markdown("___")
    # column1, column2 = st.columns(2)
    data=EDA.load_data()
    # with column1:
    fig = pp.plotly_scatter(data,"CGPA", "Chance of Admit ","Chance of Admit ")
    st.plotly_chart(fig)
    # with column2:
    fig = pp.plotly_scatter(data,"TOEFL Score", "Chance of Admit ","Chance of Admit ")
    st.plotly_chart(fig)
        
    # column3, column4 = st.columns(2)
    # with column3:
        
    fig = pp.plotly_scatter(data,"GRE Score", "Chance of Admit ","Chance of Admit ")

    st.plotly_chart(fig)
    # with column4:
    fig = pp.plotly_scatter(data,"SOP", "Chance of Admit ","Chance of Admit ")

    st.plotly_chart(fig)



