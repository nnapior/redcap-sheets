# Function Documenation 

### createModifySpreadsheet.py:

Function: getSheet(jsonObject)
Purpose: Function that prints google sheets information
Parameters: jsonObject - 
Returns: json.dumps(result) - json of sheets results

Function: create_drive_service(creds)
Purpose:
Parameters: creds - 
Returns: service - 

Function: create_service(creds)
Purpose: Function that creates a google service object for google sheets with no parameters
Parameters: creds - 
Returns: service - 

Function: create_user_service(creds)
Purpose: Function that creates a google service object for google sheets with no parameters
Parameters: creds
Returns: service - service object to interface with google sheets api commands

Function: get_user_info(jsonObject)
Purpose: Function that gets google users information
Parameters: jsonObject - 
Returns: service.userinfo().get().execute() - 

Function: createSpreadsheet(creds)
Purpose: Function that creates a new spreadsheet in the user's google drive and names it "New Spreadsheet"
Parameters: creds - 
Returns: newSpreadsheet.get('spreadsheetId') - a spreadsheet ID of the newly created spreadsheet

Function: getSpreadsheetID() 
Purpose: Function that opens the config.json file and returns the spreadsheetID in the file
Parameters: N/A
Returns: content["spreadsheet_id"] - returns a spreadsheet ID of the spreadsheet in the config.json

Function: getWorksheetID(title, creds, id=getSpreadsheetID())
Purpose: Function that takes in the name of a worksheet in a spreadsheet to find the ID of the worksheet
Parameters:title - , creds - , id=getSpreadsheetID() -
Returns: None

Function: generateTuple(jsonObject)
Purpose: Function that takes in a json object representing the data within the redcap database
parses the data in the json object into a tuple that can be used by the google sheets api
to populate a spreadsheet
Parameters: jsonObject - 
Returns: newObject - returns a tuple containing the information from the json object

Function: pushJSON(jsonObject)
Purpose: Function that takes in a jsonObject and uses that json to replace data in a google sheet
or add data to a newly created google sheet 
Parameters: jsonObject - 
Returns: id - a string "1" once completed

Function: pushCompletely(dataSet, spreadsheet_id, creds):
Purpose: Function that deletes all data from a sheet and populates the same sheet with the data from a tuple
Parameters: dataSet - tuple representing the data to be added too the sheet
            spreadsheet_id - spreadsheetID of the spreadsheet to be populated
            creds -
Returns: spreadsheet_id - 

Function: batch(requests, spreadsheet_id, creds):
Purpose: Function that executes a batch update on a spreadsheet
Parameters: requests - json object representing a command to google sheets api
            spreadsheet_id - spreadsheetID of the spreadsheet to be updated
            creds - 
Returns: N/A

Function: renameSheet(new_name, spreadsheet_id, creds)
Purpose: Function that executes a batch update on a spreadsheet to rename the google sheet
Parameters: new_name - string to become the new name of the google sheet
            spreadsheet_id - spreadsheetID of the spreadsheet to be update
            creds - 
Returns: N/A

Function: renameWorkSheet(worksheetId, newName, spreadsheet_id, creds)
Purpose: Function that executes a batch update on a spreadsheet to rename a worksheet in the spreadsheet
Parameters: worksheetId - string representing the ID of the worksheet in a googlesheet to be changed
            new_name - string to become the new name of the google worksheet
            spreadsheet_id - spreadsheetID of the spreadsheet to be updated
            creds - 
Returns:

Function: updateData(service, spreadsheet_id, worksheet_range: str, values: tuple, value_range_body: dict)
Purpose: Function that executes an update on a spreadsheet to change the data in a range on a worksheet
Parameters: service - string representing the ID of the worksheet in a googlesheet to be changed
            spreadsheet_id - spreadsheetID of the spreadsheet to be updated
            worksheet_range - the worksheet title and cell start in "title!ColumnRow"
            values - Data to be used in populating the update
            value_range_body - json including dimentions and values
Returns:

Function: clearWorksheet(worksheetName: str, spreadsheet_id, creds)
Purpose: Function that removes all data from a worksheet in a google sheet
Parameters: - worksheetName - name of the worksheet to be cleared
            spreadsheet_id - spreadsheetID of the spreadsheet to be updated
Returns:

Function: deleteWorksheet(worksheetID, spreadsheet_id, creds)
Purpose: Funtion that takes in a worksheetID and will delete the worksheet from the google sheet
Parameters: worksheetID - ID of the worksheet in the sheet to be deleted
            spreadsheet_id - spreadsheetID of the spreadsheet to be updated
            creds - 
Returns: 

Function: cleanSheet(spreadsheet_id, creds)
Purpose: Funtion that takes in a google sheet id and deletes all worksheets and leaves a single empty
         worksheet titled "Sheet1"
Parameters: spreadsheet_id - spreadsheetID of the spreadsheet to be cleaned
            creds - 
Returns: "1"

Function: createWorksheet(title: str, spreadsheet_id, creds)
Purpose: Function that creates a new worksheet in the a google sheet
Parameters: title : string of the name of the worksheet that will be add
            spreadsheet_id : spreadsheetID of the spreadsheet to be added to
            creds - 
Returns: "1" - if successful

### Export-CSV-To-GoogleSheets.py

Function: export_csv_file(file_path: str, parents: list = None)
Purpose: Function that takes in a file path and adds it to a google sheet
Parameters: file_path - 
            parents - 
Returns:

### Google.py

Function:
Purpose:
Parameters:
Returns:

Function: 
Purpose:
Parameters:
Returns:

Function:
Purpose:
Parameters:
Returns:

Function: 
Purpose:
Parameters:
Returns:

Function:
Purpose:
Parameters:
Returns:

Function: 
Purpose:
Parameters:
Returns:

Function:
Purpose:
Parameters:
Returns: