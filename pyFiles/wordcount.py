import sys
from operator import add

from pyspark.sql import SparkSession

def main():
    spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()
    # spark._jsc.hadoopConfiguration().set("fs.azure.account.key.wzwzadftutorialsav2.blob.core.windows.net", "7UYdlV42ChA2VA6y0v8JnqLS/WWB4f7J5ZPr6tUHGyhW+3KI75jZYmP/0Knsjon7L8fM32065J2hSh53ViKO4w==")

    lines = spark.read.text("wasbs://adfspark@dfcommonsa.blob.core.windows.net/pyFiles/random-wiki-article.txt").rdd.map(lambda r: r[0])
    

    counts = lines.flatMap(lambda x: x.split(' ')) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(add)
    counts.saveAsTextFile("wasbs://adfspark@dfcommonsa.blob.core.windows.net/pyFiles/wordcount.txt")

    spark.stop()

if __name__ == "__main__":
    main()