import os, json
from Google import Create_Service
from py_REDcap import getValueDict

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


def pushJSON(jsonObject):
    importMode = jsonObject['mode']
    data = generateTuple(jsonObject['object'])
    
    if(importMode == "replace"):
        # replacing sheet data
        # TODO: put this code here
        print("put code to replace sheet here")
    else:
        # creating new sheet
        # TODO: put this code here
        print("put code to create a new sheet here")
    
    return "1"

"""
function to generate a values tuple from json
"""
def generateTuple(jsonObject):
    
    keys = list(jsonObject.keys())
    
    newObject = {}
    
    for key in keys:
        event = jsonObject[key]
        eventKeys = list(event.keys())
        
        eventObject = ()
        
        headerObject = ()
        for headerKey in list(event[eventKeys[0]]):
            headerObject = headerObject+(headerKey,)
        
        eventObject = eventObject+(headerObject,)
        
        for eventKey in eventKeys:
            participantObject = ()
            for participantKey in list(event[eventKey].keys()):
                participantValue = event[eventKey][participantKey].replace("\n"," ")
                participantObject = participantObject+(participantValue,)
            eventObject = eventObject+(participantObject,)
        
        newObject[key] = eventObject
    
    return newObject

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

def getValues1():
    v = getValueDict()


#function that clears the 
def clearData(service, spreadsheet_id, sheetName: str):
    service.spreadsheets( ).values( ).clear(
        spreadsheetId=spreadsheet_id,
        range='{0}!A1:Z'.format( sheetName ),
        body={}
    ).execute( )
    
        
if __name__ == "__main__":
    service = create_service()
    
    spreadsheet_id = getSpreadSheetID()
    mySpreadsheets = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    worksheet_range = 'Sheet1!A1'
    
    value_range_body = {
        'majorDimension' : 'ROWS',
        'values' : values
    }
    #tuple(outputObject.get('initial_data_arm_1').get('1').keys())
    clearData(service,spreadsheet_id, "Sheet1")
    #updateData(service,spreadsheet_id, worksheet_range, values, value_range_body)
