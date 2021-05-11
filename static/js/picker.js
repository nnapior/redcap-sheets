// The Browser API key obtained from the Google API Console.
// Replace with your own Browser API key, or your own key.
var developerKey = 'AIzaSyDIff7MFtABpls-G3vQxG10RMHCRck0JOY';

// The Client ID obtained from the Google API Console. Replace with your own Client ID.
var clientId = "704229650-5o09hicote42v0nkr43u88uapdn4b0mm.apps.googleusercontent.com"

// Replace with your own project number from console.developers.google.com.
// See "Project number" under "IAM & Admin" > "Settings"
var appId = "704339650";

// Scope to use to access user's Drive items.
var scope = ['https://www.googleapis.com/auth/drive.file'];

var pickerApiLoaded = false;

// Use the Google API Loader script to load the google.picker script.

var pickedSheetID;

// Create and render a Picker object for searching images.
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

// A simple callback implementation.
function pickerCallback(data) {
  if (data.action == google.picker.Action.PICKED) {
	console.log(data.docs[0]);
	pickedSheetID = data.docs[0].id;
	document.getElementById("sheetName").innerHTML = data.docs[0].name;
  }
}