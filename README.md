# Game-of-Throne-Data-Analysis-Project
This project analyse the whole season Game-of-Thrones data including the ratings of each season,  each director as well as other data using Python and Spark.

# Environment
JDK8  
Hadoop 2.7.1  
Spark 3.2.1  
Scala 2.12.15  
Python 3.8  
Pandas 1.3.5  
matplotlib 3.2.2  
word cloud 1.5.0  
seaborn 0.11.2  

# Datasets
Stored in Datasets folder. There are two csv files including data about episode, ratings and episode summary description, respectively.

# Analysis Part

## Pre-processing
Firstly we read the files and use parse_dates parameter is to format data type.We notice that there are same columns in two files. So we decide to merge them into one file based on title and publish date. Then we ouput the newly merged file.

We put the merged file into hadoop directory, start the hdfs `./sbin/start-dfs.sh` and put the file into hdfs `./bin/hdfs dfs -put game_of_thrones.csv /user/james/data`.




