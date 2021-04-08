from flask import Flask, render_template, request
from py_REDcap import getValues
from createModifySpreadsheet import *

app = Flask(__name__)

@app.route('/scripts.js')
def getScripts():
   with open("scripts.js", "r") as f:
      return f.read()

@app.route('/signin.js')
def getSignin():
   with open("signin.js", "r") as f:
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
       return print("-1")

@app.route('/renameSheet', methods = ['PUT','POST'])
def renameSheetRequest():
   if(request.json):
      if(request.json["newName"]):
         return renameSheet(request.json["newName"])
   else:
       return print("-1")

@app.route('/clearSheet', methods = ['PUT','POST'])
def clearSheetRequest():
   return cleanSheet()

@app.route('/pickSpreadsheet', methods = ['GET'])
def pickSheetRequest():
   return pickSheet()

@app.route('/authREDCap', methods = ['POST'])
def authREDCapRequest():
   return "1"

@app.route('/authGoogle', methods = ['POST'])
def authGoogleRequest():
   return "1"

@app.route('/pullData') 
def pullData():
    return getValues()
if __name__ == '__main__':
   app.run(debug =True)