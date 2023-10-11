
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np
import math
from utilities import configFile,styles, EDA



simple_plot_List = ["pairplot", "histgram","barplot","violinplot","boxplot"]

advance_plot_list = []
class mainApp:

    def __init__(self):
        self.apps = []

    def ret(self):
        return self.options_menu
    def run(data):
        configFile.hideConfigOption()
        with st.sidebar:
            selected = styles.styleSettings() 
        try:
            configFile.options_menu()[selected].app(data)
        except:
            pass
        #EDA.plots(data)
if __name__ == '__main__':
    f = pd.read_csv(f"chances.csv")
    mainApp.run(f)
    data_file = "recommendation.csv"