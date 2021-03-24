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


## push-to-sheets Update 2021-03-24-10:51
Added:
* Added a new `/pushData` app route in the Flask webapp that accepts JSON.
* Added basic request code to `pushToSheets(object)` in `scripts.js`

Changed:
* Added a notice that creating a new sheet from the api isn't supported yet