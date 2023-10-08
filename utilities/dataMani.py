import pandas as pd
import streamlit as st

main_file = object
def read_data(df,columns):
    
    if len(columns) > 0:
        
        df = df[columns]
        return df
    
    else:
        return df
    
    
def upload_single_file():
    uploaded = st.file_uploader("Please Choose a csv file",type={"csv", "txt"})
    print(uploaded.name)
    
    return read_file(uploaded)
    # else:
    #     st.warning("you need to upload csv file")
def read_file(file):
    f = pd.read_csv(file)
    return f
