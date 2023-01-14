# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:10:44 2021

@author: saba naderi
"""
class CommonConstants:
    
    MAXIMUM_CACHE_ELEMENT_CAPACITY = 3
    CACHE_EXPIRY_IN_SECONDS = 3600    

class EvictionPolicy:
    
    REJECT = 1
    OLDEST_FIRST = 2    
    NEWEST_FIRST = 3
    
class HttpCode:
    
    SUCCESSFUL_REQUEST = 200    
    OBJECT_NOT_FOUND_OR_EXPIRED = 404
    SERVER_HAS_NO_STORAGE = 507