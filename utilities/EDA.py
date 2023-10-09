import streamlit as st
from utilities import dataMani , plots
import pandas as pd

def app():
    st.title("Data Visualization Main")
    f= dataMani.upload_single_file()
    st.markdown("""---""")
    features(f)
    st.markdown("""---""")
def features(data,column=[]):
    p = []
    df = object
    plots_object = object
    with st.sidebar:

        selection = st.radio (
            "Data Table",
            ["None", "All"],
            horizontal=True
        )
        st.markdown("""___""")
        st.title("Plots")
        plots_object = plot_names()

    if selection == "All":
        with st.expander("See the table"):
            df = dataMani.read_data(data,[])
            st.dataframe(df)
    for key, value in plots_object.items():
        if key == "barplot":
            if value == True:
                x = xy_dataframe(data,key)
                #st.plotly_chart(plots.plotly_group(x,x.columns.tolist()), use_container_width=True)
        if key == "boxplot":
            if value == True:
                x = xy_dataframe(data,key)
                print(x[0])
                plots.seanborn_plot(x[0])
                #st.plotly_chart(plots.seanborn_plot(x),use_container_width=True)

   
    return df

def plot_names():
    names = ["barplot","boxplot","matplot","l"]
    ss= {}
    column1,column2 = st.columns(2)
    for index, name in enumerate(names,1):
        if index%2==0:
            with column1:
                n = st.checkbox(name)
                ss[name] = n
        else:
            with column2:
                n = st.checkbox(name)
                ss[name] = n
    return ss


def xy_dataframe(data,key):
    
    column1, column2 = st.columns([0.7, 0.3],gap="small")
    if key in ["barplot","boxplot"]:
        column1, column2 = st.columns([0.9, 0.1],gap="small")
    x_frame = []
    y_target = []
    with column1:
        x_variables = st.multiselect(
            "X Features",
            dataMani.read_data(data,[]).columns.tolist(),
            key=key
        )
        if len(x_variables)>0:
            x_frame = dataMani.read_data(data,x_variables)
    if key not in ["barplot","boxplot"]:
        with column2:
            target = st.selectbox(
                "Target",

                tuple([" "]+ dataMani.read_data(data,[]).columns.tolist()),
                    help="Insert a column that can be used as target when plot xy graph",
                    key=key+'1'
            )

        if target != " ":
            y_target = dataMani.read_data(data,target)
    return [x_frame,y_target]