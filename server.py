CLIENT_ID = '2b08016a-23e0-4f73-ae47-3ef630dea02c'
CLIENT_SECRET = 'b5c13475-7456-4717-b82a-5fa5a5e72e53'

from flask import Flask, request, jsonify
import smartcar
import os
import sys

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

app = Flask(__name__)

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