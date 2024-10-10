import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.subheader("WordCloud App")


text = st.text_input("Enter text and press Enter:")

if text:
    w = WordCloud().generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(w, interpolation='bilinear')
    plt.axis("off")
    
    st.pyplot(plt.gcf())
