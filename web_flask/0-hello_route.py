#!/usr/bin/python3
  2 """ a script that starts a Flask web application """
  3 from flask import Flask
  4 
  5 app = Flask('web_flask')
  6 
  7 @app.route('/', strict_slashes=False)
  8 def home():
  9         return 'Hello HBNB!'
 10 
 11 if __name__ == "__main__":
 12         app.run(host="0.0.0.0.", port=5000)
