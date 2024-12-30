
import pandas
episodes_data=pandas.read_csv('../csv_files/game_of_thrones_episodes.csv')
imdb_data=pandas.read_csv('../csv_files/game_of_thrones_imdb.csv', parse_dates=['original_air_date'])
imdb_data=imdb_data[['title','original_air_date','imdb_rating','total_votes', 'desc']]
total_data=episodes_data.merge(imdb_data,how='left',on=['title','original_air_date'])
total_data.to_csv('../csv_files/game_of_thrones.csv', encoding='utf8', index=False)