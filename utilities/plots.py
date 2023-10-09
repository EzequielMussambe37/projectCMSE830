import streamlit as st
import seaborn as sns
import plotly as ply
import plotly.figure_factory as ff




def plot_graph(type="", 
               x_frame=[],y_frame=[],hue=None,title=""):
    pass
    
def plotly_group(hist_data,group_labels):
    fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

    return fig

def seanborn_plot(data,hue):
    
    n = sns.pairplot(data,hue)
    st.plotly_chart(n,use_container_width=True)