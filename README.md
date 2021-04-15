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
* Use `python3` on MacOS python doesn't work.
	* ex. `python3 redcap_sheets_webapp.py`

### main Update 2021-04-15
Merged:
* Add_Import_to_webapp
* cleanup
* create-new-spreadsheet-tabler
* security-reinforcement

Changes:
* Sign in to Google
* Sign out of Google
* Import from Google Sheets to REDcap
* Select and export to existing sheet in Google Drive
* Settings page to enter REDcap API key
* Redirect to Google sheet in new window when export is complete
* Added documentation
* Added folder structure for webapp
* Added folder structure for `lib/` for Dependencies of the webapp
* Updated requirements.txt, README, and .gitignore
