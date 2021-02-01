# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 11:59:02 2021

@author: themo
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"

if __name__ == "__main__":
    app.run()