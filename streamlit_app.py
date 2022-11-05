import streamlit

streamlit.title(' My Parents new healthy diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 and blueberry Oatmeal')
streamlit.text('🥗kale,Spinach and Rocket smoothie')
streamlit.text('🐔Hard_Boiled Free_Range Egg')
streamlit.text('🥑🧇Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruit_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

