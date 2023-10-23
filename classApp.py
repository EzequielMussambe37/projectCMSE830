
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np
import math
from utilities import configFile,menu

class mainApp:

    def __init__(self):
        self.apps = []

    def ret(self):
        return self.options_menu
    def run():
        configFile.hideConfigOption()
        with st.sidebar:
            selected = menu.menuSettings() 
        try:
            configFile.options_menu()[selected].app()
        except:
            pass

if __name__ == '__main__':
    mainApp.run()
    data_file = "recommendation.csv"