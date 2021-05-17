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

**1.How to export data to Google sheets.**

1.In the lower right section, you can export datato Google Sheets.

![image](https://user-images.githubusercontent.com/54848986/117846018-a27e2c00-b2b3-11eb-9064-310ae0955629.png)

2. You can export all events or you can select the data which you want to. And also to choose
the target sheet. Finally, click Export button

![image](https://user-images.githubusercontent.com/54848986/117846107-b75abf80-b2b3-11eb-8b84-a9056783b232.png)

**2.How to import data from Google sheets to REDCap.**

1.In the lower left section, you can import data fromGoogle Sheets to REDCap

![image](https://user-images.githubusercontent.com/54848986/117846178-c6417200-b2b3-11eb-94bf-2cad0b78cafe.png)

2. You can import all events to REDCap or you can select the data which you want to. And also
to choose the target sheet. Finally, click ImportButton

![image](https://user-images.githubusercontent.com/54848986/117846244-d5282480-b2b3-11eb-8199-fe9dde134e92.png)

**3.How to delete data from REDCap.** 

1.In the middle section, you can delete data from REDCap

![image](https://user-images.githubusercontent.com/54848986/117846283-e07b5000-b2b3-11eb-8211-b834a56b515f.png)

2. You can click the delete button (red one) to deletethe data, but make sure that you have
permission to delete those. If you don't have permission,it will show “you don't have permission
to delete”. If you have permission to delete, it willshow “delete successfully.”
3. You can choose which event, and which participantID you want to delete.



Created by:

```
● Mario Durso
● Justin Hamilton
● Nick Napior
● Kojo Otchere-Addo
● Zhenghan Wang
```
