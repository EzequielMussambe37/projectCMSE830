import streamlit as st

from utilities import EDA,home,conclusion,regression


def hideConfigOption():

    st.set_page_config(
        page_title = "Data Science",
        layout="centered"
    )
    hide_style= """
    <style>
    #MainMenu {visibility:hidden}
    header {visibility:hidden}
    footer {visibility:hidden}
     .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                }
    .viewerBadge_link__qRIco {
        visibility:hidden;
    }
    </style>
    """
    st.markdown(hide_style, unsafe_allow_html=True)
    
    
def options_menu():
    
    return  {"Overview":home,"EDA":EDA,"Regression":regression,"Conclusion":conclusion}

