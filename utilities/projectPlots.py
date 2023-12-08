
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


#PLOTLY PLOTS
def plot_regression(y_test,y_predict):
    
    fig = px.scatter(
        x=y_test,
        y=y_predict,
        title="actual vs predicted")
    return fig

def plotly_scatter(data,x,y,color):
    title ="{} as function of {}".format(y,x)
    
    fig = px.scatter(data,x=x,y=y,color=color)
    fig.update_layout(title_text=title, title_x=0.2)
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
def seaborn_plot_residual(y_test,y_predict):
    fig = plt.figure(figsize=(20,5))
    ax = fig.add_subplot(122)
    sns.distplot((y_test - y_predict),ax=ax,color='b')
    ax.axvline((y_test - y_predict).mean(),color='r',linestyle='--')
    ax.set_title('Check for Residual normality')
    return fig
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
        sns.heatmap(data[columns])
        
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


def seaborn_jointplot(data,x,y,hue=None,kind="kde"):
    # fig = plt.figure(figsize=(10, 10))
    fig = sns.jointplot(data=data,x=x,y=y,hue=hue,kind=kind)
    # fig = sns.jointplot(data=data,x=x,y=y,hue=hue,kind=kind)
    return fig

def scatter_plot(x,y):
    fig = plt.figure(figsize=(10, 10))
    sns.scatterplot(x,y)
    
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