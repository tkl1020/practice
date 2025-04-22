# Step 1: Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 2: Generate or load sample data
# For simplicity, we will generate synthetic data with 2 features
data = {
    'Feature1': np.random.rand(100),
    'Feature2': np.random.rand(100)
}

df = pd.DataFrame(data)

# Step 3: Visualize the data (Optional, but helpful to understand the clusters)
plt.scatter(df['Feature1'], df['Feature2'])
plt.title('Generated Data')
plt.xlabel('Feature1')
plt.ylabel('Feature2')
plt.show()

# Step 4: Apply KMeans clustering
# Specify the number of clusters you want (for example, 3 clusters)
kmeans = KMeans(n_clusters=3)

# Fit the model to the data
df['Cluster'] = kmeans.fit_predict(df[['Feature1', 'Feature2']])

# Step 5: Visualize the clusters
plt.scatter(df['Feature1'], df['Feature2'], c=df['Cluster'], cmap='viridis')
plt.title('Data after KMeans Clustering')
plt.xlabel('Feature1')
plt.ylabel('Feature2')
plt.show()

# Step 6: Inspect the cluster centers
print("Cluster Centers:")
print(kmeans.cluster_centers_)

# Step 7: Use the clustered data (Optional)
# For example, we can calculate the mean of each cluster for further analysis
cluster_means = df.groupby('Cluster').mean()
print("\nMean of each cluster:")
print(cluster_means)
