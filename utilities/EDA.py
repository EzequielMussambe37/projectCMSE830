import streamlit as st
from utilities import projectPlots as pp, read_data

# Loading the data
@st.cache_data
def load_data():
    data = read_data.read_file("csv",",", "./utilities/chances.csv")
    return data

#Main app Function.
def app():
    df = load_data()
    st.header("",divider="grey")
    st.markdown("<h2 style='text-align: center; color: green;'>Exploratory Data Analysis</h2>", unsafe_allow_html=True)

    st.markdown("""
                Data visualization is a powerful tool, it allows us to effectively identify patterns, trends, outliers or even data anomalies.
                While statistics numbers provide valuable insights, there is visual language that can communicate complex data distribution in a way that is both intuitive and powerful.
                """)
   
    
    st.markdown("""
               #### There are two Panels:
                * **:blue[Data Distribution Panel]**
                * **:blue[Data Relationship Panel]**
                """)

    #st.header("",divider="blue")
    distribution(df)
    st.header("",divider="green")
    correlation(df)

#Distribution type of plots
def distribution(data):
    with st.expander("Data Distribution Panel",expanded=True):
        st.subheader(":blue[OverView]")
        st.markdown("""
                * The target attribute for this project is  called "Chance of Admit".
                The distribution of the GRE Score, TOEFL SCORE, CGPA,SOP resemble a normal distribution.
                It is also important to highlight that the attributes are all numeric.
                
                """)
        
        st.markdown("___")
        
        # st.header(":blue[Histogram and Distribution Plots]")
        # st.markdown("""
        #             * Histograms provide a clear overview of data point frequencies across various ranges,
        #             while univariate density distribution plots enable a comprehensive view of individual variable distributions within the dataset.
        #             These essential tools empower data professionals to extract valuable insights from diverse data sources.
        #             """)
        st.markdown('''
        *The default attributes were selected based on the relation with the target*
        ''')
        
        column1,column2 = st.columns(2,gap="large")
        
        with column1:
            selected_column = st.selectbox(
                "",
                data.columns[1:],
                index=len(data.columns[1:])-1,
                key = "hist-dis"
            )
            fig = pp.seaborn_hist(data,selected_column)
            st.pyplot(fig)
            descriptionHist(selected_column)
           
        with column2:
            selected_column = st.selectbox(
                "",
                data.columns[1:],
                index=5,
                key="dist-dist"
            )
            fig = pp.seaborn_dist(data,selected_column)
            st.pyplot(fig)
            descriptionHist(selected_column)
        # st.header("",divider="green")
        st.markdown("___")
        # st.header(":blue[Box and Violin Plots]")
        # st.markdown("""
        #             * Box plots efficiently emphasize dataset characteristics like quartiles, median, and outliers.
        #             Similarly, violin plots, a family of distribution plots, offer a powerful means to visualize data distribution shapes. 
        #             This facilitates the clear representation of selected values' distributions, enabling insightful data exploration.
        #             """)
        st.markdown('''
        *The default attributes were selected based on the relation with the target*
        ''')
        column1,column2 = st.columns(2,gap="large")
        with column1:
            selected_column = st.multiselect(
                "",
                data.columns[1:],
                default=data.columns[-1],
                key="box-dist"
            )
            
            fig = pp.plotly_boxplot(data,selected_column)
            st.plotly_chart(fig,use_container_width=True)
            descriptionBoxplot(selected_column)
            
        with column2:
            
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
            fig = pp.seaborn_violinplot(data,selected_column,selected_kind)
            st.pyplot(fig)
            descriptionBoxplot(selected_column)
        st.markdown("___")
        # st.header(":blue[Pairwise Plot]")
        # st.markdown("""
        #             * In short: Allows to visualize both the distribution of single variable and the relationship between two variables..
        #             """)
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
        fig = pp.seaborn_pairwise(data,selected_column,selected_hue)
        st.pyplot(fig)


#Correlation type of Plots
def correlation(data):

    with st.expander("Data Relationship Panel",expanded=False):
        st.subheader(":blue[OverView]")
        st.markdown("""
                    
                * The :blue[GRE Score, CGPA,TOEFL Score] are the main independent candidate that pontentially can explain the changes in the target variable (:blue[Chance of Admit]).
                Observe that there is a positive correlation between the target variable ( :blue[Chance of Admit] ), and independent variables
                
                """)
        st.markdown("""
                * The objective of this exploratory data analysis (EDA) section is to discern the key 
                factors which can impact the target variable, which is denoted as "Chance of Admit." 
                The EDA process entails a comprehensive examination of various attributes within the dataset in order to identify and assess their potential influence on the target variable. 
                """)
        
        st.markdown("___")
        # st.header(":blue[Scatter Plot]")
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

        fig = pp.plotly_scatter(data,selected_column,selected_target,selected_color)
        st.plotly_chart(fig,use_container_width=True)
        descriptionCorr(selected_column,selected_target)
        st.markdown("""___""")
        st.header(":blue[Joint Plot]")
        column_x, column_y,column_hue,column_color = st.columns([.3,.3,.2,.2])
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
        with column_hue:
            selected_hue = st.selectbox(
                "Select hue",
                [None] + list(data.columns[1:]),
                key="hue-joint"
            ) 
        with column_color:
            selected_type = st.selectbox(
                "Select kind",
                ["reg","scatter","kde","hist","hex"],
                key="shape-joint"
            ) 
        fig = pp.seaborn_jointplot(data,selected_column,selected_target,selected_hue,selected_type)
        st.pyplot(fig)
        st.markdown("___")
        column1, column2 = st.columns(2)
        st.header(":blue[Correlation Matrix( HeatMap)]")
        selected_column = st.multiselect(
            "Select Attribute",
            data.columns[1:],
            default=[data.columns[-1],data.columns[1],data.columns[2]],
            key="heat-corr"
            )
        
        fig = pp.seaborn_heatmap(data, selected_column)
        st.pyplot(fig)
        #descriptionCorr(selected_column,selected_target)
        
def descriptionHist(selected_column): 
    st.caption(f'You can visualize how the :blue[{selected_column.upper()}] is distributed and you can spot and identify any known trend.Is it normal distributed or skew to the right or left?.')

def descriptionBoxplot(selected_column): 
    st.caption(f' Check the median, mode, etc... of the followings columns :blue[{str(selected_column)[1:-1]}]. Is there outliers or any anamolity on the distribution of the data?')

def descriptionCorr(x_column,y_column):
    st.caption(f"""Please check the correlation between the independent variable :blue[{x_column}] 
               against the dependent variable also called target :green[{y_column}].
               Is there any clear correlation between the two variables ( positive, negative or no-correlation)""")