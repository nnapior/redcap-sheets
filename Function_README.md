# Function Documenation 

### createModifySpreadsheet.py:

Function: getSheet(jsonObject)<br/>
Purpose: Function that prints google sheets information<br/>
Parameters: jsonObject - <br/>
Returns: json.dumps(result) - json of sheets results

Function: create_drive_service(creds)<br/>
Purpose:<br/>
Parameters: creds - <br/>
Returns: service - <br/>

Function: create_service(creds) <br/>
Purpose: Function that creates a google service object for google sheets with no parameters <br/>
Parameters: creds - <br/>
Returns: service - <br/>

Function: create_user_service(creds)<br/>
Purpose: Function that creates a google service object for google sheets with no parameters<br/>
Parameters: creds <br/>
Returns: service - service object to interface with google sheets api commands <br/>

Function: get_user_info(jsonObject) <br/>
Purpose: Function that gets google users information <br/>
Parameters: jsonObject - <br/>
Returns: service.userinfo().get().execute() - <br/>

Function: createSpreadsheet(creds) <br/>
Purpose: Function that creates a new spreadsheet in the user's google drive and names it "New Spreadsheet" <br/>
Parameters: creds - <br/>
Returns: newSpreadsheet.get('spreadsheetId') - a spreadsheet ID of the newly created spreadsheet <br/>

Function: getSpreadsheetID() <br/>
Purpose: Function that opens the config.json file and returns the spreadsheetID in the file <br/>
Parameters: N/A <br/>
Returns: content["spreadsheet_id"] - returns a spreadsheet ID of the spreadsheet in the config.json <br/>

Function: getWorksheetID(title, creds, id=getSpreadsheetID()) <br/>
Purpose: Function that takes in the name of a worksheet in a spreadsheet to find the ID of the worksheet <br/>
Parameters:title - , creds - , id=getSpreadsheetID() - <br/>
Returns: None <br/>

Function: generateTuple(jsonObject) <br/>
Purpose: Function that takes in a json object representing the data within the redcap database <br/>
parses the data in the json object into a tuple that can be used by the google sheets api 
to populate a spreadsheet <br/>
Parameters: jsonObject -  <br/>
Returns: newObject - returns a tuple containing the information from the json object <br/>

Function: pushJSON(jsonObject) <br/>
Purpose: Function that takes in a jsonObject and uses that json to replace data in a google sheet 
or add data to a newly created google sheet <br/>
Parameters: jsonObject - <br/>
Returns: id - a string "1" once completed <br/>

Function: pushCompletely(dataSet, spreadsheet_id, creds): <br/>
Purpose: Function that deletes all data from a sheet and populates the same sheet with the data from a tuple <br/>
Parameters: dataSet - tuple representing the data to be added too the sheet <br/>
            spreadsheet_id - spreadsheetID of the spreadsheet to be populated <br/>
            creds - <br/>
Returns: spreadsheet_id - <br/>

Function: batch(requests, spreadsheet_id, creds): <br/>
Purpose: Function that executes a batch update on a spreadsheet <br/>
Parameters: requests - json object representing a command to google sheets api <br/>
            spreadsheet_id - spreadsheetID of the spreadsheet to be updated <br/>
            creds -  <br/>
Returns: N/A <br/>

Function: renameSheet(new_name, spreadsheet_id, creds) <br/>
Purpose: Function that executes a batch update on a spreadsheet to rename the google sheet <br/>
Parameters: new_name - string to become the new name of the google sheet <br/>
            spreadsheet_id - spreadsheetID of the spreadsheet to be update <br/>
            creds -  <br/>
Returns: N/A <br/>

Function: renameWorkSheet(worksheetId, newName, spreadsheet_id, creds) <br/>
Purpose: Function that executes a batch update on a spreadsheet to rename a worksheet in the spreadsheet <br/>
Parameters: worksheetId - string representing the ID of the worksheet in a googlesheet to be changed <br/>
            new_name - string to become the new name of the google worksheet <br/>
            spreadsheet_id - spreadsheetID of the spreadsheet to be updated <br/>
            creds -  <br/>
Returns: <br/>

Function: updateData(service, spreadsheet_id, worksheet_range: str, values: tuple, value_range_body: dict) <br/>
Purpose: Function that executes an update on a spreadsheet to change the data in a range on a worksheet <br/>
Parameters: service - string representing the ID of the worksheet in a googlesheet to be changed <br/>
            spreadsheet_id - spreadsheetID of the spreadsheet to be updated <br/>
            worksheet_range - the worksheet title and cell start in "title!ColumnRow" <br/>
            values - Data to be used in populating the update <br/>
            value_range_body - json including dimentions and values <br/>
Returns: <br/>

Function: clearWorksheet(worksheetName: str, spreadsheet_id, creds) <br/>
Purpose: Function that removes all data from a worksheet in a google sheet <br/>
Parameters: worksheetName - name of the worksheet to be cleared <br/>
            spreadsheet_id - spreadsheetID of the spreadsheet to be updated <br/>
Returns: <br/>

Function: deleteWorksheet(worksheetID, spreadsheet_id, creds) <br/>
Purpose: Funtion that takes in a worksheetID and will delete the worksheet from the google sheet <br/>
Parameters: worksheetID - ID of the worksheet in the sheet to be deleted <br/>
            spreadsheet_id - spreadsheetID of the spreadsheet to be updated <br/>
            creds - <br/>
Returns: <br/>

