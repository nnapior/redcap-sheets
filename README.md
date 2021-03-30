# 475-team5-s21project

Software to connect REDCap with Google Sheets.

=======
Creates a web application to interact with the REDcap API


run createModifySpreadsheet.py to update a google sheet



if you use these scripts, you need a "config.json" file with the following contents:

```
{
	"api_key":"your-api-key",
	"spreadsheet_id": "your-spreadsheet-id"
}
```

you will also need your own clinet_secret.json
=======
Run this python script with "python redcap_sheets_webapp.py"


## push-to-sheets Update 2021-03-24-15:35
Added:
* Added `generateTuple()` to parse JSON into a tuple and `pushJSON()` for import mode logic in `createModifySpreadsheet.py`. 

Changed:
* Modified `/pushData` to use `pushJSON()`.
* `/pushData` JSON object is now in the format of `{"mode":"<EXPORT_MODE>", "object":{JSON OBJECT}}` for reasons of detecting export mode in backend
* Removed "Append" export option

View TODOs in code to see open tasks.

## push-to-sheets Update 2021-03-24-10:51
Added:
* Added a new `/pushData` app route in the Flask webapp that accepts JSON.
* Added basic request code to `pushToSheets(object)` in `scripts.js`

Changed:
* Added a notice that creating a new sheet from the api isn't supported yet