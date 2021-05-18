## Dependencies and requirements and installation

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
