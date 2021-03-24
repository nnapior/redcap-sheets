import os, json
from Google import Create_Service

def create_service():
    CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = 'sheets'
    API_VERSION = 'v4'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    service= Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    return service

def getSpreadSheetID():
    configFile = open("config.json","r")
    content = json.loads(configFile.read())
    return content["spreadsheet_id"]


"""
function that updates a google sheet's values
"""
def updateData(service,spreadsheet_id, worksheet_range: str, values: tuple, value_range_body: dict):
    service.spreadsheets().values().update(
        spreadsheetId = spreadsheet_id,
        valueInputOption = 'USER_ENTERED',
        range= worksheet_range,
        body = value_range_body
    ).execute()

    
 def createWorksheet(spreadsheet_id, request_body):
    spreadsheetId=spreadsheet_id,
    body = request_body
    ).execute()

if __name__ == "__main__":
    service = create_service()
    
    spreadsheet_id = getSpreadSheetID()
    mySpreadsheets = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    worksheet_range = 'Sheet1!B2' 
    values = (
        ('Col A', 'Col B'),
        ('blue' , 'pink')
    )
    value_range_body = {
        'majorDimension' : 'ROWS',
        'values' : values
    }
   
    """
    for loop to create multiple worksheets
    """
    worksheetTitles = ('Test1', 'Test2', 'Test3') 
    for worksheetTitle in worksheetTitles
    """
    creates a new worksheet
    """
    request_body = {
        'requests': [
            {
                'addSheet': {
                    'title':'worksheetTitle',
                    'gridProperties' : {
                        'rowCount' : 20,
                        'coulumnCount' : 5
                    },
                    'hidden' : False
                }
            }   
        ]
    }
    updateData(service,spreadsheet_id, worksheet_range, values, value_range_body)
    createWorksheet(spreadsheet_id, request_body)
