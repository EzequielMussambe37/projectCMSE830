import streamlit as st

from utilities import EDA


def hideConfigOption():
    st.set_page_config(
        page_title = "Main"
    )
    
    
    hide_style= """
    <style>
    #MainMenu {visibility:hidden}
    header {visibility:hidden}
    footer {visibility:hidden}
    </style>
    """
    st.markdown(hide_style, unsafe_allow_html=True)
    
    
def options_menu():
    
    return  {"EDA":EDA,"ML":"","Main":""}