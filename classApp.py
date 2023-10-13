
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np
import math
from utilities import configFile,styles

# st.set_page_config(layout = "wide")
simple_plot_List = ["pairplot", "histgram","barplot","violinplot","boxplot"]

advance_plot_list = []
class mainApp:

    def __init__(self):
        self.apps = []

    def ret(self):
        return self.options_menu
    def run():
        configFile.hideConfigOption()
        with st.sidebar:
            selected = styles.styleSettings() 
        try:
            configFile.options_menu()[selected].app()
        except:
            pass

if __name__ == '__main__':
    mainApp.run()
    data_file = "recommendation.csv"