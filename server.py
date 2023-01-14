# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:00:12 2021

@author: saba naderi
"""
from flask import Flask, request, jsonify
from cache.cache import Cache
from Definition import HttpCode
from Definition import CommonConstants
import util
import sys
import time

cache = Cache()

app = Flask(__name__)
PREFIX = "/object"
    
@app.route(f"{PREFIX}/<key>", methods=["GET"])
def get_from_cache(key):
    
    cache.autoCleanCahce()
    data, ttl = cache.get(key)
    
    if data:
        return jsonify(success = True, value = {'data': data, 'ttl': ttl})
    
    resp = jsonify(success=False)
    resp.status_code = HttpCode.OBJECT_NOT_FOUND_OR_EXPIRED
    return resp

@app.route(f"{PREFIX}/", methods=["POST", "PUT"])
def insert_into_cache():
    
    cache.autoCleanCahce()
    data = request.get_json(force=True)
    key  = data['key']
    obj  = data['value']
    
    if data['ttl']:
        ttl = int( time.time() ) + data['ttl'] if data['ttl'] != 0 else sys.maxint
    else:
        ttl = int( time.time() ) + CommonConstants.CACHE_EXPIRY_IN_SECONDS
    
    if cache.insert(str(key), obj, ttl):   
        return jsonify(success = True)
    
    resp = jsonify(success=False)
    resp.status_code = HttpCode.SERVER_HAS_NO_STORAGE
    return resp

@app.route(f"{PREFIX}/<key>", methods=["DELETE"])
def delete_from_cache(key):
    
    cache.autoCleanCahce()    
    if cache.remove(key):
        return jsonify(success = True)
    
    resp = jsonify(success=False)
    resp.status_code = HttpCode.OBJECT_NOT_FOUND_OR_EXPIRED
    return resp


def setup_app(app):
    app.port = util.getAnAvailablePort()    
    app.run(host = 'localhost', port = app.port)


if __name__ == "__main__":
    setup_app(app)
