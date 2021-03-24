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


## Update 2021-03-23-21:50
Added:
* Added export logic. Just needs code to actually write to and select a sheet.
>>>>>>> web-app

Changed:
* Improved data preview before export.
* Set body's font to Arial.
* Improved layout.
* Data now fetches on page load.
* "get data" button changed to "Refresh Data"