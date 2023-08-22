import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit 超入門")

st.write("Display Image")
img = Image.open("ミケ.png")

# use_column_width=Trueを指定すると画面の幅によって調整するようになる。
st.image(img,caption="ミケちゃん",use_column_width=True)
