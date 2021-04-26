# REDCap Google Sheets
Creates a web application to interact with the REDcap and Google Sheets/Drive

## Features
`TODO: add Features list`


## Dependencies
Install the `requirements.txt` file with `pip install -r requirements.txt`
* Use `pip3` on MacOS. ex. `pip3 install -r requirements.txt`


## Configuration
if you use these scripts, you need a `config.json` file in `config/` with the following contents:
```
{
	"api_key":"your-api-key",
	"api_url":"link-to-REDCap-API",
	"spreadsheet_id": "your-spreadsheet-id",
	...
}
```

### Configuration variables
* `api_key`: REDCap API key. (**Note**) This is only required for development
* `spreadsheet_id`: Google sheets ID. (**Note**) This is only required for development
	* ex. if the url to your sheet is `https://docs.google.com/spreadsheets/d/1fEncz_68ktr-o7CQd5TfYrv1AfKfJUPuWg0dv4HLgQA/edit#gid=80956627` then your sheet ID is `1fEncz_68ktr-o7CQd5TfYrv1AfKfJUPuWg0dv4HLgQA`
* `api_url`: URL to your REDCap api. **Required**
* `client_secret`: Path to `client_secret.json`. **Required**
	* ex. `./config/client_secret.json`
* `secret_key`: secret key for Flask cookie encryption. **Required**
	* generate this key by using the python interpreter:
	```
	$ python3
	Python 3.9.4 (default, Apr  5 2021, 01:50:46)
	[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>> import secrets
	>>> secrets.token_urlsafe(16)
	'V4A5q52Bbe9WEc4f81i4iw' <-- THIS OUTPUT IS YOUR SECRET KEY. DO NOT SHARE
	>>> exit()
	```
* `base_url`: base_url of webapp. **Required**
	* if you're using `python app.py` your `base_url` should be `http://localhost:5000/`
	* if you're using `docker` it should be something like `http://<docker-host-ip>:<target-server-port>`
	or `http://example.com:<target-server-port>/` where `example.com` resolves to the docker host

### Google Cloud Platform
The user will also need a `client_secret.json` file in `config/`.
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


## Deploying on docker
* **prerequisite** You must have `docker` installed and Running. See more at https://docs.docker.com/get-docker/
	* confirm by running `docker ps` and you should receive the output of something like
	```
	CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
	```
* Clone this repository somewhere on your machine and `cd ../../wherever-this-repo-is`
* Build the docker image with `docker build --tag redcap-sheets .`
* after the image is built create a `config/` somewhere on your machine (even in this repository folder)
 	* Follow the instructions in Configuration above to create `config/config.json` and `config/client_secret.json`
* Run the container with `docker run -d -p <target-server-port>:8080 -v ../location/to/config:/app/config redcap-sheets:latest`
* Verify it is running by running `docker ps` again, except this time we should see something like
```
CONTAINER ID   IMAGE                  COMMAND           CREATED         STATUS         PORTS                    NAMES
8fa21640a09f   redcap-sheets:latest   "./gunicorn.sh"   4 seconds ago   Up 3 seconds   0.0.0.0:8080->8080/tcp   beautiful_shockley
```
* You can now stop,start,restart,delete,etc. by using the `CONTAINER ID`.
	* ex. `docker stop 8fa21640a09f`
