import streamlit as st
import pandas as pd
import numpy as np
import datetime 
import mysql.connector
import os
from matplotlib import pyplot as plt

st.title("Layout")
st.text("Pada Page ini kita akan belajar mengenai cara mengatur layout halaman kita")

# Sidebar
st.sidebar.title('ini adalah sidebar')
# st.sidebar.image("../assets/tes.png")

# Tabs
st.subheader("Tabs")
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
st.divider()

# Columns
st.subheader("Columns")
col1, col2, col3 = st.columns(3)
with col1:
    st.header("A cat")
    st.text('A nice picture of a cat')
    st.image("https://static.streamlit.io/examples/cat.jpg")
    st.caption('this is a cat')
with col2:
    st.header("A dog")
    st.text('A nice picture of a dog')
    st.image("https://static.streamlit.io/examples/dog.jpg")
    st.caption('this is a dog')
with col3:
    st.header("An owl")
    st.text('A nice picture of an owl')
    st.image("https://static.streamlit.io/examples/owl.jpg")
    st.caption('this is an Owl')
st.divider()

# Container
st.subheader("Container")
with st.container(border=True):
    st.write("This is inside the container")
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")
st.divider()

# Expander
st.subheader("Expander")
with st.expander("See explanation"):
    st.write('''Expander Digunakan Untuk Menyembunyikan Konten''')
st.divider()

# Dialog
@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"