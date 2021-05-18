var data;
var sheetID;

/*
	getUserInfo()
		Queries the server and returns returns the current Google user's information
		
		Parameters:
			None
		Returns:
			True if logged in, false otherwise
*/
function getUserInfo() {
	if(window.localStorage.getItem("googleCredData") != undefined && window.localStorage.getItem("googleCredKey") != undefined) {
		var r = new XMLHttpRequest();
		r.open("POST","/userinfo",true);
		r.setRequestHeader("Content-Type","application/json");
		r.onreadystatechange = function() {
			if(this.readyState == 4 && this.status == 200) {
				if(this.response != "-1") {
					var userData = JSON.parse(this.response);
					showUser(userData["name"], userData["picture"]);
					enableImport();
					enableExport();
					return true;
				} else {
					return false;
				}
			}
		}

		var pushObject = {
			"key":window.localStorage.getItem("googleCredKey"),
			"creds":window.localStorage.getItem("googleCredData")
		};
		var reqData = JSON.stringify(pushObject);
		reqData = reqData.replace("\n","");
		reqData = reqData.replace("'", "\"");

		r.send(reqData);
	} else {
		showSignInGoogle();
		disableImport();
		disableExport();
		return false;
	}
	
}

/*
	showUser(name, avatar_url)
		Styles and displays the Google login button to show the associated Google account's information
		
		Parameters:
			name: The name of the Google user currently logged in
			avatar_url: The URL of the current Google user's profile picture
		Returns:
			None
*/
function showUser(name, avatar_url) {
	var avatar = document.getElementById('avatar');
	var nameDiv = document.getElementById('userName');
	var signinBtn = document.getElementById('googleBtn');
	var userInfo = document.getElementById('userInfo');
	var googleAlert = document.getElementById("googleAccountAlert");
	avatar.style.backgroundImage = "url('"+avatar_url+"')";
	nameDiv.innerHTML = name;
	signinBtn.style.display = "none";
	userInfo.style.display = "block";
	avatar.style.display = "block";
	googleAlert.style.display = "none";
}

/*
	showSignInGoogle()
		Styles and displays the Google login button
		
		Parameters:
			None
		Returns:
			None
*/
function showSignInGoogle() {
	var signinBtn = document.getElementById('googleBtn');
	var userInfo = document.getElementById('userInfo');
	var googleAlert = document.getElementById("googleAccountAlert");
	userInfo.style.display = "none";
	signinBtn.style.display = "block";
	googleAlert.style.display = "block";
}

/*
	disableImport()
		Styles the Import card to disallow user interaction
		
		Parameters:
			None
		Returns:
			None
*/
function disableImport() {
	var importCard = document.getElementById('importCard');
	var importBtn = document.getElementById('importBtn');
	importCard.classList.add('cursor-not-allowed');
	importBtn.classList.add('disabled');
	document.getElementById("importMode").classList.add('cursor-not-allowed');
	document.getElementById("importMode").classList.add('disabled');
	document.getElementById("refreshSheetsButtonImport").classList.add('cursor-not-allowed');
	document.getElementById("refreshSheetsButtonImport").classList.add('disabled');
}

/*
	disableExport()
		Styles the Export card to disallow user interaction
		
		Parameters:
			None
		Returns:
			None
*/
function disableExport() {
	var exportCard = document.getElementById('exportCard');
	var exportBtn = document.getElementById('exportBtn');
	exportCard.classList.add('cursor-not-allowed');
	exportBtn.classList.add('disabled');
	document.getElementById("sheetMode").classList.add('cursor-not-allowed');
	document.getElementById("sheetMode").classList.add('disabled');
	document.getElementById("exportMode").classList.add('cursor-not-allowed');
	document.getElementById("exportMode").classList.add('disabled');
	document.getElementById("refreshSheetsButton").classList.add('cursor-not-allowed');
	document.getElementById("refreshSheetsButton").classList.add('disabled');
}

