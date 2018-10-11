#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Fri Sep 28 14:53:13 2018

@author: Shush_000
"""

from .otdel import Otdel
import cgi
  
     
form = cgi.FieldStorage()
def main(q, selfurl):
#    work = Otdel(q, selfurl)

    print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Laba2</title>
        </head>
        <body>""")

    print("""</body>
        </html>""")

        
if __name__ == '__main__':
    main()
