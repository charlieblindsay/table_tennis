import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

from queries import queries_list
from questions import question_list

from file_paths import sql_path, raw_data_path

conn = sqlite3.connect('data/sql/database')
c = conn.cursor()

question_number = st.radio(label = 'Choose Question Number', options = [1, 2, 3, 4, 5], index=0)
query_list_index = question_number - 1
st.subheader(f'Question: {question_list[query_list_index]}')

SQL_query = st.text_area('Enter your SQL query', value=queries_list[query_list_index])

c.execute(SQL_query)

dict_list = []
name_list = []
value_list = []

matches = c.fetchall()
for match in matches:
    dict = {}
    for i in range(len(match)):
        dict[i] = match[i]
    dict_list.append(dict)
    if question_number > 1:
        name_list.append(match[0])
        value_list.append(match[1])

zipped = list(zip(name_list, value_list))
df_names_values = pd.DataFrame(zipped, columns=['Name', 'Value'])

if question_number > 1:

    visualization_option = st.radio(label = 'Table or pie chart', options = ['Table', 'Pie Chart'], index=0)

    if visualization_option == 'Table':
        df_resulting = pd.DataFrame(dict_list)
        if len(df_resulting.columns) > 1:
            df_resulting = df_resulting.set_index(0)
        st.dataframe(df_resulting)

    if visualization_option == 'Pie Chart':
        st.subheader(f'Question: {question_list[query_list_index]}')
        fig = px.pie(df_names_values, values='Value', names='Name')
        st.plotly_chart(fig)

else:
    df_resulting = pd.DataFrame(dict_list)
    st.dataframe(df_resulting)