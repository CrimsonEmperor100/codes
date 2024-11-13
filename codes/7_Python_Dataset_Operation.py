#7 ---- Perform the following operations using Python on any open source -iris , titanic.csv
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.datasets import load_iris
from scipy import stats

iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['species'] = iris.target_names[iris.target]

print("Step 1: Initial Data")
print(data.head())
print(data.info())
print("\n")

print("Step 2: Summary Statistics")
print(data.describe())
print("\n")

print("Step 3: Missing Values")
print(data.isnull().sum())
print("\n")

data.fillna(method='ffill', inplace=True)
print("After handling missing values (using forward fill):")
print(data.isnull().sum())
print("\n")

print("Step 5: Check for Negative Values in Features")
print(data.describe())
print("\n")

imputer = SimpleImputer(strategy='mean')
data_imputed = pd.DataFrame(imputer.fit_transform(data.drop(columns=['species'])))
data_imputed.columns = data.drop(columns=['species']).columns
data_imputed['species'] = data['species']

print("Step 7: Outlier Detection")
z_scores = np.abs(stats.zscore(data_imputed.select_dtypes(include=[np.number])))
outliers = (z_scores > 3)
outlier_indices = np.where(outliers)[0]
print(f"\nOutliers detected at indices: {outlier_indices}")
print("\n")

data_no_outliers = data_imputed[~outliers.any(axis=1)]

data_no_outliers['SepalLengthCm_log'] = np.log(data_no_outliers['sepal length (cm)'] + 1)

def transform_result(stringvalue):
    if stringvalue == "setosa":
        return 1
    elif stringvalue == "versicolor":
        return 2
    else:
        return 3

data_no_outliers['species_encoded'] = data_no_outliers['species'].apply(transform_result)

scaler = MinMaxScaler()
features_to_normalize = data_no_outliers.drop(columns=['species', 'species_encoded', 'SepalLengthCm_log'])
data_no_outliers_normalized = data_no_outliers.copy()
data_no_outliers_normalized[features_to_normalize.columns] = scaler.fit_transform(features_to_normalize)

print("Step 11: Final Data with Encoded Species and Normalized Features")
print(data_no_outliers_normalized.head())
print("\n")

print("Step 12: Summary of Final Data")
print(data_no_outliers_normalized.describe())




# #Titanic_csv

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.preprocessing import StandardScaler, LabelEncoder
# from scipy import stats

# data = pd.read_csv("Titanic-Dataset.csv")

# print(data.info())       
# print(data.describe())   

# print("\nMissing Values in Each Column:\n", data.isnull().sum())

# data['Age'].fillna(data['Age'].median(), inplace=True)
# data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
# data.drop(columns=['Cabin'], inplace=True)

# plt.figure(figsize=(8, 5))
# sns.boxplot(x=data['Fare'])
# plt.title("Box Plot of Fare (Before Outlier Removal)")
# plt.show()

# Q1 = data['Fare'].quantile(0.25)
# Q3 = data['Fare'].quantile(0.75)
# IQR = Q3 - Q1

# data = data[(data['Fare'] >= (Q1 - 1.5 * IQR)) & (data['Fare'] <= (Q3 + 1.5 * IQR))]

# plt.figure(figsize=(8, 5))
# sns.boxplot(x=data['Fare'])
# plt.title("Box Plot of Fare (After Outlier Removal)")
# plt.show()

# scaler = StandardScaler()
# data['Fare_scaled'] = scaler.fit_transform(data[['Fare']])

# data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# label_encoder = LabelEncoder()
# data['Sex'] = label_encoder.fit_transform(data['Sex'])

# print("\nProcessed Data Preview:\n", data.head())

