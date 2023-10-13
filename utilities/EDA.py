import streamlit as st
from utilities import dataMani , plots
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd





def app():
    st.title("Data Visualization Main")
    f= dataMani.upload_single_file()
    st.markdown("""---""")
    features(f)
    st.markdown("""---""")
def features(data):
    df = object
    plots_object = object
    with st.sidebar:
    plots_selection(data)
# def features(data,column=[]):

#     df = objects
#     plots_object = object
#     with st.sidebar:

#         selection = st.radio (
#             "Data Table",
#             ["None", "All"],
#             horizontal=True
#         )
#         st.markdown("""___""")
#         st.title("Plots")
#         plots_object = plot_names()

#     if selection == "All":
#         with st.expander("See the table"):
#             df = dataMani.read_data(data,[])
#             st.dataframe(df)
#     for key, value in plots_object.items():
#         if key == "barplot":
#             if value == True:
#                 x = xy_dataframe(data,key)
#                 tool_object = tools(x[0])
#                 plots.boxplot(x[0],tool_object)
#         if key == "pairplot":
#             if value == True:
#                 x = xy_dataframe(data,key)
#                 tool_object = tools(x[0])
#                 box_plot = plots.seanborn_pairplot(x[0],tool_object)

#                 st.pyplot(box_plot,clear_figure=False) 
#         if key == "dynamic scatter":
#             print("this is the dynamically....")
#             print(key)
#             if value == True:
#                 df = dataMani.read_data(data,[])
#                 x = xy_dataframe(data,key)
#                 if len(x[1]) > 0:
#                     print( x[0].columns.tolist()[0])
#                     print(x[1].columns.tolist()[0])
#                     y__label = x[1].columns.tolist()[0]
#                     x__label = x[0].columns.tolist()
#                     tool_object = tools(data)
#                     print(tool_object)
#                     scatter_dynamic = plots.dynamic_scatter(df,x__label,y__label,tool_object)
#                     st.plotly_chart(scatter_dynamic, use_container_width=True)
#     return df


def plots_selection(data):
    xy_dataframe_scatter(data)
    # with st.sidebar:
    #     column1, column2,column3 = st.columns(3)
    #     with column1:
    #         barplot_boolean = st.checkbox('barplot')

    #     with column2:
    #         boxplot_boolean = st.checkbox('boxplot')

    #     with column3:
    #         pairplot_boolean = st.checkbox('pairplot')

    #     with column1:
    #         dyscatter_boolean = st.checkbox('scatter')

    # print("alll datattt")
    # print(dyscatter_boolean)
    # print(pairplot_boolean)


    # if dyscatter_boolean:
    # with sidebar:
    #     barplot_boolean = st.checkbox('barplot')

    # if barplot_boolean:    
    #     x = xy_dataframe_scatter(data)
    #     if len(x[1]) > 0:
    #         print( x[0].columns.tolist()[0])
    #         print(x[1].columns.tolist()[0])
    #         y__label = x[1].columns.tolist()[0]
    #         x__label = x[0].columns.tolist()
    #         tool_objects = tool_scatter(data)
    #         print(tool_object)
    #         scatter_dynamic = plots.dynamic_scatter(data,x__label,y__label,tool_object)
    #         st.plotly_chart(scatter_dynamic, use_container_width=True)


    # if pairplot_boolean:

    #     xx = xy_dataframe_pairplot(data)
    #     print( xx[0].columns.tolist()[0])
    #     tool_objects =tool_pairplot(xx[0])

    #     pairplot = plots.seanborn_pairplot(xx[0],tool_objects)
    #     st.pyplot(pairplot)

def xy_dataframe_scatter(data,key):


    # with sidebar:
    #     barplot_boolean = st.checkbox('barplot')
    # if barplot_boolean:  

    column1, column2 = st.columns([0.7, 0.3],gap="small")
    x_frame = []
    y_target = []
    object_targeted = {}
    with column1:
        x_variables = st.multiselect(
            "X Features",
            dataMani.read_data(data,[]).columns.tolist(),
            key=key
        )
        if len(x_variables)>0:
            x_frame = dataMani.read_data(data,x_variables)
    with column2:
        target = st.selectbox(
            "Target",

            tuple([" "]+ dataMani.read_data(data,[]).columns.tolist()),
                help="Insert a column that can be used as target when plot xy graph",
                key=key + "1"
        )

    if target != " ":
        y_target = dataMani.read_data(data,[target])

    #=======================================
        y__label = y_target.columns.tolist()[0]
        x__label = x_frame.columns.tolist()
        tool_objects = tool_scatter(data,key)
        print("this is the scatter")
        print(tool_objects)
        scatter_dynamic = plots.dynamic_scatter(data,x__label,y__label,tool_objects)
        st.plotly_chart(scatter_dynamic, use_container_width=True)

