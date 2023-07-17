# winner TEXT, loser TEXT, date_of_match DATE, did_the_winner_had_his_own_bat TEXT

import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

from queries import queries_list
from questions import question_list

from file_paths import sql_path, raw_data_path

st.title('Table Tennis Table')

df_table_tennis = pd.read_csv(raw_data_path / 'table_tennis_table.csv')

st.dataframe(df_table_tennis)

