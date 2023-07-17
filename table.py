import pandas as pd
import streamlit as st

from pathlib import Path

from file_paths import raw_data_path

st.title('Table Tennis Table')

df_table_tennis = pd.read_csv(raw_data_path / 'table_tennis_table.csv')

st.dataframe(df_table_tennis)
