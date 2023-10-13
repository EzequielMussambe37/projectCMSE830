import streamlit as st
from utilities import dataMani , plots
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px



def app():
    df = load_data()
    defaultProject(df)
    

@st.cache_data
def load_data():
    data = dataMani.read_file("csv",",", "chances.csv")
    return data


def defaultProject(data):
    
    st.markdown("<h2 style='text-align: center; color: green;'>Exploratory Data Analysis</h2>", unsafe_allow_html=True)
    st.header("",divider="blue")
    st.write("""Explorer different attributes 
             from the dataset with those defaults plots """)
    
    st.markdown("""___""")
    column1,column2 = st.columns(2,gap="large")


  
    
    with column1:
        st.title("histogram")
        st.write("file one check o")
        # hist = sns.histplot(data=data, x="CGPA")
        fig = px.histogram(data, x="CGPA")
        st.plotly_chart(fig,use_container_width=True)
    with column2:
        st.header("Heatmap")
        st.write("file one check o")
        print(data[["CGPA"]])
        heat = sns.pairplot(data[["CGPA"]])
        st.pyplot(heat)
        
        
    with column1:
        st.title("Scatter")
        st.write("file one check o")
        scatter = px.scatter(data,x="CGPA",y="Chance of Admit ",color="Chance of Admit ")
        st.plotly_chart(scatter,use_container_width=True)
    st.title("Scatter")
    st.write("file one check o")
    scatter = px.scatter(data,x="CGPA",y="Chance of Admit ",color="Chance of Admit ")
    st.plotly_chart(scatter,use_container_width=True)
