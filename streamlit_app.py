import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣Omega 3 & Blueberry OatMeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard Boiled Free-Rang Egg')
streamlit.text('🥑🍞Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

#Let's put a pickup list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table top of the page
streamlit.dataframe(fruits_to_show)

#New section to display fruityvice api response

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('what fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("please select a fruit to get information.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
expect URLError as e:
  streamlit.error()

streamlit.stop()

#import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The Fruit Load List Contains:")
streamlit.dataframe(my_data_row)

add_my_fruit = streamlit.text_input('what fruit would you like to add', 'jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
