
from streamlit_option_menu import option_menu


def styleSettings():

    selected = option_menu(
                menu_title = None,
                options=["Overview","EDA", "Dynamic EDA","Regression Analysis"],
                icons=["house","",""],
                menu_icon = None,
                default_index=0,
                #orientation="horizontal",
                styles= {
                    "container":{"padding":"4!import","background-color":"lightgrey"},
                                    "icon":{"color":'black',"font-size":'23px'},
                                    "nav-link":{"color":'black',"font-size":'20px',"text-align":'left',"margin":'0px',"--hover-color":'blue'},
                                    "nav-link-selected":{"background-color":'green'}
            },)
    return selected