Function: cleanSheet(spreadsheet_id, creds) <br/>
Purpose: Funtion that takes in a google sheet id and deletes all worksheets and leaves a single empty 
         worksheet titled "Sheet1" <br/>
Parameters: spreadsheet_id - spreadsheetID of the spreadsheet to be cleaned <br/>
            creds - <br/>
Returns: "1" <br/>

Function: createWorksheet(title: str, spreadsheet_id, creds) <br/>
Purpose: Function that creates a new worksheet in the a google sheet <br/>
Parameters: title : string of the name of the worksheet that will be add <br/>
            spreadsheet_id : spreadsheetID of the spreadsheet to be added to <br/>
            creds - <br/>
Returns: "1" - if successful <br/>

### Export-CSV-To-GoogleSheets.py

Function: export_csv_file(file_path: str, parents: list = None) <br/>
Purpose: Function that takes in a file path and adds it to a google sheet <br/>
Parameters: file_path - <br/>
            parents -  <br/>
Returns: <br/>

### Google.py

Function: authGoogle(client_secret_file, scopes, redirect_uri) <br/>
Purpose: Creates a flow instance to manage the OAuth 2.0 Authorization Grant Flow steps <br/>
Parameters: client_secret_file -   <br/>
            scopes - <br/>
            redirect_uri - <br/>
Returns: (authorization_url, state) - <br/>

Function: authGoogleComplete(client_secret_file, scopes, state, response, redirect_uri) <br/>
Purpose: <br/>
Parameters: client_secret_file - <br/>
            scopes - <br/>
            state - <br/>
            response - <br/>
            redirect_uri - <br/>
Returns: json.dumps(object) - <br/>

Function: signOutGoogle(credData, key) <br/>
Purpose: Function that signs out of google <br/>
Parameters: credData - <br/>
            key - <br/>
Returns: "1" - <br/>

Function: signInGoogle(client_secret_file, api_name, api_version, *scopes) <br/>
Purpose: Function that signs into Google <br/>
Parameters: client_secret_file - <br/>
            api_name - <br/>
            api_version - <br/>
            *scopes - <br/>
Returns: json.dumps(object) - <br/>

Function: Create_Service(client_secret_file, api_name, api_version, credData, *scopes)<br/>
Purpose: <br/>
Parameters: client_secret_file<br/>
            api_name, <br/>
            api_version, <br/>
            credData, <br/>
            *scopes<br/>
Returns: service - <br/>

Function: convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0) <br/>
Purpose: Function that returns a datatime string for January 1st, 1900 <br/>
Parameters:year=1900, month=1, day=1, hour=0, minute=0 <br/>
Returns: dt <br/>

### py_REDcap_delete.py

Function: delete_records(id) <br/>
Purpose: Function that deletes all records in redcap id <br/>
Parameters: id - <br/>
Returns: <br/>

### pyREDcap_import.py

Function: createService(creds) <br/>
Purpose: Function creates google service <br/>
Parameters: creds - <br/>
Returns: service - returns service object <br/>

Function: getConfig() <br/>
Purpose: Function returns the configuration data in json form<br/>
Parameters:<br/>
Returns: config<br/>

Function: getEvents(google_service=None)<br/>
Purpose: Function gets all sheet events from google sheets<br/>
Parameters: google_service=None <br/>
Returns: events - google sheet events<br/>

Function: import_redcap(sheet, service, project)<br/>
Purpose: Funciton imports records to redcap<br/>
Parameters: sheet - <br/>
            service - <br/>
            project - <br/>
Returns: "Success" or "Fail" <br/>

Function: import_data(object)<br/>
Purpose: Functions that imports data to Redcap<br/>
Parameters: object - <br/>
Returns: imported - imported data <br/>

### py_REDcap.py

Function: getRecords(apiKey) <br/>
Purpose: Function to get the project records from the database<br/>
Parameters: apiKey - REDCap API key<br/>
Returns: None<br/>

Function: getAPIKey()<br/>
Purpose: Function that opens a config.json file in the same directory and returns the REDCap API key<br/>
Parameters: <br/>
Returns: content["api_key"] - Returns a string object containing the api key<br/>

Function: getProjName(apiKey=getAPIKey())<br/>
Purpose: Function that takes in an api key and returns the title of the REDCap project<br/>
Parameters: apiKey - api key for REDCap project<br/>
Returns: r.json()['project_title'] - Returns a string of the title of the REDCap project name<br/>

Function: getValues(apiKey)<br/>
Purpose: Function that returns the data in a redcap project as a json by reading the api key in config.json<br/>
Parameters: apiKey - REDCap api key<br/>
Returns: (json.dumps(outputObject, indent=4, sort_keys=False)) - Returns a json object containing the data within a REDCap<br/>

Function: getValueDict()<br/>
Purpose:  Function that returns the data in a redcap project as a python dictionary by reading the api key in config.json<br/>
Parameters:<br/>
Returns: (outputObject) - Returns python dictionary<br/>

### summary_webapp.py

Function: checkColumnNames()<br/>
Purpose: Function that checks redcap sheet columns against google sheets columns to compare column names<br/>
Parameters:<br/>
Returns: Prints comparison results <br/>

Function: checkcellData()<br/>
Purpose: Function that checks redcap sheet data against google sheets data to
         compare data and highlight any missing data points between the two<br/>
Parameters:<br/>
Returns: Prints comparison results <br/>

Function: checkworksheetNames()<br/>
Purpose: Function that checks redcap sheet names against google sheets names to
         compare sheet names and identify if any sheets are missing between the two<br/>
Parameters:<br/>
Returns: Prints comparison results <br/>