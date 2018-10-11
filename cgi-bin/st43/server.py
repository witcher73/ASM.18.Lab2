# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 09:50:24 2018

@author: Shush_000
"""
#запускаем сервер
from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()