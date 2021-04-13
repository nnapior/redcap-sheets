import requests, json, os
from py_REDcap import getValueDict
from createModifySpreadsheet import *


def checkColumnNames():
    service = create_service()
    spreadsheet_id = getSpreadSheetID()
    
    #check redcap columns 
    redcap_values = (getValueDict())
    redcap_column_values = list(list(list(redcap_values.values())[0].values())[0].keys())
    
    #check google sheet columns
    range_names = [ 
        'A1:AE1'
    ]
    results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheet_id, ranges=range_names).execute()
    google_column_values = results.get('valueRanges', [])
    google_column_values = google_column_values[0].get("values")[0]
   # print(google_column_values)
    #check against each other 
    column_count = 0
    while column_count < len(google_column_values):
        if redcap_column_values[column_count] == google_column_values[column_count]:
            print(column_count, "Column matches!" )
            column_count += 1
        else:
            print(column_count, "Column does not match!") 
            column_count += 1

def checkcellData():
    service = create_service()
    spreadsheet_id = getSpreadSheetID()
    
    #check if redcap cells are missing 
    redcap_values = (getValueDict()) 
    redcap_values = list(list(list(redcap_values.values())[0].values()))
    value_count = 0
    while value_count < len(redcap_values):
        if redcap_values == '':
            print('Missing data')
            value_count += 1
        else:
            print('No data Missing')
            column_count += 1
    #print(redcap_column_values)

    #check if google sheet cells are missing 

#def checkworksheetNumbers():

if __name__ == "__main__":
    checkColumnNames()
    checkcellData()
