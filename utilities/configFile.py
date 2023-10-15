import streamlit as st

from utilities import EDA,projectPlots,summary


def hideConfigOption():

    st.set_page_config(
        page_title = "Main",
        layout="wide"
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
    </style>
    """
    st.markdown(hide_style, unsafe_allow_html=True)
    
    
    
def options_menu():
    
    return  {"Overview":summary,"Dynamic EDA":EDA,"ML":"","EDA":projectPlots}

