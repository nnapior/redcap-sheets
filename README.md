**REDCap Google Sheets**


**Introduce:**

Thanks for using our webapp.This web application used to interact with the REDcap API

**What can you do using this web app?**

1.Export data to Google sheets.

2.Import data from Google sheets to REDCap. 3.Delete data from REDCap.

**Dependencies**

Install therequirements.txt file withpip install -r requirements.txt

- Usepip3 on MacOS. ex.pip3 install -r requirements.txt

Using all commands below to install all modules.

pip install pandas

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

pip install pycap

**Configuration**

**if you use these scripts, you need aconfig.json file inconfig/ with the following contents:**

**{**

**"api\_key":"your-api-key",**

**"api\_url":"link-to-REDCap-API",**

**"spreadsheet\_id": "your-spreadsheet-id"**

**}**

**The user will also need aclinet\_secret.json file inconfig/.**

- **To get the client secret.json you must go to: [https://console.cloud.google.com/home/dashboard**](https://console.cloud.google.com/home/dashboard)**
- **On this page click:**
  - **Navigation Menu->APIs & Services->Credentials ->Desktop client 1**
- **On this page click:**

**○ "DOWNLOAD JSON" Move this file into your project directory**

**What do you need?**

1. A Google account named Which has the right to edit Google Sheets.
1. A RedCap account and API key
1. Install the above Requirements
1. UD VPN

**After installing the commands above.**

**Running the webapp**

1. Login to your UD VPN

![](Aspose.Words.4047b0ed-f889-4645-a411-3ef0feff086c.001.png)

2.Run this python script with the following:![](Aspose.Words.4047b0ed-f889-4645-a411-3ef0feff086c.002.jpeg)

**python app.py**

3.Copy this link to your website. (and do not exist this window)

![](Aspose.Words.4047b0ed-f889-4645-a411-3ef0feff086c.003.jpeg)

4.Then you will come to this page.

![](Aspose.Words.4047b0ed-f889-4645-a411-3ef0feff086c.004.jpeg)

5.Next, log in to your Google account with the red button at the top right

![](Aspose.Words.4047b0ed-f889-4645-a411-3ef0feff086c.005.jpeg)

6.When you log into your Google account, agree to all options, permissions, and continue.

7.Next, Go to the setting at the top left

![](Aspose.Words.4047b0ed-f889-4645-a411-3ef0feff086c.006.jpeg)

8.Then submit your RedCap API

![](Aspose.Words.4047b0ed-f889-4645-a411-3ef0feff086c.007.jpeg)9.After you submit your REDCap API, it will show that REDCap Api key entered successfully! Then back to the home page in the top left

![](Aspose.Words.4047b0ed-f889-4645-a411-3ef0feff086c.008.jpeg)

**Congratulations, you've completed all the steps. Now you can start using this app!!!**

**Help on how to use all the features.**

**1.How to export data to Google sheets.**

1.In the lower right section, you can export data to Google Sheets.

![](Aspose.Words.4047b0ed-f889-4645-a411-3ef0feff086c.009.png)![](Aspose.Words.4047b0ed-f889-4645-a411-3ef0feff086c.010.jpeg)

2. You can export all events or you can select the data which you want to. And also to choose the target sheet. Finally, click Export button

![](Aspose.Words.4047b0ed-f889-4645-a411-3ef0feff086c.011.jpeg)

**2.How to import data from Google sheets to REDCap.**

1.In the lower left section, you can import data from Google Sheets to REDCap

![](Aspose.Words.4047b0ed-f889-4645-a411-3ef0feff086c.012.png)![](Aspose.Words.4047b0ed-f889-4645-a411-3ef0feff086c.013.jpeg)2. You can import all events to REDCap or you can select the data which you want to. And also to choose the target sheet. Finally, click Import Button

![](Aspose.Words.4047b0ed-f889-4645-a411-3ef0feff086c.014.jpeg)

**3.How to delete data from REDCap.**

1.In the middle section, you can delete data from REDCap

![](Aspose.Words.4047b0ed-f889-4645-a411-3ef0feff086c.015.png)![](Aspose.Words.4047b0ed-f889-4645-a411-3ef0feff086c.016.jpeg)

2. You can click the delete button (red one) to delete the data, but make sure that you have permission to delete those. If you don't have permission, it will show “you don't have permission to delete”. If you have permission to delete, it will show “delete successfully.”
2. You can choose which event, and which participant ID you want to delete.



Created by:

- Mario Durso
- Justin Hamilton
- Nick Napior
- Kojo Otchere-Addo
- Zhenghan Wang
