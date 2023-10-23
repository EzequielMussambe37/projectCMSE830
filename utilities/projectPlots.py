import streamlit as st
from utilities import dataMani , plots
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

# SEABORN PPLOTTTTSS===================
@st.cache_data
def seaborn_pairwise(data,columns,hue=None):
    #sns.set_theme(style="ticks")
    # fig = define_size()
    fig = sns.pairplot(data[columns], hue=hue)
    
    return fig 
    
def seaborn_violinplot(data, columns,kind):
    #fig = define_size()
    fig = sns.catplot(data=data[columns],kind=kind)
    
    return fig
def seaborn_heatmap(data,columns):
    
    print(data[columns])
    
    fig = define_size()
    # fmt="d", linewidths=.5
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
    #fig = define_size()
    fig = sns.jointplot(x=x,y=y,data=data,kind=kind,fill=True,cmap="mako")
    # plt.title('CGPA vs GRE score')
    return fig


def  seaborn_barplot(data,x='Research',y='GRE Score'):
    
    fig = plt.figure(figsize=(10, 10))
    sns.barplot(x =x,y=y,data =data)
    return fig

def defaultSetting(n,title,x,):
    n.set_title(title, fontsize=20, pad=30, fontdict={"weight": "bold"})
    n.set_xlabel(x, fontsize=16)
    n.set_ylabel("Count", fontsize=18)
 
def define_size():
     fig = plt.figure(figsize=(10, 10)) 
     return fig  
def app():
    df = load_data()
    st.markdown("<h2 style='text-align: center; color: green;'>Exploratory Data Analysis</h2>", unsafe_allow_html=True)
    st.markdown("""
                Data visualization is a powerful tool, it allows us to effectively identify patterns, trends, outliers or even data anomalies.
                While statistics numbers provide valuable insights, there is visual language that can communicate complex data distribution in a way that is both intuitive and powerful.
                """)
    st.header("",divider="blue")
    distribution(df)
    correlation(df)
    

@st.cache_data
def load_data():
    data = dataMani.read_file("csv",",", "chances.csv")
    return data


def distribution(data):

    # st.write("""Explorer different attributes 
    #          from the dataset with those defaults plots """)
    # st.markdown("""___""")
    with st.expander("Data Distribution Panel",expanded=True):
        
        st.header("Histogram and Distribution Plots")
        st.markdown("""
                    * Histograms provide a clear overview of data point frequencies across various ranges,
                    while univariate density distribution plots enable a comprehensive view of individual variable distributions within the dataset.
                    These essential tools empower data professionals to extract valuable insights from diverse data sources.
                    """)
        st.markdown('''
        *The default attributes were selected based on the relation with the target*
        ''')
        
        column1,column2 = st.columns(2,gap="large")
        
        with column1:
            #st.header("Histogram")
            selected_column = st.selectbox(
                "",
                data.columns[1:],
                index=len(data.columns[1:])-1,
                key = "hist-dis"
            )
            fig = seaborn_hist(data,selected_column)
            st.pyplot(fig)
        with column2:
            #st.header("Distribution Plot")
            selected_column = st.selectbox(
                "",
                data.columns[1:],
                index=5,
                key="dist-dist"
            )
            fig = seaborn_dist(data,selected_column)
            st.pyplot(fig)
            
        st.header("",divider="green")
        st.header("Box and Violin Plots")
        st.markdown("""
                    * Box plots efficiently emphasize dataset characteristics like quartiles, median, and outliers.
                    Similarly, violin plots, a family of distribution plots, offer a powerful means to visualize data distribution shapes. 
                    This facilitates the clear representation of selected values' distributions, enabling insightful data exploration.
                    """)
        st.markdown('''
        *The default attributes were selected based on the relation with the target*
        ''')
        column1,column2 = st.columns(2,gap="large")
        with column1:
            #st.header("Box Plot")
            selected_column = st.multiselect(
                "",
                data.columns[1:],
                default=data.columns[-1],
                key="box-dist"
            )
            
            fig = plotly_boxplot(data,selected_column)
            st.plotly_chart(fig,use_container_width=True)
            
        with column2:
            
            #st.header("Violin/Box Plot")
            column_data, column_kind = st.columns([.7,.3])
            with column_data:
                selected_column = st.multiselect(
                    "",
                    data.columns[1:],
                    default=[data.columns[1]],
                    key="violin-dist1"
                )
            with column_kind:
                selected_kind = st.selectbox(
                    "Select kind",
                    ["violin","box"],
                    help="user can choose between violin andd bosxplot",
                    key="violin-dist2",

                )
            fig = seaborn_violinplot(data,selected_column,selected_kind)
            st.pyplot(fig)

        #with column2:

        st.header("Pairwise Plot")
        st.markdown("""
                    * In short: Allows to visualize both the distribution of single variable and the relationship between two variables..
                    """)
        st.markdown('''
        *The default attributes were selected based on the relation with the target*
        ''')
        column_data, column_hue = st.columns([.7,.3])
        with column_data:
            selected_column = st.multiselect(
                "Select any attribute",
                data.columns[1:],
                default=[data.columns[-1],data.columns[1]],
                key="pairwise-dist"
            )
        with column_hue:
            selected_hue = st.selectbox(
                "Select Hue",
                [None]+selected_column,
                key="hue-dist"
            )
        fig = seaborn_pairwise(data,selected_column,selected_hue)
        st.pyplot(fig)








