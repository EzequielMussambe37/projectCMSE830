import streamlit as st
from utilities import dataMani 


def app():
    data = dataMani.read_file("csv",",", "chances.csv")
    st.markdown("<h2 style='text-align: center; color: blue;'>Chances of Admission to Graduate Program</h2>", unsafe_allow_html=True)
    st.header("",divider="green")
    st.write("This is a reason size dataset with 400 data points ")
    st.dataframe(data)
    st.markdown("""___""")
    column3,column4 = st.columns(2,gap="small")
    with column3:
        st.header("Statistics Summary",divider="green")
        st.write("This is the overall statistics summary")
        
        #st.dataframe(data.describe())
        st.dataframe(data.describe())
        
    with column4:
        st.header("Correlation",divider="green")
        st.write("Dataset  overall correlation")
        st.dataframe(data.corr())
