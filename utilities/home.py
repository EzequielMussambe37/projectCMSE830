import streamlit as st
from utilities import read_data, upload

import pandas as pd


def app():
    columns_name = ["Serial no (or Id)", "GRE Scores (out of 340)", "TOEFL Scores (out of 120)",
    "University Rating (out of 5)"," Statement of Purpose and Letter of Recommendation Strength (out of 5)","Letter of Recommendation",
    "Undergraduate GPA (out of 10)","Research Experience (either 0 or 1)", "Chance of Admit (ranging from 0 to 1)"
        
    ]
    

    

    
   
    #column5, column6 = st.columns([.7,.3])
    ######################################################
    #st.markdown('*Data Science*')
      #* [Pleae Check out my portofolio](https://portfolio-em.streamlit.app) 
    # st.markdown('''
    # **Ezequiel Mussambe**
    # * GIS Analyst and GIS Developer

  

    # ''')
    #st.title('Graduate Admission Prediction Using Regression Model')
    st.markdown(""" <h2 style="text-align:center;">Graduate Admission Prediction Using Regression Model</h2>""",unsafe_allow_html=True)
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
    considering the statement above, the fundamental objective is to develop a predictive model for graduate admission based on quantitative factors such as student GPA, test scores, and personal stamenets and recommendation,etc...,   and measure the influence of all those  features of an applicant's portfolio on admission,to help international students
     to have an idea the chances to get accepted to a university.
    and discuss the limitations and challenges associated with using predictive models for this purpose.
                """)

    st.subheader('Important Note')
    st.markdown("""
                The data set lack a few important information, for instance the universities descriptions,university locations and rank specificity.
                Therefore, the predict model might be limited to the information available in the dataset. Due to this limitation on the dataset available
                or used to performing this. This program is able to take any extending, complete and massive dataset from the user,
                in other word users are able to upload their own data to performing any regression analysis on prediction.
                
                """)

    st.markdown("___")
    # s = ["Load Existed File","Upload a new File"]
    # options= st.radio( 
    #     "Choose Option to Load Dataset",
    #     s,
    #     horizontal=True
    # )
    # st.write("this is options", options)
    
    # st.write(st.session_state.checkedOption)
    # if not st.session_state.get("options"):
        
    #     file_loaded = upload.upload_data()
    # if st.session_state.get("options") == True:
    #     #if st.session_state.checkedOption == ""
    #     upload.checked()
        
    
    # if  st.session_state.checkedOption == "Upload a new File":
    #     try:
    #         file_data = upload.file_uploaded()
    #         # return
    #         if len(data.columns.tolist) != 0:
    #             data = read_data.read_file(file_data["extension"],file_data["delimiter"], file_data["file"])
    #     except:
    #         st.write("this is the file", file_data)
    #         data = read_data.read_file("csv",",", "./utilities/chances.csv")
    # else:
    data = read_data.read_file("csv",",", "./utilities/admission.csv")
    if "data_file" not in st.session_state:
        st.session_state["data_file"]= data
    
    # st.write(st.session_state.get("options"))
    # st.write("This is the section", st.session_state.checkedOption)
    st.write(data)
    # st.dataframe(data)
    st.markdown("___")
    # st.subheader("First Phase")
    # st.markdown("""
    #             The first phase of the project is based on initial exploratory data analysis (EDA), including plotting pair plots to visualize the relationships between attributes, to understand the data distribution and correlations, and to identify any outlier  that could affect the project's overall objectives.
    #             The web application is user-friendly, it allows users to interact with various features of the dataset and visualize the major attributes that  affect admission chances.
    #             **<span style='color:blue'>Below is the Overview of the Data.</span>**
    #             """,unsafe_allow_html=True)
    st.subheader("Column name and data types")
    # st.markdown("""
    #             <ul><
    #             """)
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
    st.dataframe(df.T)

    st.caption('**Table 1.** DataFrame.')
    st.dataframe(data)
    
    st.markdown("""___""")
    st.markdown("<h4 style='text-align:center;'>Statistics Summary</h4>",unsafe_allow_html=True)
    #st.header("",divider="green")
    
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