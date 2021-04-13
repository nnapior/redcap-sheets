import os, json
from Google import Create_Service
from py_REDcap import *
'''
Helper functions for api calls
'''
def pickSheet():
    return "1"

"""
create_service
    Function that creates a google service object for google sheets with no parameters

    Returns a service object to interface with google sheets api commands
"""
def create_service(creds):
    CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = 'sheets'
    API_VERSION = 'v4'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']

    #calls Create_Service from google module
    service= Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, creds, SCOPES)
    return service

"""
createSpreadsheet
    Function that creates a new spreadsheet in the user's google drive and names it "New Spreadsheet"

    Returns a spreadsheet ID of the newly created spreadsheet
"""
def createSpreadsheet(creds):
    print("======creating new spreadsheet======")
    service = create_service(creds)
    spreadsheet = {
        'properties': {
            'title': "New Spreadsheet"
        }
    }
    newSpreadsheet = service.spreadsheets().create(body=spreadsheet,fields='spreadsheetId').execute()
    print(newSpreadsheet.get('spreadsheetUrl'))
    print(newSpreadsheet.get('spreadsheetId'))
    return newSpreadsheet.get('spreadsheetId')


"""
getSpreadsheetID
    Function that opens the config.json file and returns the spreadsheetID in the file

    returns a spreadsheet ID of the spreadsheet in the config.json
"""
def getSpreadsheetID():
    configFile = open("config.json","r")
    content = json.loads(configFile.read())
    return content["spreadsheet_id"]


"""
getWorksheetID
    Function that takes in the name of a worksheet in a spreadsheet to find the ID of the worksheet

    Parameters:
        title: String that is the title of a worksheet
        id: the spreadsheet id that contains the worksheetID the user is looking for

    returns the worksheet ID of the specifed worksheet title in a spreadsheet if worksheet in sheet
    returns None if the sheet does not contain the worksheet
"""
def getWorksheetID(title, creds, id = getSpreadsheetID()):
    service = create_service(creds)
    spreadsheet_id = id
    #get data of spreadsheet
    spreadsheet_data = service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=[], includeGridData=False).execute()
    
    for worksheet in spreadsheet_data["sheets"]:
        if worksheet["properties"]["title"] == title:
            return worksheet["properties"]["sheetId"]
    return None

"""
generateTuple
    Function that takes in a json object representing the data within the redcap database
        parses the data in the json object into a tuple that can be used by the google sheets api
        to populate a spreadsheet

    Parameters:
        jsonObject : jsonObject representing the data from a REDCap database

returns a tuple containing the information from the json object
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
pushJSON
    Function that takes in a jsonObject and uses that json to replace data in a google sheet
        or add data to a newly created google sheet

    Parameters:
        jsonObject : jsonObject representing the data from a REDCap database

returns a string "1" once completed
"""
def pushJSON(jsonObject):
    importMode = jsonObject['mode']
    data = generateTuple(jsonObject['object']) 
    creds = jsonObject['creds']
    print(creds)
    
    if(importMode == "replace"):
        # replacing sheet data
        pushCompletely(data, getSpreadsheetID(), creds)
    else:
        # creating new sheet
        pushCompletely(data, createSpreadsheet(creds), creds)
    
    return "1"


"""
pushCompletely
    Function that deletes all data from a sheet and populates the same sheet with the data from a tuple

    Parameters:
        dataSet : tuple representing the data to be added too the sheet
        spreadsheet_id : spreadsheetID of the spreadsheet to be populated
"""
def pushCompletely(dataSet, spreadsheet_id, creds):
    
    #remove previous data
    cleanSheet(spreadsheet_id, creds)
    
    service = create_service(creds)
    
    #add data too sheet
    for table_title in dataSet:
        createWorksheet(table_title, spreadsheet_id, creds)
        table_content = dataSet[table_title]
        value_range_body = {
            'majorDimension' : 'ROWS',
            'values' : table_content
        }
        worksheet_range = table_title+'!A1'
        updateData(service,spreadsheet_id, worksheet_range, table_content, value_range_body)
    # TODO: only rename if no new name has been set
    renameSheet(getProjName(), spreadsheet_id, creds)
    
    #remove hanging empty worksheet from when sheet was cleaned
    deleteWorksheet(getWorksheetID("Sheet1", creds, spreadsheet_id), spreadsheet_id, creds)

'''
API funtion calls
'''

