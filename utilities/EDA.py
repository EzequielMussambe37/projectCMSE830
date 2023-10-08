import streamlit as st
from utilities import dataMani 
import pandas as pd

def app():
    st.title("Data Visualization Main")
    f= dataMani.upload_single_file()
    features(f)
    #st.dataframe(f)

    #st.write_csv("chances.csv",uploaded.upload_url)
    # df = st.dataframe(f)
    # df
    #features()

def features(data,column=[]):
    p = []
    df = object
    with st.sidebar:

        selection = st.selectbox (
            "Visualize DataFrame",
            ("", "View All", "Select Atributes")
        )

    if selection == "Select Atributes":
        with st.sidebar:
                options = st.multiselect(
                    "What Features",
                    dataMani.read_data(data,[]).columns.tolist()
                )
        if len(options)>0:
            df = dataMani.read_data(data,options).transpose()
            st.dataframe(df)
    elif selection == "View All":
        df = dataMani.read_data(data,[])
        st.dataframe(df)
        
    return df

