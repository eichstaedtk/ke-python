import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('edlich-kmeans.csv', skiprows=1)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(dataset.to_numpy())
    wcss.append(kmeans.inertia_)


plt.figure(figsize=(10,5))
sns.lineplot(range(1, 11), wcss,marker='o', color='red')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(dataset.to_numpy())

x = dataset.to_numpy()

fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x[y_kmeans == 0,0],x[y_kmeans == 0,1],x[y_kmeans == 0,2], s = 40 , color = 'blue', label = "cluster 1")
ax.scatter(x[y_kmeans == 1,0],x[y_kmeans == 1,1],x[y_kmeans == 1,2], s = 40 , color = 'orange', label = "cluster 2")
ax.scatter(x[y_kmeans == 2,0],x[y_kmeans == 2,1],x[y_kmeans == 2,2], s = 40 , color = 'green', label = "cluster 3")
ax.scatter(x[y_kmeans == 3,0],x[y_kmeans == 3,1],x[y_kmeans == 3,2], s = 40 , color = '#D12B60', label = "cluster 4")
ax.scatter(x[y_kmeans == 4,0],x[y_kmeans == 4,1],x[y_kmeans == 4,2], s = 40 , color = 'purple', label = "cluster 5")
ax.set_xlabel('V1')
ax.set_ylabel('V2')
ax.set_zlabel('V3')
ax.legend()
plt.show()

