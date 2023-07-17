queries_list = ['SELECT DISTINCT winner FROM table_tennis_table', 
                'SELECT DISTINCT winner FROM table_tennis_table WHERE date_of_match = \'17/07/2023\'',
                'SELECT loser, COUNT() FROM table_tennis_table GROUP BY loser',
                'SELECT winner, COUNT() FROM table_tennis_table GROUP BY winner',
                'SELECT winner, COUNT(CASE WHEN did_the_winner_have_his_own_bat = \'Yes\' THEN 1 END) FROM table_tennis_table GROUP BY winner',
                'SELECT did_the_winner_have_his_own_bat, COUNT() FROM table_tennis_table GROUP BY did_the_winner_have_his_own_bat']