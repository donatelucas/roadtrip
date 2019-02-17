
import Location
import ApiKey
import MapInterface
from flask import Flask, jsonify, request


app = Flask(__name__)

if __name__ == "__main__":
    app.run(port=8000)

'''
so far useless...
'''
@app.route("/")
def hello():
    return "this is the home route"




'''
return sample data set of all local landmarks for user to choose
'''
@app.route("/landmarks")
def getLandmarks():
    #TODO: return list of all local landmarks on the map
    ApiKey.ApiKey.getInstance();
    return Location.getLatLong("white house")




'''
when user enters a new trip it posts to this route. the request.data should have a json object with a place property
that can be used to search for the landmark.
'''
@app.route("/tripdetails", methods = ['POST'])
def getTrip():
    #TODO: Replace print with processing to get the landmark data from google geocoder
    print(request.data) 




'''
sends the map from mapbox to the client.
'''
@app.route('/loadmap', methods =['GET'])
def getMap():
    #TODO: return the map object from mapbox possibly html text
    return MapInterface.getMap()




'''
returns the car metrics with provided options{odometer,location,both} get will return all available
'''
@app.route('/carmetrics', methods = ['GET','POST'])
def getMetrics():

    if request.method == 'POST':
        vInfo, vOdo = metricsFromSmartcar.run()
         
    else:
        vInfo, vOdo = metricsFromSmartcar.run()
    return vInfo, vOdo
