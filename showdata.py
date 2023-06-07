from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from getdata import get_data, urls

spark = SparkSession.builder.getOrCreate()

data = {}

for k,v in urls.items():
    data[k] = get_data(v)
    
df1 = spark.createDataFrame(data["PC-Key"])
df2 = spark.createDataFrame(data["App-Key"])
df3 = spark.createDataFrame(data["Rating-key"])
df4 = spark.createDataFrame(data["councilor-key"])

df1.show(5)
df2.show(5)
df3.show(5)
df4.show(5)

spark.stop()
