import wordcloud
import pandas
import matplotlib.pyplot as plt
import seaborn as sns
# 读取文本
with open("./words.csv",encoding="utf-8") as f:
    s = f.read()
wc=wordcloud.WordCloud(width=1000,height=700,background_color='white',max_words=100)
wc.generate(s) # 加载词云文本
wc.to_file("word_cloud_result.png") # 保存词云文件

season_avgdata = pandas.read_csv('./season_avgdata.csv')
sns.lineplot(x="season", y="avg(us_viewers)", data=season_avgdata)
plt.show()
director_avgdata = pandas.read_csv('director_avgdata.csv')
sns.barplot(x='directed_by',y= 'avg(imdb_rating)',data=director_avgdata)
plt.show()
director_countdata = pandas.read_csv('./director_countdata.csv')
plt.pie(x=director_countdata['count'], labels=director_countdata['directed_by'])
plt.show()
writer_countdata = pandas.read_csv('./writer_countdata.csv')
plt.pie(x=writer_countdata['count'], labels=writer_countdata['written_by'])

plt.show()