from flask import Flask, render_template, request
from py_REDcap import getValues
from createModifySpreadsheet import *

app = Flask(__name__)

@app.route('/scripts.js')
def getScripts():
   with open("scripts.js", "r") as f:
      return f.read()

@app.route('/')
def hello_world():
   """
   Function that open opening of webapp reads data from html
   """
   with open("homepage.html", "r") as f:
       read_data = f.read()
   return read_data

@app.route('/style.css')
def getStyle():
   """
   Function that retireves redcapp style for webapp
   """
   with open("style.css","r") as f:
      return f.read()
      
@app.route('/pushData', methods = ['PUT','POST'])
def pushData():
   """
   Function that pushes data from a json to webapp
   """
   if(request.json):
       return pushJSON(request.json)
   else:
       return print("-1")

@app.route('/pullData') 
def pullData():
   """
   Function that pulls data from redcap to webapp
   Returns values from redcap
   """
    return getValues()
if __name__ == '__main__':
   app.run(debug =True)