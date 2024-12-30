
import pandas
import matplotlib.pyplot as plt
import seaborn as sns
season_avgdata = pandas.read_csv('../csv_files/season_data.csv')
# sns.lineplot(x="season",y="us_viewers",data=season_avgdata,)
# sns.lineplot(x="season",y="total_votes",data=season_avgdata,)
sns.lineplot(x="season",y="imdb_rating",data=season_avgdata,)
plt.show()