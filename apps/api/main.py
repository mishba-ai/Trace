from flask import Flask
from api.app.config import app 

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"