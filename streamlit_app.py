import streamlit 

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('Tuna melt sandwich 🐟🧀 ')
streamlit.text('Pain au chocolat🥐🍫')
streamlit.text('Avocado and egg toast 🥑🍞🍳')

streamlit.header('Make your own frickin smoothie🍔🍇🍊')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
