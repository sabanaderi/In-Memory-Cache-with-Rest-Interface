# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:00:12 2021

@author: saba naderi
"""
import socket
from contextlib import closing

def isPortInUse(port):
    """ Return True if the port is already used, False otherwise. 
    """
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        return s.connect_ex(('localhost', port)) == 0
    return True

def getAnAvailablePort(preferredPort=5000):
    """ Return an available port number. """

    if not isPortInUse(preferredPort):
        return preferredPort
    
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]
