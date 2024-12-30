import streamlit as st
import pandas as pd
import plotly.express as px

vehicles_us = pd.read_csv('vehicles_us.csv', parse_dates=['date_posted'])
print(vehicles_us.head())

st.title("Vehicle Data Explorer")
st.header("Exploratory Data Analysis")

st.subheader("Price Distribution")
show_histogram = st.checkbox("Show Price Histogram")
if show_histogram:
    fig_histogram = px.histogram(vehicles_us, x="price", nbins=30, title="Price Distribution")
    st.plotly_chart(fig_histogram)

st.subheader("Price vs Odometer")
show_scatter = st.checkbox("Show Price vs Odometer Scatter Plot")
if show_scatter:
    fig_scatter = px.scatter(vehicles_us, x="odometer", y="price", title="Price vs Odometer")
    st.plotly_chart(fig_scatter)