/*
	enableImport()
		Styles the Import card to allow user interaction
		
		Parameters:
			None
		Returns:
			None
*/
function enableImport() {
	var importCard = document.getElementById('importCard');
	var importBtn = document.getElementById('importBtn');
	importCard.classList.remove('cursor-not-allowed');
	importBtn.classList.remove('disabled');
	document.getElementById("importMode").classList.remove('cursor-not-allowed');
	document.getElementById("importMode").classList.remove('disabled');
	document.getElementById("refreshSheetsButtonImport").classList.remove('cursor-not-allowed');
	document.getElementById("refreshSheetsButtonImport").classList.remove('disabled');
	showImportEventCheckboxes(document.getElementById("importMode").value);
}

/*
	enableExport()
		Styles the Export card to allow user interaction
		
		Parameters:
			None
		Returns:
			None
*/
function enableExport() {
	var exportCard = document.getElementById('exportCard');
	var exportBtn = document.getElementById('exportBtn');
	exportCard.classList.remove('cursor-not-allowed');
	exportBtn.classList.remove('disabled');
	document.getElementById("sheetMode").classList.remove('cursor-not-allowed');
	document.getElementById("sheetMode").classList.remove('disabled');
	document.getElementById("exportMode").classList.remove('cursor-not-allowed');
	document.getElementById("exportMode").classList.remove('disabled');
	document.getElementById("refreshSheetsButton").classList.remove('cursor-not-allowed');
	document.getElementById("refreshSheetsButton").classList.remove('disabled');
	showEventCheckboxes(document.getElementById("exportMode").value);
	showSheetSelection(document.getElementById("sheetMode").value);
}

/*
	pageLoad()
		Runs whenever the webpage is loaded in a browser, redirects to Settings if REDCap API key is not entered
		
		Parameters:
			None
		Returns:
			None
*/
function pageLoad() {
	if(document.getElementById("dataContainer") != undefined) {
		var r = new XMLHttpRequest();
		r.open("GET", "/checkAPIKey", true);
		r.onreadystatechange = function() {
			if(this.status == 200 && this.readyState == 4) {
				if(this.response != "-1") {
					getData();
					getUserInfo();
				} else {
					window.location = "/settings";
				}
			}
		}
		r.send();
	}
}

/*
	showParticipant(eventKey, participantID)
		Shows a particular participant's data for a REDCap event and adds it to the data preview
		
		Parameters:
			eventKey: The key of the REDCap event for which the participant data is drawn from
			participantID: The ID of the specific participant whose data to show, or "all" to show all participants
		Returns:
			None
*/
function showParticipant(eventKey, participantID) {
	// Populate table keys
	var tableKeys = document.getElementById("table-keys");
	var keys = Object.keys(data[eventKey][1]); // get keys from data object
	var outputStr = "<th>delete</th>\n";
	// add keys to table
	for(key of keys) {
		outputStr +="<th>"+key+"</th>\n";
	}
	tableKeys.innerHTML = outputStr;
	outputStr = ""; // reset outputStr to be used for table body

	var tableBody = document.getElementById("table-body");
	tableBody.innerHTML = ""; // clear current table body
	// populate table with all participants if "all" option is passed in as ID
	if(participantID=="all"){
		for(participant in data[eventKey]) {
			var btn = document.createElement("BUTTON");
			btn.innerHTML = "delete";
			btn.classList.add('btn');
			btn.classList.add('btn-danger');
			btn.setAttribute('onclick', "deleteUser("+participant+")");
			outputStr += "<tr>\n<td>"+btn.outerHTML+"</td>\n"; // new table entry
			// add all the values for this entry
			for(key of keys) {
				outputStr +="<td>"+data[eventKey][participant][key]+"</td>\n";
			}
			outputStr += "</tr>\n"; // close table entry
		}
	}
	// else, just print the passed in ID
	else {
		var btn = document.createElement("BUTTON");
		btn.innerHTML = "delete";
		btn.classList.add('btn');
		btn.classList.add('btn-danger');
		btn.setAttribute('onclick', "deleteUser("+participantID+")");
		outputStr += "<tr>\n<td>"+btn.outerHTML+"</td>\n"; // new table entry
		for(key of keys) {
			outputStr +="<td>"+data[eventKey][participantID][key]+"</td>\n";
		}
		outputStr += "</tr>\n";
	}
	tableBody.innerHTML = outputStr; // update table body
}

