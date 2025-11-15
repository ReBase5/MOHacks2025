# Here is practice for what ChatGPT says for a simple first ML model (almost all just copy and paste)
# ChatGPT is not leaving comments

# Import data frame and display the head
# target?
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
irisDataFrame = pd.DataFrame(iris.data, columns=iris.feature_names)
irisDataFrame['target'] = iris.target
irisDataFrame.head()

# split the model and dataset into train and test sets
# 

from sklearn.model_selection import train_test_split

X = irisDataFrame.drop('target', axis=1)
y = irisDataFrame['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# this is supposed to train the model

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# This is supposed to make predictions using the model

from sklearn.metrics import accuracy_score

preds = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, preds))

import matplotlib.pyplot as plt

plt.figure()        # creates a new blank figure
## There is missing data here
plt.scatter()   # scatter points
plt.xlabel("X")     # label the x-axis
plt.ylabel("y")     # label the y-axis
plt.title("Scatter Plot of Data")   # title
plt.show()          # display the plot

