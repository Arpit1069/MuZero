import imp
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="MuZero",page_icon=":tada:",layout="wide")
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottie("https://assets7.lottiefiles.com/packages/lf20_knnirj9a.json")
# header section
with st.container():
# st.subheader("")-->medium
  st.title("MuZero")#-->large
  st.write("welcome to virtual assitant")

  with st.container():
   st.write("---")
   left_column, right_column = st.columns((1,2))
   with left_column:
    st_lottie(lottie_coding, height=300, key = "coding")