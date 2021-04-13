from flask import Flask, render_template, request, flash, redirect, url_for
from py_REDcap import getValues
from createModifySpreadsheet import *
from redcapImport import import_data, getEvents
from redcapDelete import delete_records

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/scripts.js')
def getScripts():
   with open("scripts.js", "r") as f:
      return f.read()

@app.route('/')
def hello_world():
   # with open("homepage.html", "r") as f:
   #     read_data = f.read()
   # return read_data
   return render_template("homepage.html")

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
    data = getValues()
    return data

@app.route('/import_page')
def import_page():
    events = getEvents()
    return render_template("importRedcap.html", events = events)


@app.route('/import_redcap', methods = ['PUT','POST'])
def import_to_redcap():
    if request.method == "POST":
        if request.form["importMode"] == 'select':
            response = import_data(request.form.getlist("events"))
            if response == False:
                flash("Please Select Events")
            else:
                flash(response)
            return redirect(url_for("import_page"))
        elif request.form["importMode"] == "all":
            response = import_data("All Events")
            if response == False:
                flash("Please Select Events")
            else:
                flash(response)
            return redirect(url_for("import_page"))


@app.route('/delete_record', methods = ["POST"])
def delete_record():
    if request.method == "POST":
        id = request.form['participantSelection']
        response = delete_records(id)
        if response == '<?xml version="1.0" encoding="UTF-8" ?><hash><error>You do not have Delete Record privileges</error></hash>':
            flash("You donot have permission to delete records.")
            return redirect(url_for("hello_world"))
        else:
            return redirect(url_for("hello_world"))


if __name__ == '__main__':
   app.run(debug =True)