from flask import Flask, render_template, request
from py_REDcap import getValues
from createModifySpreadsheet import *
from Google import *

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
   return "-1"

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
   CLIENT_SECRET_FILE = 'client_secret.json'
   API_NAME = 'sheets'
   API_VERSION = 'v4'
   SCOPES = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive.metadata.readonly']

   return signInGoogle(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

@app.route('/signOutGoogle', methods = ['POST'])
def signOutGoogleRequest():
   if(request.json):
      if(request.json["creds"]):
         return signOutGoogle(request.json["creds"])
   return "-1"

@app.route('/pullData') 
def pullData():
    return getValues()
if __name__ == '__main__':
   app.run(debug =True)