/*
	exportData
		Gathers the events to export to Google Sheets from REDCap and pushes them to pushToSheets(object)
		
		Parameters:
			None
		Returns:
			None
*/
function exportData() {
	//Function that gets the json data ready to push to sheets
	var exportMode = document.getElementById("exportMode").value;

	if(exportMode == "select") {
		//export only selected events"
		var newObject = {};
		var checkboxes = document.getElementsByClassName("eventSelectionCheckbox");
		for(checkbox of checkboxes) {
			if(checkbox.checked) {
				newObject[checkbox.value] = data[checkbox.value];
			}
		}
		pushToSheets(newObject);
	} else {
		//export all events in data
		pushToSheets(data);
	}
	
	
}
/*
	importData
		Gathers the events to import to REDCap from Google Sheets and pushes them to pushToRedcap(object)
		
		Parameters:
			None
		Returns:
			None
*/
function importData() {
	var importMode = document.getElementById("importMode").value;

	if(importMode == "select") {

		var newObject = {};
		var checkboxes = document.getElementsByClassName("eventImportSelectionCheckbox");
		for(checkbox of checkboxes) {
			if(checkbox.checked) {
				newObject[checkbox.value] = data[checkbox.value];
			}
		}

		pushToRedcap(newObject)

	} else {
		pushToRedcap("All Events");
	}
}

/*
	pushToRedcap(object)
		Writes Google Sheets data to REDCap with the selected import mode
		
		Parameters:
			object: The Google Sheets data to be exported
		Returns:
			None
*/
function pushToRedcap(object) {
	var sheetID = document.getElementById("importSheetIDSelect").value;
	var r = new XMLHttpRequest();
	var importBtn = document.getElementById('importBtn');
	r.open("POST","/import_sheets_to_redcap",true);
	r.setRequestHeader("Content-Type","application/json");
	r.onreadystatechange = function() {
		if(this.readyState == 4 && this.status == 200) {
			importBtn.classList.remove("btn-loading");
		}
	}

	if(window.localStorage.getItem("googleCreds") != undefined && sheetID != "") {
		var pushObject = {"events":object, "id":pickedImportSheetID, "creds":window.localStorage.getItem("googleCreds")};
		console.log(pushObject);
		var reqData = JSON.stringify(pushObject);
		reqData = reqData.replace("\n","");
		reqData = reqData.replace("'", "\"");
		importBtn.classList.add("btn-loading");
		r.send(reqData);
	} else {
		alert("failed to import data from sheets. Please sign into google");
	}
}

/*
	pushToSheets(object)
		Writes REDCap data to Google Sheets with the selected export mode
		
		Parameters:
			object: The REDCap data to be exported
		Returns:
			None
*/
function pushToSheets(object) {

	if(window.localStorage.getItem("googleCredData") != undefined && window.localStorage.getItem("googleCredKey") != undefined) {
		document.getElementById("export-btn-icon").classList.add("btn-loading");
		//if we're doing sheet destination control, use this outline
		var sheetDestination = document.getElementById("sheetMode").value;
		var exportBtn = document.getElementById('exportBtn');
		if(sheetDestination == "new") {
			//put code to create/write to a new sheet here
			console.log("writing to new sheet");
			var pushObject = {
				"mode":"new",
				"object":object,
				"key":window.localStorage.getItem("googleCredKey"),
				"creds":window.localStorage.getItem("googleCredData")
			};

			var r = new XMLHttpRequest();
			var spreadsheet_address = "https://docs.google.com/spreadsheets/d/";
			r.open("POST","/pushData",true);
			r.setRequestHeader("Content-Type","application/json");
			r.onreadystatechange = function() {
				if(this.readyState == 4 && this.status == 200) {
					var id = this.response;
					exportBtn.classList.remove("btn-loading");
					window.open(spreadsheet_address+this.response);
					document.getElementById("export-btn-icon").classList.remove("btn-loading");
				}
			}

			var reqData = JSON.stringify(pushObject);
			reqData = reqData.replace("\n","");
			reqData = reqData.replace("'", "\'");

			console.log(reqData);

			r.send(reqData);
		} else {
			if(pickedSheetID) {
				switch(sheetDestination) {
					case "replace":
						//put code to replace an existing sheet's data here

						var pushObject = {
							"mode":"replace",
							"id":pickedSheetID,
							"object":object,
							"key":window.localStorage.getItem("googleCredKey"),
							"creds":window.localStorage.getItem("googleCredData")
						};

						var r = new XMLHttpRequest();
						var spreadsheet_address = "https://docs.google.com/spreadsheets/d/";
						r.open("POST","/pushData",true);
						r.setRequestHeader("Content-Type","application/json");
						r.onreadystatechange = function() {
							if(this.readyState == 4 && this.status == 200) {
								var id = this.response;
								exportBtn.classList.remove("btn-loading");
								window.open(spreadsheet_address+this.response);
								document.getElementById("export-btn-icon").classList.remove("btn-loading");
							}
						}

						var reqData = JSON.stringify(pushObject);
						reqData = reqData.replace("\n","");
						reqData = reqData.replace("'", "\"");

						r.send(reqData);

						break;
					default:
						alert("there was an error exporting to an existing sheet: unknown export mode");

						document.getElementById("export-btn-icon").classList.remove("btn-loading");
						break;
				}
			} else {

				document.getElementById("export-btn-icon").classList.remove("btn-loading");
				alert("there was an error exporting to an existing sheet: sheet not selected");
			}
		}
	} else {

		document.getElementById("export-btn-icon").classList.remove("btn-loading");
		alert("there was an error exporting to an existing sheet: not signed in to google");
	}
}

