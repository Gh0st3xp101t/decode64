#coding:utf-8

#This program decode hash base64 just change range for your need interaction
#-------------------------------|
# By Gh0st_3xp10!t              |
#-------------------------------|

import base64

def decode(a):
    i = 0
    for i in range(1, 14):
            a = base64.b64decode(a)
    return a

strings = """ENTER_HASH"""
b = decode(strings)
print b
