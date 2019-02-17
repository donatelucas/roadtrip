
CLIENT_ID = '2b08016a-23e0-4f73-ae47-3ef630dea02c'
CLIENT_SECRET = 'b5c13475-7456-4717-b82a-5fa5a5e72e53'

from flask import Flask, request, jsonify
import smartcar
import os
import sys
import Location
import ApiKey
import MapInterface
<<<<<<< HEAD:Backend/server.py
=======
import smartcar
import os
from flask import Flask, jsonify, request, redirect
>>>>>>> apikeys:server.py


app = Flask(__name__)

<<<<<<< HEAD:Backend/server.py
# 1. Create an instance of Smartcar's client.
client = smartcar.AuthClient(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri='http://localhost:8000/callback',
    scope=[
        'read_vehicle_info',
        'read_location',
        'read_odometer',
        'control_security'
    ]
)



# 3. Create a page with a 'Connect Car' button.
@app.route('/', methods=['GET'])
def index():
    auth_url = client.get_auth_url()
    return '''
        <h1>Let's Plan a Roadtrip!</h1>
        <a href=%s>
          <button>Connect Car</button>
        </a>
    ''' % auth_url
  
  
  

# 4. On an HTTP GET to our callback will exchange our OAuth Auth Code
#    for an Access Token and log it out.
@app.route('/callback', methods=['GET'])
def callback():
    code = request.args.get('code')
    access = client.exchange_code(code)

    # Log the access token response
    print(access)

    # Respond with a success status to browser
    return jsonify(access)

# 5. Let's start up the server at port 8000.
if __name__ == '__main__':
    app.run(port=8000)
=======
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


>>>>>>> apikeys:server.py



'''
return sample data set of all local landmarks for user to choose
'''
@app.route("/landmarks")
def getLandmarks():
    #TODO: return list of all local landmarks on the map
    ApiKey.ApiKey.getInstance();
    return Location.getLatLong("tokyo")




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


<<<<<<< HEAD:Backend/server.py
'''
returns the car metrics with provided options{odometer,location,both} get will return all available
'''
@app.route('/carmetrics', methods = ['GET','POST'])
def getMetrics():
    #TODO: replace return with real data from smartcar api
    if request.method == 'POST':
         #metrics = metricsFromSmartcar(response.data.option)
         x=1; #so compiler doesnt complain
    else:
        #metrics = metricsFromSmartcar()
        x =2; #so compiler doesnt complain
    return 'metrics' #remove quotes

=======
@app.route('/exchange', methods=['GET'])
def exchange():
    code = request.args.get('code')
    global access
    access = client.exchange_code(code)
    
    return redirect('http://localhost:5000/carmetrics')



@app.route('/carmetrics', methods=['GET'])
def vehicle():
    global access
    vehicle_ids = smartcar.get_vehicle_ids(access['access_token'])['vehicles']

    vehicle = smartcar.Vehicle(vehicle_ids[0], access['access_token'])
    info = vehicle.info()
    #print(info)

    response = vehicle.odometer()
    #print(response)
    
    return jsonify(info, response)


   
>>>>>>> apikeys:server.py
