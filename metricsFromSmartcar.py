import smartcar
from flask import Flask, redirect, request, jsonify
from flask_cors import CORS

import os

def run():
    app = Flask(__name__)
    CORS(app)

    # global variable to save our access_token
    access = None

    client = smartcar.AuthClient(
        client_id=os.environ.get('CLIENT_ID'),
        client_secret=os.environ.get('CLIENT_SECRET'),
        redirect_uri=os.environ.get('REDIRECT_URI'),
        scope=['read_vehicle_info', 'read_odometer'],
        test_mode=True,

    )

    if __name__ == '__main__':
    app.run(port=8000)


@app.route('/login', methods=['GET'])
def login():


    auth_url = client.get_auth_url()
    return redirect(auth_url)


@app.route('/exchange', methods=['GET'])
def exchange():
    code = request.args.get('code')
    global access
    access = client.exchange_code(code)
    
    return redirect('http://localhost:8000/vehicle"')




@app.route('/vehicle', methods=['GET'])
def vehicle():
    global access
    vehicle_ids = smartcar.get_vehicle_ids(access['access_token'])['vehicles']

    vehicle = smartcar.Vehicle(vehicle_ids[0], access['access_token'])
    info = vehicle.info()
    print(info)

    response = vehicle.odometer()
    print(response)
    
    return jsonify(info), jsonify(response)



