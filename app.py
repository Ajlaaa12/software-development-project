import streamlit as st
import pandas as pd
import plotly.express as px

vehicles_us = pd.read_csv('C:/Users/ajlam/OneDrive/Documents/GitHub/software-development-project/vehicles_us.csv', parse_dates=['date_posted'])
print(vehicles_us.head())

st.title('Vehicle Data Exploration')
st.header('Exploratory Data Analysis')

st.subheader('Price Distribution Between Manufacturers')
show_histogram = st.checkbox('Show Price Histogram')
if show_histogram:
    fig_histogram = px.histogram(vehicles_us, x='manufacturer', y='price', title='Price Distribution Between Manufacturers', histfunc='avg')
    st.plotly_chart(fig_histogram)

st.subheader('Price vs Odometer')
show_scatter = st.altair_chart('Show Price vs Odometer Scatter Plot')
if show_scatter:
    fig_scatter = px.scatter(vehicles_us, x='odometer', y='price', title='Odometer vs Price', labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)'})
    st.plotly_chart(fig_scatter)