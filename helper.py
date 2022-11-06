import streamlit as st

def defaultConfig(pagesize:int=0):
    if pagesize == 0:
        st.set_page_config(layout="wide")
    elif pagesize == 1:
        st.set_page_config(layout="centered")
        
    hide_st_style = """
                <style>
                MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)