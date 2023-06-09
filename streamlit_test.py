import streamlit
import snowflake.connector  
streamlit.title('My parents new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

import requests




fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response)


fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#add_fruit_choice = input("Enter the fruit choice: ") # User-provided value
add_fruit_choice = streamlit.text_input('What fruit would you like add about?')
streamlit.write('The user entered ', add_fruit_choice)

#my_cur.execute("insert into FRUIT_LOAD_LIST  values (?)",(add_fruit_choice))
my_cur.execute("insert into FRUIT_LOAD_LIST  values ('"+ add_fruit_choice +"')")

#values ('banana')
#my_data_row = my_cur.fetchone()
#streamlit.text("fruti load list:")
#streamlit.text(my_data_row)
