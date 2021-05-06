import os, json, math
from array import array
from collections import Counter
from Google import Create_Service
from py_REDcap import getValues
'''
Helper functions for api calls
'''
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

def getWorksheetID(title):
    service = create_service()
    spreadsheet_id = getSpreadSheetID()
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
        # TODO: put this code here
        print("put code to replace sheet here")
    else:
        # creating new sheet
        
        pushCompletely()
    
    return "1"

def pushCompletely():
    cleanSheet()
    # creating new sheet
    dataSet = generateTuple(json.loads(getValues()))
    service = create_service()
    spreadsheet_id = getSpreadSheetID()
    for key in dataSet:
        createWorksheet(key)
        values = dataSet[key]
        value_range_body = {
            'majorDimension' : 'ROWS',
            'values' : values
        }
        worksheet_range = key+'!A1'
        updateData(service,spreadsheet_id, worksheet_range, values, value_range_body)
    deleteWorksheet(getWorksheetID("Sheet1"))

'''
API funtion calls
'''
#create new google sheet
def createSheet():
    newSheetData = service.spreadsheets().create().execute()
    




def batch(requests):
    """
    function to run batch updates on the sheet.
    """
    service = create_service()
    spreadsheet_id = getSpreadSheetID()
    body = {
        'requests': requests
    }
    return service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()

#function that takes in a string a renames the google sheet
def renameSheet(new_name):
    """
    function to rename sheet
    """
    batch({
        "updateSpreadsheetProperties": {
            "properties": {
                "title": new_name,
            },
            "fields": "title",
        }
    })
def renameWorkSheet(sheetId, newName):
    batch({
        "updateSheetProperties": {
            "properties": {
                "sheetId": sheetId,
                "title": newName,
            },
            "fields": "title",
        }
    })

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
def clearWorksheet(sheetName: str):
    service = create_service()
    spreadsheet_id = getSpreadSheetID()
    service.spreadsheets( ).values( ).clear(
        spreadsheetId=spreadsheet_id,
        range='{0}!A1:Z'.format( sheetName ),
        body={}
    ).execute( )
    
#funtion that takes in a worksheetID and will delete the worksheet
def deleteWorksheet(worksheetID):
    service = create_service()
    spreadsheet_id = getSpreadSheetID()
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
    
def cleanSheet():
    service = create_service()
    spreadsheet_id = getSpreadSheetID()
    data = service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=[], includeGridData=False).execute()
    #createWorksheet("Sheet1")
    worksheetIds= [x["properties"]["sheetId"]for x in data["sheets"]]
    for ids in worksheetIds[:-1]:
        deleteWorksheet(ids)
    renameWorkSheet(worksheetIds[-1],"Sheet1")
 #   clearWorksheet("Sheet1")


def validatedata():
    service = create_service()
    spreadsheet_id = getSpreadSheetID()
    diabetes = service.spreadsheets().values().get(spreadsheetId = spreadsheet_id, range=("initial_data_arm_1!D2:D11")).execute()
    print(diabetes["values"])
    #need to convert list to arrray 
    c = Counter(diabetes["values"])
    c.most_common()
    value, count = c.most_common()[0]
    print(value)
    for cell in diabetes["values"] :
        if cell == value:
            sheet_id = 2158304
            request_body = {
                'requests': [
                    {
                        'repeatCell': {
                            'range':{
                               'sheetId' : sheet_id,
                               'startRowIndex' : 2,
                               'endRowIndex' : 11,
                               'startColumnIndex' : 3,
                               'endColumnIndex' : 3
                           },
                           'cell' :{
                               'userEnteredFormat' :{
                                   'backgroundColor':{
                                       'red': 120
                                  }
                               }
                           }
                       }
                    }
                ]
            }
    response = service.spreadsheets().batchUpdate(
        spreadsheetId = spreadsheet_id,
        body = requeest_body
    ).execute
   
    




'''
function that takes in the service, spreadsheetID, and title of the new worksheet
creates a worksheet with 20 by 5 with the specified title
'''
def createWorksheet(title:str):
    service = create_service()
    spreadsheet_id = getSpreadSheetID()
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
    validatedata()
    
    #updateData(service,spreadsheet_id, worksheet_range, values, value_range_body)
    
    #print(getWorksheetID("a"))
    #deleteWorksheet(getWorksheetID("Sheet3"))
    #CSV-to-Google-Sheet
    renameSheet("CSV-to-Google-Sheet")
    #renameWorkSheet(getWorksheetID("a"),"Sheet1")
    #print(generateTuple(json.loads(getValues())))
    #cleanSheet()
    

    
