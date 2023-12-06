import pandas as pd
import streamlit as st

@st.cache_data
def read_file(extension,delimiter, file):

    if extension == "csv":
        f = pd.read_csv(file,delimiter=delimiter)
    elif extension == "txt":
        f = pd.read_table(file,delimiter=delimiter)
    elif extension == "xlsx":
        f = pd.read_excel(file,delimiter=delimiter) 
    f.drop(f.columns[f.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    
    return f