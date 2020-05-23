import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


DATA_URL = ("C:/Users/Divya/gainers.csv")
DATA_UR= ("C:/Users/Divya/losers.csv")
df=pd.read_csv(DATA_URL)
df1=pd.read_csv(DATA_UR)

st.title("Share Price analysis for May 2019 to May 2020:")
st.sidebar.title("Share Price analysis for May 2019 to May 2020:")
st.markdown("This application is a Share Price dashboard for Top 5 Gainers and Losers:")
st.sidebar.markdown("This application is a Share Price dashboard for Top 5 Gainers and Losers:")


st.sidebar.title("Gainers")
select = st.sidebar.selectbox('Share', ['Adani Green Energy', 'GMM Pfaudler', 'AGC Networks', 'Alkyl Amines Chem', 'IOL Chem & Pharma'], key='1')
if not st.sidebar.checkbox("Hide", True, key='1'):
    st.title("Gainers")
    if select == 'Adani Green Energy':
        fig = go.Figure(data=[go.Candlestick(x=df['AdaDate'], open=df[' AdaOpen '], high=df[' AdaHigh '], low=df[' AdaLow '], close=df[' AdaClose '])])
        st.plotly_chart(fig)
    elif select=='GMM Pfaudler':
        fig = go.Figure(data=[go.Candlestick(x=df['GmmDate'], open=df[' GmmOpen '], high=df[' GmmHigh '], low=df[' GmmLow '], close=df[' GmmClose '])])
        st.plotly_chart(fig)
    elif select == 'AGC Networks':
        fig = go.Figure(data=[go.Candlestick(x=df['AgcDate'], open=df[' AgcOpen '], high=df[' AgcHigh '], low=df[' AgcLow '], close=df[' AgcClose '])])
        st.plotly_chart(fig)
    elif select=='Alkyl Amines Chem':
        fig = go.Figure(data=[go.Candlestick(x=df['AlkDate'], open=df[' AlkOpen '], high=df[' AlkHigh '], low=df[' AlkLow '], close=df[' AlkClose '])])
        st.plotly_chart(fig)
    else:
        fig = go.Figure(data=[go.Candlestick(x=df['IolDate'], open=df[' IolOpen '], high=df[' IolHigh '], low=df[' IolLow '], close=df[' IolClose '])])
        st.plotly_chart(fig)



st.sidebar.title("Losers")
select = st.sidebar.selectbox('Share', ['Indiabulls Housing', 'YES Bank', 'Indusind Bank', 'GAIL India', 'HDFC Bank'], key='2')
if not st.sidebar.checkbox("Hide", True, key='2'):
    st.title("Losers")
    if select == 'Indiabulls Housing':
        fig = go.Figure(data=[go.Candlestick(x=df1['IBDate'], open=df1[' IBOpen '], high=df1[' IBHigh '], low=df1[' IBLow '], close=df1[' IBClose '])])
        st.plotly_chart(fig)
    elif select=='YES Bank':
        fig = go.Figure(data=[go.Candlestick(x=df1['YEDate'], open=df1[' YEOpen '], high=df1[' YEHigh '], low=df1[' YELow '], close=df1[' YEClose '])])
        st.plotly_chart(fig)
    elif select == 'Indusind Bank':
        fig = go.Figure(data=[go.Candlestick(x=df1['INDate'], open=df1['INOpen'], high=df1['INHigh'], low=df1['INLow'], close=df1['INClose'])])
        st.plotly_chart(fig)
    elif select=='GAIL India':
        fig = go.Figure(data=[go.Candlestick(x=df1['GADate'], open=df1[' GAOpen '], high=df1[' GAHigh '], low=df1[' GALow '], close=df1[' GAClose '])])
        st.plotly_chart(fig)
    else:
        fig = go.Figure(data=[go.Candlestick(x=df1['HDDate'], open=df1[' HDOpen '], high=df1[' HDHigh '], low=df1[' HDLow '], close=df1[' HDClose '])])
        st.plotly_chart(fig)
