import googlemaps
import ApiKey
from flask import Flask, jsonify, request


googleAcess = ApiKey.ApiKey.getInstance();

def getLatLong(loc_name):
    gmaps = googlemaps.Client(key=googleAcess.getKey('GoogleKey'))
    coordinates = gmaps.geocode(loc_name)
    print(coordinates[0]["formatted_address"])
    return jsonify(name = coordinates[0]["formatted_address"], position = coordinates[0]["geometry"]["location"])
    #return jsonify(name=coordinates)




