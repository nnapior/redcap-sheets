# REDCap Google Sheets

### Introduce:

Thanks for using our webapp.Thisweb application usedto interact with the REDcap API

### What can you do using this web app?

1.Export data to Google sheets.


2.Import data from Google sheets to REDCap.


3.Delete data from REDCap.

## Dependencies

Install the ```requirements.txt``` file with 
```
pip install -r requirements.txt
```
Using the command below on MacOS. ex.
```
● pip3 install -r requirements.txt
```
Using all commands below to install all modules.
```
pip install pandas

pip install --upgrade google-api-python-client google-auth-httplib2google-auth-oauthlib

pip install pycap
```

## Configuration

**if you use these scripts, you need a ```config.json ```file in ```config/``` with the following
contents:**

**{

"api_key":"your-api-key",

"api_url":"link-to-REDCap-API",

"spreadsheet_id": "your-spreadsheet-id"

}**

**The user will also need a ```clinet_secret.json ```file in ```config/```.**

● To get the client secret.json you must go to:

https://console.cloud.google.com/home/dashboard

● On this page click:

    ○ Navigation Menu->APIs & Services->Credentials ->Desktop client 1

● On this page click:

    ○ "DOWNLOAD JSON" Move this file into your project directory

### What do you need?

1. A Google account named Which has the right to editGoogle Sheets.
2. A RedCap account and API key
3. Install the above Requirements
4. UD VPN


### After installing the commands above.

## How to Run and setup the WEBAPP


[Click here to go to How to Run and setup WebApp](/Runing_the_webapp.md)


### Help on how to use all the features.
include:
    Export data to Google sheets.
    
    Import data from Google sheets to REDCap.
    
    Delete data from REDCap.
    

[Click here to go to help page](/Help.md)


Created by:

```
● Mario Durso
● Justin Hamilton
● Nick Napior
● Kojo Otchere-Addo
● Zhenghan Wang
```
