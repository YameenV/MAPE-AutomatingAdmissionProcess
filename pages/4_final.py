import streamlit as st
from helper import defaultConfig
import requests
from streamlit_lottie import st_lottie

defaultConfig()

st.header('Welcome to Boost up your Engineering Career With Universal Collage of Engineering ')
# for welcome
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_welcome = "https://assets3.lottiefiles.com/packages/lf20_69HH48.json"
lottie_welcome = load_lottieurl(lottie_url_welcome)

st_lottie(lottie_welcome, key="welcome")