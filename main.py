#importing modules
import pandas
import json
from config import config
from redcap import Project
from Google import Create_Service

#set up data for requests
CLIENT_SECRET_FILE = "client_secret.json"
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = '1ztM8iHHvlmEt5SbYZQswNc2UN-4f6ifLHZd3O9aJ2HQ'


#create google sheet service object
service  = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# create redcap api object
project = Project(config["api_url"],config["api_token"])


#request for google sheets data and extract the sheeets names
sheet_metadata = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
sheets_info = sheet_metadata.get('sheets', '')
sheets = [sheets_info[x].get("properties", {}).get("title", "Sheet1") for x in range(len(sheets_info))]


#iterate through sheets
for sheet in sheets:
    #request for particular sheet data
    request = service.spreadsheets().values().get(spreadsheetId = SPREADSHEET_ID, majorDimension = 'ROWS', range = sheet).execute()
    rows = request['values']
    print(request)

    #create dataframe from rows get from sheet
    df = pandas.DataFrame(rows[1:],columns = rows[0])
    df = df.replace(to_replace="n/a", value="")

    # create dict from dataframe
    rows = df.to_dict(orient = 'records')

    #iterate through each record from rows: dict
    for row in rows:
        row["redcap_event_name"] = sheet  #append event name to record
        rec = json.dumps(row)   #converting record to  json format
        data = [json.loads(rec)]    #load json object and put that in list
        response = project.import_records(to_import=data) #import record to redcap api
        print(response) #printing response

