# REDCap Google Sheets

### Introduce:

Thanks for using our webapp. This web application used to import and export data with the REDcap and google sheets.

### What can you do using this web app?

1.Export data to Google sheets.


3.Import data from Google sheets to REDCap.


5.Delete data from REDCap.

## Dependencies

Install the requirements.txt file with 
```
pip install-r requirements.txt
```
Using the command below for pip3 on MacOS. ex.
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

**The user will also need a ```clinet_secret.json ```file in ```config/```.**

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

## Running the webapp on an already hosted server

1. Login to your UD VPN

![image](https://user-images.githubusercontent.com/54848986/117843794-b9238380-b2b1-11eb-903c-0144cc3780e1.png)

2. Go to following link http://redcap.cis.udel.edu/

## Running the webapp when not hosted

1.Run this python script with the following:
**python app.py**

![image](https://user-images.githubusercontent.com/54848986/117843979-e2dcaa80-b2b1-11eb-9a53-2e34b0944943.png)

2.Copy this link to your website. (and do not exist this window)

![image](https://user-images.githubusercontent.com/54848986/117844048-f4be4d80-b2b1-11eb-947a-915fa9641b19.png)

3.Then you will come to this page.

![image](https://user-images.githubusercontent.com/54848986/117844116-01db3c80-b2b2-11eb-848e-c761e281abae.png)

4.Next, log in to your Google account with the red button at the top right

![image](https://user-images.githubusercontent.com/54848986/117844214-13244900-b2b2-11eb-964a-862d404159bb.png)

5.When you log into your Google account, agree toall options, permissions, and continue.


6.Next, Go to the setting at the top left

![image](https://user-images.githubusercontent.com/54848986/117844305-29320980-b2b2-11eb-93d0-488e849b4041.png)

7.Then submit your RedCap API

![image](https://user-images.githubusercontent.com/54848986/117845738-677bf880-b2b3-11eb-8479-a152f9ceeec4.png)

8.After you submit your REDCap API, it will show thatREDCap Api key entered successfully!
Then back to the home page in the top left

![image](https://user-images.githubusercontent.com/54848986/117845829-78c50500-b2b3-11eb-9113-6890916ee4d9.png)

**Congratulations, you've completed all the steps. Nowyou can start using this
app!!!**


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
