import requests
import json
import os

# global variable for url
url = "https://dri.udel.edu/redcap/api/"

"""
getWorksheetID
    Function that takes in an api key and returns a json object containing the database

    Parameters:
        apiKey : api key for REDCap project

    returns a json object containing the data from a redcap database
"""
def getRecords(apiKey):
    """
    function to get the project records from the database
    """
    # set up request
    data = {
        'token': apiKey,
        'content': 'record',
        'format': 'json',
        'type': 'flat'
    }

    # make the request
    r = requests.post(url, data=data)

    # is the result ok?
    if(r.status_code == 200):
        # create a json object from the result and return it
        jsonObject = json.loads(r.text)
        return jsonObject
    # if not, print the error and return None
    else:
        print("error "+str(r.status_code)+": "+r.text)
        return None

"""
getAPIKey
    Function that opens a config.json file in the same directory and returns the REDCap API key

    Returns a string object containing the api key
"""
def getAPIKey():
    configFile = open("config.json", "r")
    content = json.loads(configFile.read())
    return content["api_key"]

"""
getProjName
    Function that takes in an api key and returns the title of the REDCap project

    Parameters:
        apiKey : api key for REDCap project

    Returns a string of the title of the REDCap project name
"""
def getProjName(apiKey = getAPIKey()):
    data = {
        'token': apiKey,
        'content': 'project',
        'format': 'json',
        'returnFormat': 'json'
    }
    r = requests.post(url, data=data)
    print('HTTP Status: ' + str(r.status_code))
    return r.json()['project_title']

"""
getValues
    Function that returns the data in a redcap project as a json by reading the api key in config.json


    Returns a json object containing the data within a REDCap
"""
def getValues():
    # get the api key from config.json
    apiKey = getAPIKey()

    # get the raw records object
    jsonObject = getRecords(apiKey)

    # initiate output object
    outputObject = {}

    # for each record...
    i = 1
    for item in jsonObject:
        # save the event name and participant id
        participantID = item["participant_id"]
        eventName = item["redcap_event_name"]

        recordOutputObject = {
            "participant_id": participantID
        }

        # get the keys of the record dictionary
        keys = list(item.keys())

        # for each key in the record (except participant id and event name)...
        for key in keys[2:]:
            # if value is blank, write "n/a". else write the value to the record object
            if(item[key] == ''):
                recordOutputObject[key] = "n/a"
            else:
                recordOutputObject[key] = item[key]

        # if event name is already in output JSON, append the new record. else add the event to the output JSON
        if(eventName in outputObject):
            outputObject[eventName][participantID] = recordOutputObject
        else:
            outputObject[eventName] = {participantID: recordOutputObject}

    # prettyprint json
    # return(outputObject.get('initial_data_arm_1').get('1').keys())
    return(json.dumps(outputObject, indent=4, sort_keys=False))

"""
getValues
    Function that returns the data in a redcap project as a python dictionary by reading the api key in config.json


    Returns a python dictionary object containing the data within a REDCap
"""
def getValueDict():
    # get the api key from config.json
    apiKey = getAPIKey()

    # get the raw records object
    jsonObject = getRecords(apiKey)

    # initiate output object
    outputObject = {}

    # for each record...
    i = 1
    for item in jsonObject:
        # save the event name and participant id
        participantID = item["participant_id"]
        eventName = item["redcap_event_name"]

        recordOutputObject = {
            "participant_id": participantID
        }

        # get the keys of the record dictionary
        keys = list(item.keys())

        # for each key in the record (except participant id and event name)...
        for key in keys[2:]:
            # if value is blank, write "n/a". else write the value to the record object
            if(item[key] == ''):
                recordOutputObject[key] = "n/a"
            else:
                recordOutputObject[key] = item[key]

        # if event name is already in output JSON, append the new record. else add the event to the output JSON
        if(eventName in outputObject):
            outputObject[eventName][participantID] = recordOutputObject
        else:
            outputObject[eventName] = {participantID: recordOutputObject}

    # prettyprint json
    return(outputObject)


# main function
if __name__ == "__main__":
    # print(getValues())

    print(getValueDict())
