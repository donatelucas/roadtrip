import googlemaps
from flask import Flask, jsonify, request




def getLatLong(loc_name):
    gmaps = googlemaps.Client(key='AIzaSyBdyzbEUZAr6E1WZ3dWA-UQg5M5jVOEJ2s')
    coordinates = gmaps.geocode(loc_name)
    print(coordinates[0]["formatted_address"])
    return jsonify(name = coordinates[0]["formatted_address"], position = coordinates[0]["geometry"]["location"])
    #return jsonify(name=coordinates)




