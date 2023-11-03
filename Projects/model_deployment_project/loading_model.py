from flask import Flask, request
import pickle
import numpy as np

app = Flask("yourapp")
#app = Flask(__name__)

# home route that returns below text when root url is accessed
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello")
def viewfunc():
    return "<p>Second Route</p>"

@app.route("/hello/bye")
def viewfunc1():
    return "<h1>Third Route</h1>"

@app.route("/add",methods=["POST"])
def add():
    a=request.json['a']
    b=request.json['b']
    return {"sum":int(a)+int(b)}

#this is connected to defined the features X in the iris random forest model (sepal length, sepal width, petal length, and petal width) 
# in this route, you have extracted feature values from the JSON payload, and you can pass them to your model for making predictions
@app.route("/iris",methods=["POST"]) #This is a decorator in Flask that specifies the route for the function that follows it. It defines a route named "/iris" and specifies that it should only respond to HTTP POST requests (as indicated by methods=["POST"]).
def classify(): #This defines a Python function named classify, which is associated with the "/iris" route.
    a=request.json['a'] #Extracting Data from the POST Request:
    b=request.json['b'] #This code retrieves data from the JSON body of the POST request. It assumes that the JSON body contains four key-value pairs ('a', 'b', 'c', and 'd')
    c=request.json['c'] #each corresponding to a feature used for making predictions with the machine learning model. 
    d=request.json['d']
    loaded_model = pickle.load(open("model2.pkl", 'rb')) #This line loads the machine learning model from the "model2.pkl" file using pickle.load, rb stands for read binary 
    # row,features as we have 1 row here shape is 1,features (4), NumPy array that represents the input data for making predictions with a machine learning model
    test=np.array([a,b,c,d]).reshape(1,-1) #this creates a NumPy array by passing a list [a, b, c, d] as an argument. The list contains the four feature values (a, b, c, and d) that were extracted from the JSON request, .reshape(1, -1) 1 in the first dimension indicates that you want the array to have a single row. This is typical when you want to make predictions for a single data point,  -1 in the second dimension indicates that you want NumPy to automatically determine the size of the second dimension based on the provided data. t will be automatically set to 4 because there are four feature values 
    print(test.shape) #These lines are for debugging and print the shape of the input data (which should be (1, 4)) 
    print(loaded_model.predict(test)) #is the prediction made by your machine learning model based on the feature values in the test array. 
    return {"prediction":str(loaded_model.predict(test)[0])} #The prediction result is printed to the console.


if __name__ == '__main__':  #This block of code ensures that the Flask application is only started if the script is executed directly (not if it's imported as a module). It starts the Flask web server so that you can access the defined routes and interact with the model.
   app.run()
