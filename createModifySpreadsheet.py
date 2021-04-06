import os, json
from Google import Create_Service
from py_REDcap import *
'''
Helper functions for api calls
'''
def pickSheet():
    return "1"

def create_service():
    CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = 'sheets'
    API_VERSION = 'v4'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']

    service= Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    return service

def createSpreadsheet():
    print("======creating new spreadsheet======")
    service = create_service()
    spreadsheet = {
        'properties': {
            'title': "New Spreadsheet"
        }
    }
    newSpreadsheet = service.spreadsheets().create(body=spreadsheet,fields='spreadsheetId').execute()
    print(newSpreadsheet.get('spreadsheetUrl'))
    print(newSpreadsheet.get('spreadsheetId'))
    return newSpreadsheet.get('spreadsheetId')

def getSpreadSheetID():
    configFile = open("config.json","r")
    content = json.loads(configFile.read())
    return content["spreadsheet_id"]

def getWorksheetID(title, id = getSpreadSheetID()):
    service = create_service()
    spreadsheet_id = id
    data = service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=[], includeGridData=False).execute()
    
    for x in data["sheets"]:
        if x["properties"]["title"] == title:
            return x["properties"]["sheetId"]
    return None
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

def pushJSON(jsonObject):
    importMode = jsonObject['mode']
    data = generateTuple(jsonObject['object']) 
    
    if(importMode == "replace"):
        # replacing sheet data
        pushCompletely(data, getSpreadSheetID())
    else:
        # creating new sheet
        pushCompletely(data, createSpreadsheet())
    
    return "1"

def pushCompletely(object = getValues(), id = getSpreadSheetID()):
    cleanSheet(id)
    # creating new sheet
    dataSet = object
    service = create_service()
    spreadsheet_id = id
    for key in dataSet:
        createWorksheet(key, spreadsheet_id)
        values = dataSet[key]
        value_range_body = {
            'majorDimension' : 'ROWS',
            'values' : values
        }
        worksheet_range = key+'!A1'
        updateData(service,spreadsheet_id, worksheet_range, values, value_range_body)
    # TODO: only rename if no new name has been set
    renameSheet(getProjName(), spreadsheet_id)
    deleteWorksheet(getWorksheetID("Sheet1", spreadsheet_id), spreadsheet_id)

'''
API funtion calls
'''
def batch(requests, id = getSpreadSheetID()):
    """
    function to run batch updates on the sheet.
    """
    service = create_service()
    spreadsheet_id = id
    body = {
        'requests': requests
    }
    return service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()

#function that takes in a string a renames the google sheet
def renameSheet(new_name, id):
    """
    function to rename sheet
    """
    return batch({
        "updateSpreadsheetProperties": {
            "properties": {
                "title": new_name,
            },
            "fields": "title",
        }
    }, id)

def renameWorkSheet(sheetId, newName, id=getSpreadSheetID()):
    return batch({
        "updateSheetProperties": {
            "properties": {
                "sheetId": sheetId,
                "title": newName,
            },
            "fields": "title",
        }
    }, id)

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



#function that clears the data of a worksheet
def clearWorksheet(sheetName: str, id=getSpreadSheetID()):
    service = create_service()
    spreadsheet_id = id
    service.spreadsheets( ).values( ).clear(
        spreadsheetId=spreadsheet_id,
        range='{0}!A1:Z'.format( sheetName ),
        body={}
    ).execute( )
    
#funtion that takes in a worksheetID and will delete the worksheet
def deleteWorksheet(worksheetID, id=getSpreadSheetID()):
    service = create_service()
    spreadsheet_id = id
    request_body = {
            'requests': [
                {'deleteSheet': {
                    'sheetId': worksheetID }
                 }   
            ]
        }
    service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body = request_body
     ).execute()
    
def cleanSheet(id = getSpreadSheetID()):
    print("CLEANING SPREADSHEET ID "+id)
    service = create_service()
    spreadsheet_id = id
    data = service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=[], includeGridData=False).execute()
    #createWorksheet("Sheet1")
    worksheetIds= [x["properties"]["sheetId"]for x in data["sheets"]]
    for ids in worksheetIds[:-1]:
        deleteWorksheet(ids)
    renameWorkSheet(worksheetIds[-1],"Sheet1", spreadsheet_id)
    clearWorksheet("Sheet1", spreadsheet_id)
    return "1"

'''
function that takes in the service, spreadsheetID, and title of the new worksheet
creates a worksheet with 20 by 5 with the specified title
'''
def createWorksheet(title:str, id = getSpreadSheetID()):
    service = create_service()
    spreadsheet_id = id
    request_body = {
            'requests': [
                {'addSheet': { "properties" :{
                        'title': title,
                        'gridProperties' : {
                            'rowCount' : 20,
                            'columnCount' : 40
                        },
                        'hidden' : False}
                    }
                }   
            ]
        }
    service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body = request_body
     ).execute()

if __name__ == "__main__":
    service = create_service()
    spreadsheet_id = getSpreadSheetID()
    mySpreadsheets = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    worksheet_range = 'Sheet1!A1'
    values =[]
    value_range_body = {
        'majorDimension' : 'ROWS',
        'values' : values
    }

    """
    for loop to create multiple worksheets
    """
    worksheetTitles = ('Test1', 'Test2', 'Test3')
    '''for title in worksheetTitles:
        createWorksheet(service, spreadsheet_id, title)'''
    
    
    #updateData(service,spreadsheet_id, worksheet_range, values, value_range_body)
    
    #print(getWorksheetID("a"))
    #deleteWorksheet(getWorksheetID("Sheet3"))
    #CSV-to-Google-Sheet
    renameSheet("CSV-to-Google-Sheet")
    #renameWorkSheet(getWorksheetID("a"),"Sheet1")
    #print(generateTuple(json.loads(getValues())))
    cleanSheet()
    

    
