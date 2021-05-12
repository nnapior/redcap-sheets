var appId, developerKey, clientId;

var scope = ['https://www.googleapis.com/auth/drive.file'];

var pickerApiLoaded = false;

var pickedSheetID;

/*
	createPicker()
		Initializes and displays the Google Picker via the Google Picker API
		
		Parameters:
			None
		Returns:
			None
*/
function createPicker() {
	if(!window.localStorage.getItem("pickerCredToken")) {
		alert("please sign into google");
	} else {
	var oauthToken = atob(window.localStorage.getItem("pickerCredToken"));
	  if (pickerApiLoaded && oauthToken) {
		  console.log("1")
		var view = new google.picker.View(google.picker.ViewId.DOCS);
		view.setMimeTypes("application/vnd.google-apps.spreadsheet");
		var picker = new google.picker.PickerBuilder()
			.enableFeature(google.picker.Feature.NAV_HIDDEN)
			.enableFeature(google.picker.Feature.MULTISELECT_ENABLED)
			.setAppId(appId)
			.setOAuthToken(oauthToken)
			.addView(view)
			.addView(new google.picker.DocsUploadView())
			.setDeveloperKey(developerKey)
			.setCallback(pickerCallback)
			.build();
		 picker.setVisible(true);
	  }
  }
}

/*
	pickerCallBack(data)
		Receives the document selected via the Google Picker (createPicker()) and sets it as the export replacement target
		
		Parameters:
			data: The document(s) picked via the Google Picker
		Returns:
			None
*/
function pickerCallback(data) {
  if (data.action == google.picker.Action.PICKED) {
	console.log(data.docs[0]);
	pickedSheetID = data.docs[0].id;
	document.getElementById("sheetName").innerHTML = data.docs[0].name;
  }
}