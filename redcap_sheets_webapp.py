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
   with open("homepage.html", "r") as f:
       read_data = f.read()
   return read_data

@app.route('/style.css')
def getStyle():
   with open("style.css","r") as f:
      return f.read()
      
@app.route('/pushData', methods = ['PUT','POST'])
def pushData():
   if(request.json):
      return pushJSON(request.json)
   else:
      return "-1"

@app.route('/pullData') 
def pullData():
    return getValues()
if __name__ == '__main__':
   app.run(debug =True)