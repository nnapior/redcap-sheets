# REDCap Google Sheets
Creates a web application to interact with the REDcap API

## Dependencies
Install the `requirements.txt` file with `pip install -r requirements.txt`
* Use `pip3` on MacOS. ex. `pip3 install -r requirements.txt`

## Configuration
if you use these scripts, you need a `config.json` file in `config/` with the following contents:

```
{
	"api_key":"your-api-key",
	"api_url":"link-to-REDCap-API",
	"spreadsheet_id": "your-spreadsheet-id"
}
```
The user will also need a `clinet_secret.json` file in `config/`.
* To get the client secret.json you must go to: https://console.cloud.google.com/home/dashboard
* On this page click:
	* Navigation Menu->APIs & Services->Credentials ->Desktop client 1
* On this page click:
	* "DOWNLOAD JSON"
Move this file into your project directory


## Running the webapp
Run this python script with `python redcap_sheets_webapp.py`


### main Update 2021-04-06-16:12

Added:
* Merged code for creating new spreadsheets with Tabler interface.
* Added a placeholder function for choosing an existing spreadsheet. Currently nonfunctional.

Changed:
* Removed "Existing (Append)" spreadsheet destination.
* Renamed page to "REDCap to Google Sheets"
