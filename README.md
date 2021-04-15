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

=======
The user will also need a clinet_secret.json.
To get the client secret.json you must go to:

https://console.cloud.google.com/home/dashboard
On this page click:
	Navigation Menu->APIs & Services->Credentials ->Desktop client 1
On this page click:
	"DOWNLOAD JSON"
Move this file into your project directory


=======
Run this python script with "python redcap_sheets_webapp.py"


## `security-reinforcement` Update 2021-04-14-23:53

Added:
* Added a button to sign into Google
* Added a button to revoke access of your Google account to the webapp

Changed:
* Modified the `.pickle` file behavior, so your user credentials are returned to the browser and stored locally rather than server-side