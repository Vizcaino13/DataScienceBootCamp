import pandas as pd
from sklearn.datasets import load_iris
import pickle #is used for serializing and deserializing Python objects.

# Load dataset
#The dataset contains information about iris flowers, including features like sepal length, sepal width, petal length, petal width, and the species they belong to
iris = load_iris()

data = pd.DataFrame({
    'sepal length': iris.data[:, 0],
    'sepal width': iris.data[:, 1],
    'petal length': iris.data[:, 2],
    'petal width': iris.data[:, 3],
    'species': iris.target
})


#spliting the data nto traininf testing sets
from sklearn.model_selection import train_test_split

X = data[['sepal length', 'sepal width', 'petal length', 'petal width']]
y = data['species']  # 0 'setosa', 1 'versicolor', 2 'virginica'

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

#creating the model 

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(X_train, y_train)
pickle.dump(regressor, open("model2.pkl", 'wb')) #pickle.dump is a method in Python's pickle module that is used to serialize (convert to a binary representation) and save a Python object into a file.
#It opens a file called "model2.pkl" for writing in binary mode ('wb'). The 'w' indicates write mode, and the 'b' indicates binary mode. Binary mode is necessary when working with pickle because it deals with binary data.
y_pred = regressor.predict(X_test)
