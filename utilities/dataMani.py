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
    
    
    options = upload_load_ExistedFile()
    print(options)
    if options =="Load Existed File":
        return read_file("csv",",","chances.csv")

    elif options == "Upload a new File":
        colum1,colum2 = st.columns(2)

        text_delimeter = {"comma":",","whitespace":" ","semi-colon":";"}
        with colum1:
            delimiter = st.selectbox(
                "Text Delimiter",
                tuple(list(text_delimeter.keys()))
            )

        with colum2:
            uploaded = st.file_uploader("Please Choose a csv file")
        extension = uploaded.name.split(".")[1].strip().lower()
       
        return read_file(extension,text_delimeter[delimiter],uploaded)

def read_file(extension,delimiter, file):

    if extension == "csv":
        f = pd.read_csv(file,delimiter=delimiter)
    elif extension == "txt":
        f = pd.read_table(file,delimiter=delimiter)
    elif extension == "xlsx":
        f = pd.read_excel(file,delimiter=delimiter) 
    f.drop(f.columns[f.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    return f


def upload_load_ExistedFile():
    options= st.radio( 
        "Choose Option to Load Dataset",
        ["Load Existed File","Upload a new File"],
        horizontal=True
    )

    return options
# css-1erivf3 e1b2p2ww15