
import Location
import ApiKey
import MapInterface
import metricsFromSmartcar
import smartcar
import os
from flask import Flask, jsonify, request, redirect


app = Flask(__name__)

# global variable to save our access_token
access = None
fOdometer = None
lOdometer = None

client = smartcar.AuthClient(
    client_id='1714bcc1-e189-489f-81f1-aaf39fe89785',
    client_secret='4d17ecec-e19a-4616-baf3-ca83ad334eae',
    redirect_uri='http://localhost:5000/exchange',
    scope=['read_vehicle_info', 'read_odometer'],
    test_mode=True,

)

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


@app.route('/login', methods=['GET'])
def login():


    auth_url = client.get_auth_url()
    return redirect(auth_url)


@app.route('/exchange', methods=['GET'])
def exchange():
    code = request.args.get('code')
    global access
    access = client.exchange_code(code)
    
    return redirect('http://localhost:5000/vehicle')



@app.route('/vehicle', methods=['GET'])
def vehicle():
    global access
    vehicle_ids = smartcar.get_vehicle_ids(access['access_token'])['vehicles']

    vehicle = smartcar.Vehicle(vehicle_ids[0], access['access_token'])
    info = vehicle.info()
    #print(info)

    response = vehicle.odometer()
    #print(response)
    
    return jsonify(info, response)


'''
returns the car metrics with provided options{odometer,location,both} get will return all available
'''
'''
@app.route('/carmetrics', methods = ['GET','POST'])
def getMetrics():
    
    metricsFromSmartcar.login()
    vInfo, vOdo = metricsFromSmartcar.vehicle()
    return str(vInfo), str(vOdo)
'''
   
