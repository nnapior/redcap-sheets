from flask import Flask, render_template, request, flash, session, redirect, url_for
from lib.py_REDcap import getValues
from lib.createModifySpreadsheet import pushJSON, renameSheet, cleanSheet, pickSheet
from lib.py_REDcap_import import import_data
from lib.py_REDcap_delete import delete_records
from forms import SettingsForm

app = Flask(__name__)


@app.route('/scripts.js')
def getScripts():
    with open("js/scripts.js", "r") as f:
        return f.read()


@app.route('/')
@app.route('/home')
def home():
    if 'redcap_api_key' not in session:
        flash("Please enter your REDcap API key in the Settings", "info")
    return render_template('homepage.html')


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    form = SettingsForm(request.form)
    if request.method == 'POST' and form.validate():
        session['redcap_api_key'] = form.redcap_api_key.data
        flash('REDcap API key entered successfully!', "success")
        return redirect(url_for('home'))
    return render_template('settings.html', form=form)


@app.route('/style.css')
def getStyle():
    with open("css/style.css", "r") as f:
        return f.read()


@app.route('/pushData', methods=['PUT', 'POST'])
def pushData():
    if(request.json):
        return pushJSON(request.json)
    else:
        return print("-1")


@app.route('/renameSheet', methods=['PUT', 'POST'])
def renameSheetRequest():
    if(request.json):
        if(request.json["newName"]):
            return renameSheet(request.json["newName"])
    else:
        return print("-1")


@app.route('/clearSheet', methods=['PUT', 'POST'])
def clearSheetRequest():
    return cleanSheet()


@app.route('/pickSpreadsheet', methods=['GET'])
def pickSheetRequest():
    return pickSheet()


@app.route('/pullData')
def pullData():
    return getValues(session['redcap_api_key'])


@app.route('/import_sheets_to_redcap', methods=['PUT', 'POST'])
def import_to_redcap():
    if request.json:
        response = import_data(request.json)
        flash(response)
        return redirect(url_for("home"))
    else:
        return print("-1")


@app.route('/delete_record_redcap', methods=["POST"])
def delete_record():
    if request.method == "POST":
        id = request.form['participantSelection']
        delete_records(id)
        return redirect(url_for("home"))


if __name__ == '__main__':
    app.secret_key = 'e71f3911e68fafd3249dc212cc9954ec'
    app.run(debug=True)
