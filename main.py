import streamlit as st
from streamlit_option_menu import option_menu
import about,account,home

image=st.sidebar.image('log.png',width=200,channels="RGB")
st.set_page_config(page_title="fitness tracker")
class multiapp:
    def __init__(self):
        self.apps=[]
    def add_app(self,title,function):
        self.apps.append({"title":title,"function":function})
    def run():
        with st.sidebar:
            app=option_menu(
                menu_title='fitness tracker',
                options=['Home','Account','about'],
                icons=['house-fill','person-circle','i-circle'],
                menu_icon='gym-equpment',
                default_index=1,
                styles={"container":{"padding":"5!important","background-colour":"black"},
                        "icon":{"color":"white","font-size":"23px"},
                        "nav-link":{"color":"white","font-size":"20px","text-aline":"left"},
                        "nav-link-selected":{"background-color":"#02ab21"},}        
                )    

            if app== 'Home':
                home.app()
            if app== 'Account':
                home.account()
            if app== 'about':
                home.about()
                        
