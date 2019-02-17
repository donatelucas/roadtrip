from flask import Flask, jsonify, request
import requests
import ApiKey

KEY = ApiKey.ApiKey.getInstance()
URL = "https://api.mapbox.com/v4/mapbox.mapbox-streets-v8/1/0/0.mvt?access_token=" + KEY.getKey('MapboxKey')

def getMap():
    req = requests
    data = req.get(URL)
    return data.content()
