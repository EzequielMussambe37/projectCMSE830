
from streamlit_option_menu import option_menu


def menuSettings():
    
    selected = option_menu(
                menu_title = None,
<<<<<<< HEAD
                options=["Overview","Portofolio","EDA","Regression Analysis"],
=======
                options=["Overview","EDA","Conclusion","Regression Analysis"],
>>>>>>> 68edb3d71d4ec23bdeae3ec1ed746fc660444114
                icons=["house","📊","💻"," "],
                menu_icon = None,
                default_index=0,
                orientation="horizontal",
                styles= {
                    "container":{"padding":"4!import","background-color":"lightgrey"},
                                    "icon":{"color":'black',"font-size":'23px'},
                                    "nav-link":{"color":'black',"font-size":'20px',"text-align":'left',"margin":'0px',"--hover-color":'blue'},
                                    "nav-link-selected":{"background-color":'green'}
            },)
    return selected
