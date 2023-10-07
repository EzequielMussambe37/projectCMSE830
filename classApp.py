
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np
import math
from utilities import configFile,styles



simple_plot_List = ["pairplot", "histgram","barplot","violinplot","boxplot"]

advance_plot_list = []
class mainApp:

    def __init__(self):
        self.apps = []
    def run():
        configFile.hideConfigOption()
        with st.sidebar:
           selected = styles.styleSettings() 
        st.write(selected)


if __name__ == '__main__':
    
    mainApp.run()
    data_file = "recommendation.csv"