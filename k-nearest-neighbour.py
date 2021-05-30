import pandas as pd
import numpy as np
from collections import Counter


# Normalize
def normalize(value, minimum, maximum):
    return (value-minimum) / (maximum-minimum)


# Euclidian Distance
def distance(instance1, instance2):
    return np.linalg.norm(np.subtract(instance1, instance2))


def get_neighbors(training_set,
                  labels,
                  test_instance,
                  k, distancefunc):
    distances = []
    for index in range(len(training_set)):
        dist = distancefunc(test_instance, training_set[index])
        distances.append([dist, labels[index]])
    neighbors = distances[:k]
    return neighbors


def vote(neighbors):
    class_counter = Counter()
    for neighbor in neighbors:
        class_counter[neighbor[1]] += 1
    return class_counter.most_common(1)[0][0]


# Daten einlesen und Vorbereiten
df = pd.read_csv("fruit.csv", delimiter=";")
labelsFruit = df['fruit_label']
minMass, minColor = np.min(df[["mass", "color_score"]])
maxMass, maxColor = np.max(df[["mass", "color_score"]])
massNorm = normalize(df['mass'], minMass, maxMass)
colorNorm = normalize(df['color_score'], minColor, maxColor)
normValues = np.column_stack((massNorm, colorNorm))

# Calculate Distance
apple = [[normalize(190, minMass, maxMass), normalize(0.55, minColor, maxColor)]]
orange = [[normalize(150, minMass, maxMass), normalize(0.75, minColor, maxColor)]]
lemmon = [[normalize(170, minMass, maxMass), normalize(0.72, minColor, maxColor)]]

fruitNeighbours = get_neighbors(normValues, labelsFruit, lemmon, 60, distancefunc=distance)

# Sort
fruitNeighboursSorted = sorted(fruitNeighbours)

# Aggregate
vote = vote(fruitNeighboursSorted[0:10])

# Take Max to find Class
print(np.max(vote))

