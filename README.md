# REDCap Google Sheets

Created by:

```
● Mario Durso
● Justin Hamilton
● Nick Napior
● Kojo Otchere-Addo
● Zhenghan Wang
```
### Introduce:

Thanks for using our webapp.Thisweb application usedto interact with the REDcap API

### What can you do using this web app?

1.Export data to Google sheets.
2.Import data from Google sheets to REDCap.
3.Delete data from REDCap.

## Dependencies

Install therequirements.txtfile withpip install-r requirements.txt

```
● Usepip3on MacOS. ex.pip3 install -r requirements.txt
```
Using all commands below to install all modules.
pip install pandas

pip install --upgrade google-api-python-client google-auth-httplib2google-auth-oauthlib

pip install pycap


## Configuration

**if you use these scripts, you need aconfig.jsonfileinconfig/with the following
contents:**

**{
"api_key":"your-api-key",
"api_url":"link-to-REDCap-API",
"spreadsheet_id": "your-spreadsheet-id"
}**

**The user will also need aclinet_secret.jsonfileinconfig/.**

```
● To get the client secret.json you must go to:
https://console.cloud.google.com/home/dashboard
● On this page click:
○ Navigation Menu->APIs & Services->Credentials ->Desktopclient 1
● On this page click:
○ "DOWNLOAD JSON" Move this file into your project directory
```
### What do you need?

1. A Google account named Which has the right to editGoogle Sheets.
2. A RedCap account and API key
3. Install the above Requirements
4. UD VPN


### After installing the commands above.

## Running the webapp

1. Login to your UD VPN

2.Run this python script with the following:
**python app.py**


3.Copy this link to your website. (and do not exist this window)

4.Then you will come to this page.


5.Next, log in to your Google account with the red button at the top right

6.When you log into your Google account, agree toall options, permissions, and continue.


7.Next, Go to the setting at the top left

8.Then submit your RedCap API


9.After you submit your REDCap API, it will show thatREDCap Api key entered successfully!
Then back to the home page in the top left

**Congratulations, you've completed all the steps. Nowyou can start using this
app!!!**


### Help on how to use all the features.

**1.How to export data to Google sheets.**
1.In the lower right section, you can export datato Google Sheets.


2. You can export all events or you can select the data which you want to. And also to choose
the target sheet. Finally, click Export button

**2.How to import data from Google sheets to REDCap.**
1.In the lower left section, you can import data fromGoogle Sheets to REDCap


2. You can import all events to REDCap or you can select the data which you want to. And also
to choose the target sheet. Finally, click ImportButton

**3.How to delete data from REDCap.**
1.In the middle section, you can delete data from REDCap


2. You can click the delete button (red one) to deletethe data, but make sure that you have
permission to delete those. If you don't have permission,it will show “you don't have permission
to delete”. If you have permission to delete, it willshow “delete successfully.”
3. You can choose which event, and which participantID you want to delete.


