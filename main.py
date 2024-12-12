import streamlit as st
from streamlit_option_menu import option_menu
import home, account, about
st.set_page_config(
    page_title="fitness tracker",
)
image=st.sidebar.image('f.jpg',use_container_width=True,channels="RGB")
class multiapp:
    def __init__(self):
        self.apps = []

    def add_app(self,title,function):
        self.apps.append({"title":title,"function":function})

    def run():
        with st.sidebar:
            app=option_menu(
                menu_title='fitness tracker',
                options=['Home','Account','about'],
                icons=['house-fill','person-circle','info-circle-fill'],
                menu_icon='gym-equpment',
                default_index=1,
                styles={"container":{"padding":"5!important","background-colour":"black"},
                        "icon":{"color":"white","font-size":"23px"},
                        "nav-link":{"color":"white","font-size":"20px","text-aline":"left","margin":"0px","--hover-color":"blue"},
                        "nav-link-selected":{"background-color":"#02ab21"},}        
                )    

        if app== 'Home':
            home.app()
        if app== 'Account':
            account.app()
        if app== 'about':
            about.app()
    run()                        