"""
batch
    Function that executes a batch update on a spreadsheet

    Parameters:
        requests : json object representing a command to google sheets api
        spreadsheet_id : spreadsheetID of the spreadsheet to be updated
"""
def batch(requests, spreadsheet_id, creds):
    """
    function to run batch updates on the sheet.
    """
    service = create_service(creds)
    body = {
        'requests': requests
    }
    service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()

"""
renameSheet
    Function that executes a batch update on a spreadsheet to rename the google sheet

    Parameters:
        new_name : string to become the new name of the google sheet
        spreadsheet_id : spreadsheetID of the spreadsheet to be updated
"""
def renameSheet(new_name, spreadsheet_id, creds):
    batch({
        "updateSpreadsheetProperties": {
            "properties": {
                "title": new_name,
            },
            "fields": "title",
        }
    }, spreadsheet_id, creds)


"""
renameWorkSheet
    Function that executes a batch update on a spreadsheet to rename a worksheet in the spreadsheet

    Parameters:
        worksheetId : string representing the ID of the worksheet in a googlesheet to be changed
        new_name : string to become the new name of the google worksheet
        spreadsheet_id : spreadsheetID of the spreadsheet to be updated
"""
def renameWorkSheet(worksheetId, newName, spreadsheet_id, creds):
    batch({
        "updateSheetProperties": {
            "properties": {
                "sheetId": worksheetId,
                "title": newName,
            },
            "fields": "title",
        }
    }, spreadsheet_id, creds)

"""
updateData
    Function that executes an update on a spreadsheet to change the data in a range on a worksheet

    Parameters:
        service : string representing the ID of the worksheet in a googlesheet to be changed
        spreadsheet_id : spreadsheetID of the spreadsheet to be updated
        worksheet_range : the worksheet title and cell start in "title!ColumnRow" 
        values : Data to be used in populating the update
        value_range_body : json including dimentions and values
"""
def updateData(service,spreadsheet_id, worksheet_range: str, values: tuple, value_range_body: dict):
    service.spreadsheets().values().update(
        spreadsheetId = spreadsheet_id,
        valueInputOption = 'USER_ENTERED',
        range= worksheet_range,
        body = value_range_body
    ).execute()



"""
clearWorksheet
    Function that removes all data from a worksheet in a google sheet

    Parameters:
        worksheetName : name of the worksheet to be cleared
        spreadsheet_id : spreadsheetID of the spreadsheet to be updated
"""
def clearWorksheet(worksheetName: str, spreadsheet_id, creds):
    service = create_service(creds)
    service.spreadsheets( ).values( ).clear(
        spreadsheetId=spreadsheet_id,
        range='{0}!A1:Z'.format( worksheetName ),
        body={}
    ).execute( )
 
"""
deleteWorksheet
    Funtion that takes in a worksheetID and will delete the worksheet from the google sheet

    Parameters:
        worksheetID : ID of the worksheet in the sheet to be deleted
        spreadsheet_id : spreadsheetID of the spreadsheet to be updated
"""
def deleteWorksheet(worksheetID, spreadsheet_id, creds):
    service = create_service(creds)
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


"""
cleanSheet
    Funtion that takes in a google sheet id and deletes all worksheets and leaves a single empty
        worksheet titled "Sheet1"

    Parameters:
        spreadsheet_id : spreadsheetID of the spreadsheet to be cleaned
        
    Returns the string "1" if successful
"""
def cleanSheet(spreadsheet_id, creds):
    print("CLEANING SPREADSHEET ID "+spreadsheet_id)
    service = create_service(creds)
    data = service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=[], includeGridData=False).execute()
    #createWorksheet("Sheet1")
    
    
    worksheetIds= [worksheet["properties"]["sheetId"] for worksheet in data["sheets"]]
    for ids in worksheetIds[:-1]:
        deleteWorksheet(ids, spreadsheet_id, creds)
    renameWorkSheet(worksheetIds[-1],"Sheet1", spreadsheet_id, creds)
    clearWorksheet("Sheet1", spreadsheet_id, creds)
    return "1"


"""
createWorksheet
    Function that creates a new worksheet in the a google sheet

    Parameters:
        title : string of the name of the worksheet that will be add
        spreadsheet_id : spreadsheetID of the spreadsheet to be added too
        
    Returns the string "1" if successful
"""
def createWorksheet(title:str, spreadsheet_id, creds):
    service = create_service(creds)
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
    spreadsheet_id = getSpreadsheetID()
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
    #renameSheet("CSV-to-Google-Sheet")
    #renameWorkSheet(getWorksheetID("a"),"Sheet1")
    #print(generateTuple(json.loads(getValues())))
    pushCompletely(generateTuple(json.loads(getValues())), getSpreadsheetID())
    

    
