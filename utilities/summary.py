import streamlit as st
from PIL import Image
from utilities import dataMani 



def app():
    
    image = Image.open("./data.jpg")
    data = dataMani.read_file("csv",",", "chances.csv")
    
    
    column5, column6 = st.columns([.7,.3])
    st.markdown("""<h2 style='text-align: center; color: white;'>Data Science Project</h2>""",unsafe_allow_html=True) 
    st.markdown("""<h3 style='text-align: center; color: blue;'>Chances of Admission to a university based on quantitative factors</h3>
                <div style=height:200px;></div>
                
                """,unsafe_allow_html=True)
    # st.markdown("<h2 style='text-align: center; color: blue;'>Chances of Admission to Graduate Program</h2>", unsafe_allow_html=True)
    #st.header("",divider="green")
    # st.write("This is a reason size dataset with 400 data points ")  
    column1,column2 = st.columns(2)
    column3,column4 = st.columns(2)
  
    
    # with column5:

    # with column6:
    #     st.image(image, width=330, caption="ProfilePage") 
    
    

    with column1:
        
        st.dataframe(data)
        
    with column2:                                   
        st.write("This is a reason size dataset with 400 data points ")
    st.markdown("""___""")

    with column3:
        st.header("Statistics Summary",divider="green")
        st.write("This is the overall statistics summary")
        
        #st.dataframe(data.describe())
        st.dataframe(data.describe())
        
    with column4:
        st.header("Correlation",divider="green")
        st.write("Dataset  overall correlation")
        st.dataframe(data.corr())
