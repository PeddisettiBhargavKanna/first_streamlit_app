import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣Omega 3 & Blueberry OatMeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard Boiled Free-Rang Egg')
streamlit.text('🥑🍞Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

#Let's put a pickup list here so they can pick the fruit they want to include

streamlit.multiselect("pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

#display the table top of the page
streamlit.dataframe(my_fruit_list)
