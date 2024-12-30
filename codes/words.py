import wordcloud
# 读取文本
with open("../csv_files/words.csv",
          encoding="utf-8") as f:
    s = f.read()
wc=wordcloud.WordCloud(width=1000,height=700,
background_color='white',max_words=100)
wc.generate(s) # 加载词云文本
wc.to_file("word_cloud_result.png")