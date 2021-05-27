# importing modules
import pandas
import json
from redcap import Project
from cryptography.fernet import Fernet
from lib.Google import Create_Service


def createService(creds):
    """
    THis funciton creates google sheets service
    :return: service object
    """
    CLIENT_SECRET_FILE = "client_secret.json"
    API_NAME = 'sheets'
    API_VERSION = 'v4'
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets",
              'https://www.googleapis.com/auth/drive']

    # create google sheet service object
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, creds, SCOPES)
    return service


def getConfig():
    """This function returns the configuration data in json form
    :returns config"""
    file = open("config/config.json", "r")
    config = json.load(file)
    file.close()
    return config


def getEvents(google_service, sheetID):
    """This function get all the sheet events from google sheets
    :return events list"""
    service = google_service
    ''' if google_service == None:
        service = createService()
    else:
        service = google_service
    config = getConfig()'''

    # request for google sheets data and extract the sheeets names
    sheet_metadata = service.spreadsheets().get(spreadsheetId=sheetID).execute()
    sheets_info = sheet_metadata.get('sheets', '')
    events = [sheets_info[x].get("properties", {}).get("title", "Sheet1")
              for x in range(len(sheets_info))]

    return events


def import_redcap(sheet, service, project, sheetID):
    """
    This funciton import records to redcap
    return: Successfull/Failed
    """

    # config = getConfig()
    # request for particular sheet data
    request = service.spreadsheets().values().get(spreadsheetId=sheetID, majorDimension='ROWS',
                                                  range=sheet).execute()
    rows = request['values']

    # create dataframe from rows get from sheet
    df = pandas.DataFrame(rows[1:], columns=rows[0])
    df = df.replace(to_replace="n/a", value="")

    # create dict from dataframe
    rows = df.to_dict(orient='records')

    try:
        # iterate through each record from rows: dict
        for row in rows:
            row["redcap_event_name"] = sheet  # append event name to record
            rec = json.dumps(row)  # converting record to  json format
            data = [json.loads(rec)]  # load json object and put that in list
            # print(data)
            response = project.import_records(to_import=data)  # import record to redcap api
            print(response)
    except Exception as e:
        print(e)
        return "Import Data to RedCap Failed because "
    return "Import Data to RedCap Successful"


def import_data(object, apiKey, api_url):
    """
    Function that imports data to Redcap

    Parameters
    Object : list of redcap data

    Returns
    Imported data
    """

    imported = False
    events = object['events']
    sheetID = object['id']
    encCreds = bytes(object["creds"].encode("utf-8"))
    print(object["key"])
    key = bytes(object["key"].encode("utf-8"))
    print(key)

    fernet = Fernet(key)

    creds = fernet.decrypt(encCreds).decode()
    service = createService(creds)

    # config = getConfig()

    project = Project(api_url, apiKey)

    if events == "All Events":
        events = getEvents(service, sheetID)
        for event in events:
            response = import_redcap(event, service, project, sheetID)
            if response == "Import Data to RedCap Successful":
                imported = response
                continue
            else:
                return response

    else:
        for event in events:
            response = import_redcap(event, service, project, sheetID)
            if response == "Import Data to RedCap Successful":
                imported = response
                continue
            else:
                return response
    return imported


if __name__ == "__main__":
    print(import_data(["initial_data_arm_1"]))
