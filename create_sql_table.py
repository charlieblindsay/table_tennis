import sqlite3
import pandas as pd

from pathlib import Path

sql_path = Path.cwd() / 'data/sql'
raw_data_path = Path.cwd() / 'data/raw'

conn = sqlite3.connect(sql_path / 'database')
c = conn.cursor()

# c.execute(f'SET DATEFORMAT dmy')
c.execute(f'CREATE TABLE IF NOT EXISTS table_tennis_table (winner TEXT, loser TEXT, date_of_match DATE, did_the_winner_have_his_own_bat TEXT)')

df_table_tennis = pd.read_csv(raw_data_path / 'table_tennis_table.csv')

df_table_tennis.to_sql('table_tennis_table', conn, if_exists='replace', index=False)

conn.commit()