import sys
from pyspark import SparkContext, SparkConf
import collections

if __name__ == "__main__":
    # create Spark context with necessary configuration
    sc = SparkContext("local", "PySpark Word Count Exmaple")

    # read data from text file and split each line into words
    words = sc.textFile("/Users/konrad/Sourcecode/ke-python/t8.shakespeare.txt").map( lambda x: x.replace(',',' ').replace('.',' ').replace('-',' ').lower())

    # count the occurrence of each word
    counts = words.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b)

    # save the counts to output
    sorted_counts = counts.sortBy(lambda wordCounts: wordCounts[1], ascending=False)
    # the #24 most used word in Shakespeares writings
    # the first one is not a word
    i = 0
    for word, count in sorted_counts.collect()[0:25]:
        print("{} : {} : {} ".format(i, word, count))
        i += 1