/* 
showEventCheckboxes(value)
	Displays the event checkboxes for exporting if exporting only selected events
	
	Parameters:
		value: The value of the export mode selection (all/select)
	Returns:
		None
*/
function showEventCheckboxes(value) {
	var eventCheckboxes = document.getElementById("exportEventContainer");
	if(value == "select") {
		eventCheckboxes.style.display = "block";
	} else {
		eventCheckboxes.style.display = "none";
	}
}

/* 
	showImportEventCheckboxes(value)
		Displays the event checkboxes for importing if importing only selected events
		
		Parameters:
			value: The value of the import mode selection (all/select)
		Returns:
			None
*/
function showImportEventCheckboxes(value) {
	var eventCheckboxes = document.getElementById("importEventContainer");
	if(value == "import-select") {
		eventCheckboxes.style.display = "block";
	} else {
		eventCheckboxes.style.display = "none";
	}
}

/*
	showEvent(eventKey)
		Shows the REDCap data for the selected event
		
		Parameters:
			eventKey: The key of the event whose data will be displayed
		Returns:
			None
*/
function showEvent(eventKey) {
	var object = data[eventKey];
	var keys = Object.keys(object);
	var selection = document.getElementById("participantSelection");
	selection.innerHTML = "";
	selection.oninput = function() {
		showParticipant(eventKey, this.value);
	}
	var option = document.createElement("option");
	option.value = "all";
	option.innerHTML = "all";
	selection.appendChild(option);
	for(key of keys) {
		var option = document.createElement("option");
		option.value = key;
		option.innerHTML = key;
		selection.appendChild(option);
	}
	selection.value = "all";
	showParticipant(eventKey, "all");
}

