



# pip install --upgrade threadpoolctl
# conda update scikit-learn
# conda update --all



 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("sales_data_sample.csv", encoding='ISO-8859-1')

if df is None:
    print("Error loading dataset.")
else:
    print("Dataset loaded successfully.")
    print(df.head())  # Display first few rows of the dataset

df_cleaned = df[['SALES', 'QUANTITYORDERED', 'PRICEEACH', 'MSRP']]

# Ensure the dataframe is not empty after dropping NaN values
df_cleaned.dropna(inplace=True)
if df_cleaned.empty:
    print("The cleaned dataframe is empty after dropping rows with missing values.")
else:
    print(df_cleaned.head())  # Display first few rows of the cleaned dataset

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_cleaned)

wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(df_scaled)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of clusters (k)')
plt.ylabel('WCSS')
plt.show()

optimal_k = 4

kmeans = KMeans(n_clusters=optimal_k, init='k-means++', max_iter=300, n_init=10, random_state=42)
y_kmeans = kmeans.fit_predict(df_scaled)

df_cleaned['Cluster'] = y_kmeans

plt.figure(figsize=(10, 8))
plt.scatter(df_cleaned['SALES'], df_cleaned['MSRP'], c=df_cleaned['Cluster'], cmap='viridis')
plt.title(f'KMeans Clustering (k={optimal_k})')
plt.xlabel('Sales')
plt.ylabel('MSRP')
plt.show()

cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
print(f'Cluster centers (scaled to original data):\n {cluster_centers}')

new_data_point = np.array([[500, 10, 300, 2500]])
new_data_point_scaled = scaler.transform(new_data_point)
predicted_cluster = kmeans.predict(new_data_point_scaled)
print(f"The new data point belongs to cluster {predicted_cluster[0]}")


