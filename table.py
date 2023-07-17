import pandas as pd
import streamlit as st

from pathlib import Path

sql_path = Path.cwd() / 'data/SQL'

raw_data_path = Path.cwd() / 'data/raw'

st.title('Table Tennis Table')

df_table_tennis = pd.read_csv(raw_data_path / 'table_tennis_table.csv')

st.dataframe(df_table_tennis)