/*
	setButtons(object)
		Sets the event selection checkboxes for exporting and importing, and sets the event dropdown for the data preview
		
		Parameters:
			object: The JSON object containing the event names
		Returns:
			None
*/
function setButtons(object) {
	var keys = Object.keys(object);
	var buttons = document.getElementById("eventSelection");
	buttons.innerHTML = "";
	buttons.oninput = function() {
		showEvent(this.value);
	}

	var eventCheckboxes = document.getElementById("selectedEvents");
	var eventImportCheckboxes = document.getElementById("selectedImportEvents");

	for(key of keys) {
		var option = document.createElement("option");
		option.value = key;
		option.innerHTML = key;
		buttons.appendChild(option);

		var label = document.createElement("label");
		label.className = "form-selectgroup-item";
		
		var checkbox = document.createElement("input");
		checkbox.type = "checkbox";
		checkbox.className = "form-selectgroup-input";
		checkbox.value = key;
		checkbox.name = "selectedEvents"
		checkbox.checked = true;
		
		var div = document.createElement("div");
		div.className = "form-selectgroup-label";
		
		var checkContainer = document.createElement("div");
		checkContainer.className = "me-3";
		
		var checkBoxElement = document.createElement("span");
		checkBoxElement.className = "form-selectgroup-check";
		
		var labelContainer = document.createElement("div");
		labelContainer.className = "form-selectgroup-label-content d-flex align-items-center";
		labelContainer.innerHTML = key;
		
		checkContainer.appendChild(checkBoxElement);
		div.appendChild(checkContainer);
		div.appendChild(labelContainer);
		
		label.appendChild(checkbox);
		label.appendChild(div);
		eventCheckboxes.appendChild(label);
		
		// var label = document.createElement("label");
		// label.htmlFor = key;
		// label.innerHTML = key;
		// eventCheckboxes.appendChild(checkbox);
		// eventCheckboxes.appendChild(label);
		// eventCheckboxes.appendChild(document.createElement("br"));

		// eventImportCheckboxes.appendChild(label);
		
		label = document.createElement("label");
		label.className = "form-selectgroup-item";
		
		checkbox = document.createElement("input");
		checkbox.type = "checkbox";
		checkbox.className = "form-selectgroup-input";
		checkbox.value = key;
		checkbox.name = "selectedEvents"
		checkbox.checked = true;
		
		div = document.createElement("div");
		div.className = "form-selectgroup-label";
		
		checkContainer = document.createElement("div");
		checkContainer.className = "me-3";
		
		checkBoxElement = document.createElement("span");
		checkBoxElement.className = "form-selectgroup-check";
		
		labelContainer = document.createElement("div");
		labelContainer.className = "form-selectgroup-label-content d-flex align-items-center";
		labelContainer.innerHTML = key;
		
		checkContainer.appendChild(checkBoxElement);
		div.appendChild(checkContainer);
		div.appendChild(labelContainer);
		
		label.appendChild(checkbox);
		label.appendChild(div);
		eventImportCheckboxes.appendChild(label);
	}
	buttons.value = keys[0];
	showEvent(keys[0]);
}

/*
	showSheetSelection(value)
		Displays the export location (spreadsheet) if exporting to an existing spreadsheet
		
		Parameters:
			value: The value of the export mode selection (new/existing)
		Returns:
			None
*/
function showSheetSelection(value) {
	//showSheetSelection
	//Function that gets sheet selection based on sheet ID
	//Parameters: value:

	let sheetSelection = document.getElementById("sheetSelection");
	if(value == "new") {
		sheetSelection.style.display = "none";
	} else {
		sheetSelection.style.display = "block";
	}
}

/*
	deleteUser(id)
		Deletes a record from the current REDCap project
		
		Parameters:
			id: The ID of the record to be deleted
		Returns:
			None
*/
function deleteUser(id) {
	var r = new XMLHttpRequest();
	r.open("POST", "/delete_record_redcap", true);
	r.setRequestHeader("Content-Type","application/json");

	r.onreadystatechange = function() {
		if(this.status == 200 && this.readyState == 4) {
			getData();
		}
	}

	var pushObject = {"id":id};
	var reqData = JSON.stringify(pushObject);
	reqData = reqData.replace("\n","");
	reqData = reqData.replace("'", "\"");

	r.send(reqData);
}

/*
	getData()
		Queries the server and pulls records from the REDCap project associated with the inputted API key
		
		Parameters:
			None
		Returns:
			True if data was returned, false otherwise
*/
function getData() {
	//getData
	//Function that retrieves data

	document.getElementById("refresh-btn").classList.add("btn-loading");
	var r = new XMLHttpRequest();
	r.open("GET", "/pullData", true);
	r.onreadystatechange = function() {
		if(this.status == 200 && this.readyState == 4) {
			if(this.response != -1) {
				var parsedRes = JSON.parse(r.response);
				data = parsedRes;
				setButtons(data);
			}

			document.getElementById("refresh-btn").classList.remove("btn-loading");
		}
	}
	r.send();
}

/*
	getRedCapAPIKey()
		Toggles visibility of the inputted REDCap API key on the Settings page
		
		Parameters:
			None
		Returns:
			None
*/
function getRedCapAPIKey(){
	var x = document.getElementById("key");
	if (x.style.visibility === "visible") {
    	x.style.visibility = "hidden";
  	} else {
    	x.style.visibility = "visible";
  	}
}
