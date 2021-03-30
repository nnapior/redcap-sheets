import pandas
import json
import random
from config import config
from redcap import Project
from Google import Create_Service

CLIENT_SECRET_FILE = "client_secret.json"
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = '1ztM8iHHvlmEt5SbYZQswNc2UN-4f6ifLHZd3O9aJ2HQ'

service  = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
request = service.spreadsheets().values().get(spreadsheetId = SPREADSHEET_ID, majorDimension = 'ROWS', range = "week_4_arm_1").execute()
rows = request['values']
print(request)


df = pandas.DataFrame(rows[1:],columns = rows[0])
df = df.replace(to_replace="n/a", value="")
rec = json.dumps(random.choice(df.to_dict(orient='records')))
data = [json.loads(rec)]
project = Project(config["api_url"],config["api_token"])
response = project.import_records(to_import=data)
print(response)

