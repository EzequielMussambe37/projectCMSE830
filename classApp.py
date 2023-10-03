
import streamlit as st
simple_plot_List = ["pairplot", "histgram","barplot","violinplot","boxplot"]
'''
    colorblind. importante escolher bem,
    python tem  spetrum for colorblind...
    como mudaram as colors no python libraries tipo seaborn, matplotlib,etc...
'''
advance_plot_list = []
class mainApp(st):

    def __init__(self,username,auth,):

        self.username = username
        self.auth = auth


    def dataVisusalization(self):
        #operation to show


    def basicPlots(self,plotName):

        if plotName

