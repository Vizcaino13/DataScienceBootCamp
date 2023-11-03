import requests #This line imports the requests library, which is commonly used in Python for making HTTP requests to web services or APIs

#url = 'http://127.0.0.1:5000/add'
#myobj = {'a': 2,'b': 4}

#x = requests.post(url,json=myobj)

#print(x.text)

url = 'http://127.0.0.1:5000/iris' #specify the URL of the API endpoint you want to send the POST request to
myobj = {'a': 2,'b': 4,'c': 2,'d': 4} #this contains the input data you want to send to the API. The keys 'a', 'b', 'c', and 'd' correspond to the features that the machine learning model expects as input for making predictions. 
# when you run calling_endpoint.py script, it sends the feature values in the myobj(features of the flower  to predict) dictionary to the API, and the API responds with a prediction of the flower species based on those input features
x = requests.post(url,json=myobj) #function sends a POST request to the specified URL (in this case, the /iris route of your API) and includes the data from the myobj dictionary in JSON format as the request body

print(x.text) #This line prints the content of the response received from the API. 



 # calling_endpoint.py script is used to send a POST request to a Flask web application serving a machine learning model through an API. 
 # It provides input data for the model and then prints the response from the API.