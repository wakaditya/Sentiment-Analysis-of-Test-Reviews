from pyspark import SparkContext
from pyspark.sql import *

sc = SparkContext()
sqlContext = SQLContext(sc)

df = sc.textFile("C:\\Users\\wakad\\PycharmProjects\\cloudera\\BX-Book-Ratings.csv")
df.top(2)