def correlation(data):

    with st.expander("Data Relationship Panel",expanded=False):
        #column1,column2 = st.columns(2,gap="large")
        #with column1:
        st.header("Scatter Plot")
        column_x, column_y,column_color = st.columns([.4,.3,.3])
        
        with column_x:
            selected_column = st.selectbox(
                "Select X attribute",
                data.columns[1:],
                key="x-corr"
            )
        with column_y:
            selected_target = st.selectbox(
                "Select Target",
                data.columns[1:],
                index=len(data.columns[1:])-1,
                key="target-corr"
            )
        with column_color:
            selected_color = st.selectbox(
                "Select color attribute",
                data.columns[1:],
                index=len(data.columns[1:])-1,
                key="color-corr"
            ) 


        


        fig = plotly_scatter(data,selected_column,selected_target,selected_color)
        st.plotly_chart(fig,use_container_width=True)
        st.markdown("""___""")

        column_x, column_y,column_color = st.columns([.4,.3,.3])
        with column_x:
            selected_column = st.selectbox(
                "Select X attribute",
                data.columns[1:],
                key="x-joint"
            )
        with column_y:
            selected_target = st.selectbox(
                "Select Target",
                data.columns[1:],
                index=len(data.columns[1:])-1,
                key="target-joint"
            )
        with column_color:
            selected_type = st.selectbox(
                "Select color attribute",
                ["reg"],
                
                key="color-joint"
            ) 
        # fig = seaborn_jointplot(data,selected_column,selected_target,selected_type)
        
        # st.pyplot(fig)
        column1, column2 = st.columns(2)
        
        
        #with column1:
        selected_column = st.multiselect(
            "Select Attribute",
            data.columns[1:],
            default=[data.columns[-1],data.columns[1],data.columns[2]],
            key="heat-corr"
            )

        fig = seaborn_heatmap(data, selected_column)
        st.pyplot(fig)
        # with column2:
            #seaborn_heatmap()
            # fig = seaborn_pairwise(data,selected_column,selected_hue)
            # st.pyplot(fig)
        # with column1:
        #     st.header("Correlation")
        #     selected_column = st.selectbox(
        #         "Select any attribute",
        #         data.columns[1:],
        #         index=len(data.columns[1:])-1,
        #         key = "hist"
        #     )
        #     fig = seaborn_hist(data,selected_column)
        #     st.pyplot(fig)
        # with column2:
        #     st.header("Distribution Plot")
        #     selected_column = st.selectbox(
        #         "Select any attribute",
        #         data.columns[1:],
        #         index=len(data.columns[1:])-1,
        #         key="dist"
        #     )
        #     fig = seaborn_dist(data,selected_column)
        #     st.pyplot(fig)
        # with column1:
        #     st.header("Box Plot")
        #     selected_column = st.multiselect(
        #         "Select any attribute",
        #         data.columns[1:],
        #         default=data.columns[-1],
        #         key="violin"
        #     )
            
        #     fig = plotly_boxplot(data,selected_column)
        #     st.plotly_chart(fig,use_container_width=True)
        
            
            
            
    # with column1:
    #     st.title("Scatter")
    #     st.write("file one check o")
    #     scatter = px.scatter(data,x="CGPA",y="Chance of Admit ",color="Chance of Admit ")
    #     st.plotly_chart(scatter,use_container_width=True)
    # st.title("Scatter")
    # st.write("file one check o")
    # scatter = px.scatter(data,x="CGPA",y="Chance of Admit ",color="Chance of Admit ")
    # st.plotly_chart(scatter,use_container_width=True)




# def 
# sb.jointplot(x = 'CGPA',y ='GRE Score',data = admission_predict,kind = 'kde',fill = True,cmap = 'mako')
# plt.title('CGPA vs GRE score')
# plt.show()
