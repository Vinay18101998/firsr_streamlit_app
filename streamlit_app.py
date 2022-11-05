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

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)




fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit Load List Contains:")
streamlit.dataframe(my_data_rows)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Jackfruit')
streamlit.write('Thanks for adding ', fruit_choice)

#add_fruit=my_cur.execute("insert into fruit_load_list values('from streamlit')")
#streamlit.write('Thanks for adding ', add_fruit)

my_cur.execute("insert into fruit_load_list values('from streamlit')")
my_cur.execute("delete table fruit_load_list where fruitname='test'")
