from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

# Setting random seed
np.random.seed(0)

# Creating an object called iris with the iris data
iris = load_iris()

# Creating a dataframe with the four feature variables
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Viewing the top 5 rows
df.head()

# Adding a new column for the species name
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
# iris.target: numerical value for species, such as 0 - setosa, 1 - versicolor, and 2 - virginica
# iris.target_names: 'setosa', 'versicolor', 'virginica'

# Viewing the top 5 rows
df.head()

# Creating Training Dataset by random number if it is less than 0.75, and the rest of them will be in Test Dataset
df['is_train'] = np.random.uniform(0, 1, len(df)) <= 0.75

# Viewing the top 5 rows
df.head()

# Creating dataframes with test rows and training rows
train, test = df[df['is_train'] == True] , df[df['is_train'] == False]

# Show the number of observations for the test and training dataframes
print('Number of observations in the training data:', len(train))
print('Number of observations in the test data:', len(test))
# df.shape
# print(df)

# Creating a list of the feature column's names
features = df.columns[:4]

# Viewing features
features

# Converting each species name into digits
y = pd.factorize(train['species'])[0]

# Viewing target
y