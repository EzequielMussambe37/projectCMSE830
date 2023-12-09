
import streamlit as st
from utilities import configFile,menu
import streamlit.components.v1 as components

class mainApp:

    def __init__(self):
        self.apps = []
        st.session_state.options = False

    def ret(self):
        return self.options_menu
    
    def run():
        configFile.hideConfigOption()
        selected = menu.menuSettings() 
        try:
            if selected == "Portofolio":
                #st.write("reachable")
                ur = "https://portfolio-em.streamlit.app/?embed=true"
                st.markdown("""<iframe src=https://portfolio-em.streamlit.app/?embed=true height=900 frameBorder=0 style="width:100%;border:none;"></iframe >""",unsafe_allow_html=True)
            else: 
                configFile.options_menu()[selected].app()
        except:
            pass

if __name__ == '__main__':
    mainApp.run()
    data_file = "recommendation.csv"