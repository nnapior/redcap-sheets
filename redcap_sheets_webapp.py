from flask import Flask, render_template, request, flash, redirect, url_for
from py_REDcap import getValues
from createModifySpreadsheet import *
from redcapImport import import_redcap

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/scripts.js')
def getScripts():
   with open("scripts.js", "r") as f:
      return f.read()

@app.route('/')
def hello_world():
   return  render_template('homepage.html')

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

@app.route('/pullData') 
def pullData():
    return getValues()

@app.route('/import')
def import_to_redcap():
    response = import_redcap()
    for item in response:
        flash(item)
    return redirect(url_for("hello_world"))
if __name__ == '__main__':
   app.run(debug =True)