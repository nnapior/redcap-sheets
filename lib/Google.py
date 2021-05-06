import pickle
import os
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request
import io
import codecs
import requests
from cryptography.fernet import Fernet
import json


def authGoogle(client_secret_file, scopes, redirect_uri):
    # Create flow instance to manage the OAuth 2.0 Authorization Grant Flow steps.
    flow = Flow.from_client_secrets_file(client_secret_file, scopes=scopes)
    # The URI created here must exactly match one of the authorized redirect URIs
    # for the OAuth 2.0 client, which you configured in the API Console. If this
    # value doesn't match an authorized URI, you will get a 'redirect_uri_mismatch'
    # error.
    flow.redirect_uri = redirect_uri

    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true')

    return (authorization_url, state)


def authGoogleComplete(client_secret_file, scopes, state, response, redirect_uri):
    flow = Flow.from_client_secrets_file(client_secret_file, scopes=scopes, state=state)
    flow.redirect_uri = redirect_uri

    flow.fetch_token(authorization_response=response)
    creds = flow.credentials
    content = codecs.encode(pickle.dumps(creds), "base64").decode()
    key = Fernet.generate_key()
    print(key)

    fernet = Fernet(key)

    encrypted = fernet.encrypt(content.encode())

    object = {}

    object["key"] = key.decode("utf-8")
    object["data"] = encrypted.decode("utf-8")

    # print(object)

    return json.dumps(object)


def signOutGoogle(credData, key):
    encCreds = bytes(credData.encode("utf-8"))
    key = bytes(key.encode("utf-8"))
    print(key)

    fernet = Fernet(key)

    creds = pickle.loads(codecs.decode(fernet.decrypt(encCreds), "base64"))

    requests.post('https://oauth2.googleapis.com/revoke',
                  params={'token': creds.token},
                  headers={'content-type': 'application/x-www-form-urlencoded'})
    return "1"


def signInGoogle(client_secret_file, api_name, api_version, *scopes):
    print(client_secret_file, api_name, api_version, scopes, sep='-')
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]
    cred = None

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        content = codecs.encode(pickle.dumps(cred), "base64").decode()

        key = Fernet.generate_key()
        print(key)

        fernet = Fernet(key)

        encrypted = fernet.encrypt(content.encode())

        object = {}

        object["key"] = key.decode("utf-8")
        object["data"] = encrypted.decode("utf-8")

        print(object)

        return json.dumps(object)


def Create_Service(client_secret_file, api_name, api_version, credData, *scopes):
    '''
    Create_Service
        Function that returns

        Paramaters:
            client_secret_file : String name of the json file containing api access information
            api_name : String name of the google API being accessed
            api_version : String Version number of the api used
            scopes : List of strings indicating the scope of the API service

        Returns a service object to interface with google api
    '''
    print(client_secret_file, api_name, api_version, scopes, sep='-')
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]
    print(SCOPES)
    cred = pickle.loads(codecs.decode(credData.encode(), "base64"))
    print(cred)

    # pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'
    # print(pickle_file)

    # if os.path.exists(pickle_file):
    #     with open(pickle_file, 'rb') as token:
    #         cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        # with open(pickle_file, 'wb') as token:
        #     pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print(API_SERVICE_NAME, 'service created successfully')
        return service
    except Exception as e:
        print('Unable to connect.')
        print(e)
        return None


def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    '''
    convert_to_RFC_datetime
        Function that returns a datatime string for January 1st, 1900
    '''
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt
