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
    print(google_column_values)
    #check against each other 
    column_count = 0
    while column_count < len(google_column_values):
        if redcap_column_values[column_count] == google_column_values[column_count]:
            print( "Column", column_count, "matches!" )
            column_count += 1
        else:
            print("Column", column_count, "does not match!") 
            column_count += 1

def checkcellData():
    service = create_service()
    spreadsheet_id = getSpreadSheetID()
    
    #check if redcap cells are missing 
    redcap_values = (getValueDict()) 
    redcap_values = list(list(list(redcap_values.values())[0].values())[0].values())
   # print(redcap_values)
    value_count = 0
    while value_count < len(redcap_values):
        if redcap_values == '':
            print('Missing red cap data')
            value_count += 1
        else:
            print('No red cap data Missing')
            value_count += 1

    #check if google sheet cells are missing 
    spreadsheet_data = service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=[], includeGridData=False).execute()
    cell_count = 0 
    while cell_count < len(spreadsheet_data):
        if spreadsheet_data == '':
            print("Missing Google sheets data")
            cell_count += 1
        else: 
            print("No google sheets data Missing")
            cell_count += 1
    #print(spreadsheet_data)
   

def checkworksheetNumbers():
    service = create_service()
    spreadsheet_id = getSpreadSheetID()
    #redcap worksheet names
    redcap_worksheets = (getValueDict()) 
    redcap_worksheets = list(list(list(redcap_worksheets.values())[0].values())[0].values())
    #currently print data values not sheet name
    print(redcap_worksheets)

    #Google worksheet names
    results = service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=[], includeGridData=False).execute()
    worksheet_names = results.get('sheets', [])
    worksheet_names = worksheet_names[0].get('properties', [])
    
    print(worksheet_names)
    worksheet_count = 0 
    while worksheet_count < len(worksheet_names):
        if worksheet_names == '':
            print("Missing Google Worksheet")
            worksheet_count += 1
        else: 
            print("No Google workssheet Missing")
            worksheet_count += 1

if __name__ == "__main__":
    checkColumnNames()
    checkcellData()
    checkworksheetNumbers()
