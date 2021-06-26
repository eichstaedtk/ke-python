from pyspark import SparkContext

if __name__ == "__main__":
    # create Spark context with necessary configuration
    sc = SparkContext("local", "PySpark Word Count Exmaple")

    shakespeare = sc.textFile("t8.shakespeare.txt").map(lambda x: x.replace(',', ' ').replace('.', ' ').replace('-', ' ').lower())

    # count the occurrence of each word
    counts = shakespeare.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b)

    sorted_counts = counts.sortBy(lambda wordCounts: wordCounts[1], ascending=False)

    i = 0
    for word, count in sorted_counts.collect()[0:25]:
        print("{} : {} : {} ".format(i, word, count))
        i += 1
