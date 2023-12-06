import streamlit as st
 
def upload_data():

    options= st.radio( 
        "Choose Option to Load Dataset",
        ["Load Existed File","Upload a new File"],
        horizontal=True
    )
    if options == "Upload a new File":
        st.session_state.options = True
        st.session_state.checkedOption = options
        st.experimental_rerun()
def checked():
    
    options= st.radio( 
        "Choose Option to Load Dataset",
        ["Upload a new File","Load Existed File"],
        horizontal=True
    )
    if options == "Load Existed File":
        st.session_state.options = False
        st.experimental_rerun()
        st.session_state.checkedOption = options
    
    
def file_uploaded():
    text_delimeter = {"comma":",","whitespace":" ","semi-colon":";"}
    colum1,colum2 = st.columns(2)
    with colum1:
        delimiter = st.selectbox(
            "Text Delimiter",
            tuple(list(text_delimeter.keys()))
        )
    with colum2:
        uploaded = st.file_uploader("Please Choose a csv file")
    extension = uploaded.name.split(".")[1].strip().lower()
    return {"extension":extension,"delimiter":text_delimeter[delimiter],"file":uploaded}
