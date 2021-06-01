import pandas as pd
import numpy as np
from collections import Counter
from math import sqrt


# Normalize
def normalize(value, minimum, maximum):
    return (value - minimum) / (maximum - minimum)


# Calculate Euclidian Distance
def euclidean_distance(value1, value2):
    edistance = 0.0
    for x, y in np.nditer([value1, value2]):
        edistance += (y - x)**2
    return sqrt(edistance)


def calculate_distance(training_set,
                       labels,
                       test_instance,
                       k, distancefunc):
    distances = []
    for index in range(len(training_set)):
        dist = distancefunc(test_instance, training_set[index])
        distances.append([dist, labels[index]])
    neighbors = distances[:k]
    return neighbors


def aggregate(neighbors):
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

fruitNeighbours = calculate_distance(normValues, labelsFruit, lemmon, 60, distancefunc=euclidean_distance)

# Sort
fruitNeighboursSorted = sorted(fruitNeighbours)

# Aggregate
vote = aggregate(fruitNeighboursSorted[0:10])

# Take Max to find Class
print(np.max(vote))

