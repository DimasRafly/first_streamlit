import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def get_data():
    gaming_df_encoded = pd.read_csv('data.csv')    
    return gaming_df_encoded

# Use get_data function to support Streamlit app
gaming_df_encoded = get_data()

st.title('Game Dataset Exploration by RevoU')
st.write('To deepen my knowledge of data analytics, I participated in and completed a mini-task from a short course program organized by RevoU. The goal of this project was quite simple: to answer analytical questions with data visualization.')

st.header('The Questions')
st.write('1. Which publisher published most of the games?')
st.write('2. Which developer developed most of the games?')
st.write('3. Which series is the most sales?')
st.write('4. Which series have the most games?')

st.header('The Dataset')
st.write(gaming_df_encoded.head())

# ============================== #

# Plotting the bar chart
st.header('Number of Published Game by Publisher')

publ = gaming_df_encoded['Publisher'].value_counts(ascending=False).head()

plt.figure(figsize=(10, 6))
barplot = plt.bar(publ.index, publ.values)
plt.title('Number of Published Game by Publisher')
plt.xlabel('Publisher Name')
plt.ylabel('Number of Game')

# Bar labelling
for bar, value in zip(barplot, publ):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), round(value, 2), ha='center', va='bottom', color='black')

# Display the plot in Streamlit
st.pyplot(plt)

# ============================== #
# Plotting the bar chart
st.header('Number of Developed Games by Developer')

# Which developer developed most of the games?
devs = gaming_df_encoded['Developer'].value_counts(ascending = False).head()

plt.figure(figsize=(10,6))
barplot = plt.bar(devs.index, devs.values)
plt.title('Number of Developed Games by Developer')
plt.xlabel('Developer Name')
plt.ylabel('Number of Developed Game')

# bar labelling
bars = barplot.patches
for bar, value in zip(bars, devs):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
    round(value, 2), ha='center', va='bottom', color='black')

st.pyplot(plt)

# ============================== #

st.header('Most Profitable Series')

# Which series is the most sales?
plt.figure(figsize=(12,6))
sold_series = gaming_df_encoded.groupby('Series')['Sales'].sum()
sold_series = sold_series.nlargest()

barplot = plt.bar(sold_series.index, sold_series.values)
plt.title('Most Profitable Series')
plt.xlabel('Series Name')
plt.ylabel('Sales in Thousand $')

# bar labelling
bars = barplot.patches
for bar, value in zip(bars, sold_series):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
    round(value, 2), ha='center', va='bottom', color='black')

st.pyplot(plt)

# ============================== #

st.header('Top 5 Game Franchise')

# Which series have the most games?
series_game = gaming_df_encoded.groupby('Series')['Name'].count()
series_game = series_game.nlargest(5)
plt.figure(figsize=(12,6))

barplot = plt.bar(series_game.index, series_game.values)
plt.title('Top 5 Game Franchise')
plt.xlabel('Series Name')
plt.ylabel('Total Having Games')

# bar labelling
bars = barplot.patches
for bar, value in zip(bars, series_game):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
    round(value, 2), ha='center', va='bottom', color='black')

st.pyplot(plt)

# ============================== #

st.header('Thank You!')