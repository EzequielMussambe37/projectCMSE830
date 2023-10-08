import streamlit as st
from utilities import dataMani 

def app():
    st.title("Data Visualization Main")
    features()

def features():
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
                    dataMani.read_data([]).columns.tolist()
                )
        if len(options)>0:
            df = dataMani.read_data(options).transpose()
            st.dataframe(df)
    elif selection == "View All":
        df = dataMani.read_data([])
        st.dataframe(df)
        
    return df

