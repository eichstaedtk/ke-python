import numpy as np
import pandas as pd
from collections import Counter
from sklearn import datasets

# Daten einlesen
iris = datasets.load_iris()
data = iris.data
label = iris.target


def distance(instance1, instance2):
    """ Calculates the Eucledian distance between two instances"""
    return np.linalg.norm(np.subtract(instance1, instance2))


def get_neighbors(training_set,
                  labels,
                  test_instance,
                  k,
                  distancefunc):
    distances = []
    for index in range(len(training_set)):
        dist = distancefunc(test_instance, training_set[index])
        distances.append((training_set[index], dist, labels[index]))
    distances.sort(key=lambda x: x[1])
    neighbors = distances[:k]
    return neighbors


def vote(neighbors):
    class_counter = Counter()
    for neighbor in neighbors:
        class_counter[neighbor[2]] += 1
    return class_counter.most_common(1)[0][0]


# 1 Example for Testing
iris_versicolor = [7.0, 3.2, 4.7, 1.4]
# 0 Example for Testing
iris_setosa = [5.1, 3.5, 1.4, 0.2]
# 2 Example for Testing
iris_virginica = [6.3, 3.3, 6.0, 2.5]

# Exercise Value
iris_example = [4.8, 2.5, 5.3, 2.4]

irisValues = get_neighbors(data, label, iris_example, 150, distancefunc=distance)

# Aggregate
print(np.max(vote(irisValues[0:10])))

