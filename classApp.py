
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
simple_plot_List = ["pairplot", "histgram","barplot","violinplot","boxplot"]

advance_plot_list = []
class mainApp(object):

    def __init__(self):
        self.page_title = "University Recommendation System"
        self.page_icon = ":money_with_wings:"
        self.layout = "centered" #centered
        st.set_page_config(self.page_title,self.layout)
        st.title(self.page_title)
        self.df = object

    def dataVisusalization(self):
        #operation to show
        pass

    def basicPlots(self,plotName):
        #show basic plots
        pass
    
    def read_dataframe(self,data):
        self.df = pd.read_csv(data)
        return self.df


if __name__ == '__main__':
    data_file = "recommendation.csv"
    app = mainApp()
    app.read_dataframe(data_file)