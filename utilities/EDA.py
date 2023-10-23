# import streamlit as st
# from utilities import dataMani , plots
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd

# def app():
#     st.title("Data Visualization Main")
#     f= dataMani.upload_single_file()
#     st.markdown("""---""")
#     features(f)
#     st.markdown("""---""")
# def features(data,column=[]):
#     p = []
#     df = object
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
#                 #st.plotly_chart(plots.plotly_group(x,x.columns.tolist()), use_container_width=True)
        
#         if key == "pairplot":
#             if value == True:
#                 x = xy_dataframe(data,key)
#                 tool_object = tools(x[0],key)
#                 pair = plots.seanborn_pairplot(x[0],tool_object)
#                 st.pyplot(pair)
#                 st.markdown("""___""")
#         if key == "boxplot":
#             if value == True:
#                 x = xy_dataframe(data,key)
#                 tool_object = tools(x[0])
#                 plots.seanborn_pairplot(x[0],tool_object)
                
#         if key == "dynamic scatter":
            
#             #df = xy_dataframe(data,[])
#             if value == True:
#                 df = dataMani.read_data(data,[])
#                 x = xy_dataframe(data,key)
#                 if len(x[1]) > 0:
#                     print( x[0].columns.tolist()[0])
#                     print(x[1].columns.tolist()[0])
#                     y__label = x[1].columns.tolist()[0]
#                     x__label = x[0].columns.tolist()
#                     tool_object = tools(data)
#                     scatter = plots.dynamic_scatter(df,x__label,y__label,tool_object)
#                     st.plotly_chart(scatter,use_container_width=True)
            
#     return df

# def plot_names():
#     names = ["barplot","boxplot","matplot","dynamic scatter"]
#     ss= {}
#     column1,column2 = st.columns(2)
#     for index, name in enumerate(names,1):
#         if index%2==0:
#             with column1:
#                 n = st.checkbox(name)
#                 ss[name] = n
#         else:
#             with column2:
#                 n = st.checkbox(name)
#                 ss[name] = n
#     return ss


# def xy_dataframe(data,key):
    
#     column1, column2 = st.columns([0.7, 0.3],gap="small")
#     if key in ["barplot","boxplot"]:
#         column1, column2 = st.columns([0.9, 0.1],gap="small")
#     x_frame = []
#     y_target = []
#     object_targeted = {}
#     with column1:
#         x_variables = st.multiselect(
#             "X Features",
#             dataMani.read_data(data,[]).columns.tolist(),
#             key=key
#         )
#         if len(x_variables)>0:
#             x_frame = dataMani.read_data(data,x_variables)
#     if key not in ["barplot","boxplot"]:
#         with column2:
#             target = st.selectbox(
#                 "Target",

#                 tuple([" "]+ dataMani.read_data(data,[]).columns.tolist()),
#                     help="Insert a column that can be used as target when plot xy graph",
#                     key=key+'1'
#             )

#         if target != " ":
#             y_target = dataMani.read_data(data,[target])
#             #object_targeted[target] = y_target
#     return [x_frame,y_target]



# def tools(data):

#     column1,column2,column3= st.columns(3)
#     #print(data)
#     with column1:
#         hue = st.selectbox(
#                     "hue",
#                     tuple([None]+ dataMani.read_data(data,[]).columns.tolist()),
#                         help="Insert a column that can be used as target when plot xy graph",
#                         #key=key+'1'
#         ) 
#     with column2:
#         diag_kind = st.selectbox(
#                     "diagonal kind",
#                     ("auto", "hist", "kde", None)
#                         #key=key+'1'
#         ) 
#     with column3:
#         palette = st.selectbox(
#                     "palette-color",
#                     ("rocket","rocket_r","Spectral", "mako","coolwarm","viridis","cubehelix","YlOrBr","Blues")
#                         #key=key+'1'
#         ) 
#     return {"hue":hue,"diag_kind":diag_kind,"palette_color":palette} 