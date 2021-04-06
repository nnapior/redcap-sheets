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


## main Update 2021-04-06-16:12

Added:
* Merged code for creating new spreadsheets with Tabler interface.
* Added a placeholder function for choosing an existing spreadsheet. Currently nonfunctional.

Changed:
* Removed "Existing (Append)" spreadsheet destination.
* Renamed page to "REDCap to Google Sheets"