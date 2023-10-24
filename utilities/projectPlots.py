
from utilities import read_data 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


#PLOTLY PLOTS
def plotly_scatter(data,x,y,color):
    fig = px.scatter(data,x=x,y=y,color=color)

    return fig

def plotly_boxplot(data,column):
    fig = px.box(data[column],points="outliers")
    fig.update_layout(showlegend=False)
    fig.update_yaxes(showgrid=False)
    fig.update_traces(quartilemethod="exclusive")

    return fig

def plotly_violin(data,y="CGPA"):
    
    fig = go.Figure(data=go.Violin(y=data, box_visible=True, 
                                   line_color='black',meanline_visible=True, fillcolor='lightseagreen', opacity=0.6,
                               x0=y))

    fig.update_layout(yaxis_zeroline=False)
    return fig

def plotly_bar(data, x="CGPA",orientation="h"):
    
    result = px.bar(data, x=x,orientation=orientation, color_discrete_sequence=["#0083B8"]*len(data))
    return result



# SEABORN PLOTS
def seaborn_pairwise(data,columns,hue=None):
    fig = sns.pairplot(data[columns], hue=hue)
    
    return fig 
    
def seaborn_violinplot(data, columns,kind):
    fig = sns.catplot(data=data[columns],kind=kind)
    
    return fig
def seaborn_heatmap(data,columns):
    
    print(data[columns])
    
    fig = define_size()
    if len(columns) > 1:
        sns.heatmap(data[columns].corr(), annot=True)
    else:
        sns.heatmap(data[columns], annot=True)
        
    return fig
def seaborn_boxplot(data,columns):
    fig = define_size()
    n = sns.boxplot(data[columns])
    return fig
def pairplot(data,columns=["CGPA"], hue=None):
    result = sns.pairplot(data[columns],hue = hue)
    return result
def seaborn_hist(data,x="CGPA"):
    
    fig = define_size()
    n = sns.histplot(x=x,data=data)
    title = f"Histogram of {x}"
    defaultSetting(n,title,x,)
    return fig

def seaborn_dist(data,x="CGPA"):
    fig = define_size()
    n = sns.distplot(data[[x]])
    title = f"Distribution of {x}"
    defaultSetting(n,title,x,)
    return fig


def seaborn_jointplot(data,x,y, kind="reg"):
    fig = sns.jointplot(x=x,y=y,data=data,kind=kind,fill=True,cmap="mako")
    return fig


def  seaborn_barplot(data,x='Research',y='GRE Score'):
    
    fig = plt.figure(figsize=(10, 10))
    sns.barplot(x =x,y=y,data =data)
    return fig

# PLOT BASICS SETTINGS
def defaultSetting(n,title,x,):
    n.set_title(title, fontsize=20, pad=30, fontdict={"weight": "bold"})
    n.set_xlabel(x, fontsize=16)
    n.set_ylabel("Count", fontsize=18)
 
def define_size():
     fig = plt.figure(figsize=(10, 10)) 
     return fig  
 
 





