
import pandas
import seaborn as sns
import matplotlib.pyplot as plt
director_avgdata = pandas.read_csv\
    ('../csv_files/director_data.csv')
sns.barplot(x="avg(imdb_rating)",y="directed_by",
            data=director_avgdata)
plt.show()