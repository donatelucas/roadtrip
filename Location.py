import googlemaps
from flask import Flask, jsonify, request



def getLatLong(loc_name):
    gmaps = googlemaps.Client(key='AIzaSyBdyzbEUZAr6E1WZ3dWA-UQg5M5jVOEJ2s')
    coordinates = gmaps.geocode(loc_name)
    c = str(coordinates)
    start = c.find("'lat'")
    end = c.find('}', start, start+50)
    new = c[start:end]
    return jsonify(name = "L&L", position = new)


test = getLatLong("White house")
print (test)