def xy_dataframe_pairplot(data):

    #column1 = st.columns(1)
    x_frame = []
    y_target = []
    object_targeted = {}
    #with column1:
    x_variables = st.multiselect(
        "X Features",
        dataMani.read_data(data,[]).columns.tolist(),
        key="pairplot-x"
    )

    if len(x_variables)>0:
        x_frame = dataMani.read_data(data,x_variables)

    print("this is scatter plot")
    print(x_frame)
    return [x_frame]
























<<<<<<< HEAD
=======
    if selection == "All":
        with st.expander("See the table"):
            df = dataMani.read_data(data,[])
            st.dataframe(df)
    for key, value in plots_object.items():
        
        if key == "barplot":
            if value == True:
                x = xy_dataframe(data,key)
                #st.plotly_chart(plots.plotly_group(x,x.columns.tolist()), use_container_width=True)
        if key == "pairplot":
            if value == True:
                x = xy_dataframe(data,key)
                tool_object = tools(x[0],key)
                pair = plots.seanborn_pairplot(x[0],tool_object)
                st.pyplot(pair)
                st.markdown("""___""")
        if key == "dynamic scatter":
            
            #df = xy_dataframe(data,[])
            if value == True:
                df = dataMani.read_data(data,[])
                x = xy_dataframe(data,key)
                if len(x[1]) > 0:
                    print( x[0].columns.tolist()[0])
                    print(x[1].columns.tolist()[0])
                    y__label = x[1].columns.tolist()[0]
                    x__label = x[0].columns.tolist()
                    tool_object = tools(data,key)
                # print()
                    scatter = plots.dynamic_scatter(df,x__label,y__label,tool_object)
                    st.plotly_chart(scatter,use_container_width=True)
                st.markdown("""___""")
    return df
>>>>>>> 02d5830c308e189119c0c4f72a4062d22e22e12c

def plot_names():
    names = ["barplot","boxplot","matplot","dynamic scatter","pairplot"]
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
    # if key in ["barplot","boxplot"]:
    #     column1, column2 = st.columns([0.9, 0.1],gap="small")
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
    if key not in ["barplot","boxplot","pairplot"]:
        with column2:
            target = st.selectbox(
                "Target",

                tuple([" "]+ dataMani.read_data(data,[]).columns.tolist()),
                    help="Insert a column that can be used as target when plot xy graph",
                    key=key+'1'
            )

        if target != " ":
            y_target = dataMani.read_data(data,[target])
    return [x_frame,y_target]



<<<<<<< HEAD
def tool_scatter(data,key):

    column1,column2,column3= st.columns(3)
    print("ssshhhhhhhhh")
    print(key)
    with column1:
        hue = st.selectbox(
                "hue",
                tuple([None]+ dataMani.read_data(data,[]).columns.tolist()),
                 key = key+"2") 

    with column2:
        diag_kind = st.selectbox(
                "diagonal kind",
                ("auto", "hist", "kde", None),
                key =key+"3") 

    with column3:
        palette = st.selectbox(
                 "palette-color",
                ("rocket","rocket_r","Spectral", "mako","coolwarm","viridis","cubehelix","YlOrBr","Blues"),
                key = key+"4") 
    #print({"hue":hue,"diag_kind":diag_kind,"palette_color":palette})
    return {"hue":hue,"diag_kind":diag_kind,"palette_color":palette} 




def tool_pairplot(data):
=======
def tools(data,key):
>>>>>>> 02d5830c308e189119c0c4f72a4062d22e22e12c

    column1,column2,column3= st.columns(3)
    #print(data)
    with column1:
        hue = st.selectbox(
                    "hue",
                    tuple([None]+ dataMani.read_data(data,[]).columns.tolist()),
<<<<<<< HEAD
                        help="Insert a column that can be used as target when plot xy graph",
                        key="apirplot-column1"
=======
                    key=key+"2",
                    help="Insert a column that can be used as target when plot xy graph",
                        #key=key+'1'
>>>>>>> 02d5830c308e189119c0c4f72a4062d22e22e12c
        ) 
    with column2:
        diag_kind = st.selectbox(
                    "diagonal kind",
                    ("auto", "hist", "kde", None),
<<<<<<< HEAD
                    key="apirplot-column2"
=======
                    key=key+'3'
>>>>>>> 02d5830c308e189119c0c4f72a4062d22e22e12c
        ) 
    with column3:
        palette = st.selectbox(
                    "palette-color",
                    ("rocket","rocket_r","Spectral", "mako","coolwarm","viridis","cubehelix","YlOrBr","Blues"),
<<<<<<< HEAD

                    key="apirplot-column3"
=======
                    key=key+'4'
>>>>>>> 02d5830c308e189119c0c4f72a4062d22e22e12c
        ) 
    return {"hue":hue,"diag_kind":diag_kind,"palette_color":palette} 