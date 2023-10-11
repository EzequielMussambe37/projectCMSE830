import streamlit as st
import seaborn as sns
# import plotly as ply
import plotly.figure_factory as ff
import plotly.express as px
import matplotlib.pyplot as plt
# import plotly.io as pio
#pio.renderers.default = 'browser'



# def plot_graph(type="", 
#             x_frame=[],y_frame=[],hue=None,title=""):
#     pass
    
def plotly_group(hist_data,group_labels):
    fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

    return fig

def seanborn_pairplot(data,tool_object):
    print(data)
    n = sns.pairplot(data,hue=tool_object["hue"],
                     diag_kind=tool_object["diag_kind"],
                     palette=tool_object["palette_color"])
    return n 

def boxplot(data,tool_object):
    s = sns.pairplot(data,hue=tool_object["hue"],
                    diag_kind=tool_object["diag_kind"],
                    palette=tool_object["palette_color"])
    return s
def dynamic_scatter(data,x,y,tool_object):
    fig = px.scatter(data, x=x, y=y, color=tool_object["hue"])
    return fig
