/*
	signInGoogle()
		Signs in to a user's Google account and stores the credentials in the browser's local storage.
		
		Parameters:
			None
		Returns:
			None
*/
function signInGoogle() {
	var req = new XMLHttpRequest();
	req.open("POST","/authGoogle", true);
	req.onreadystatechange = function() {
		if(this.readyState == 4 && this.status == 200) {
			var res = JSON.parse(this.response);
			
			window.localStorage.setItem("pickerCredToken", btoa(res["token"]));
			window.localStorage.setItem("googleCreds",res["creds"]);
			alert("successfully signed in");
			getUserInfo();
		}
	}
	req.send();
}

/*
	signOutGoogle()
		Signs out of a user's Google account, and removes the credentials from local storage.
		
		Parameters:
			None
		Returns:
			None
*/
function signOutGoogle() {
	var obj = {"creds":window.localStorage.getItem("googleCreds")};
	var reqData = JSON.stringify(obj);
	reqData = reqData.replace("\n","");
	reqData = reqData.replace("'", "\"");

	var req = new XMLHttpRequest();
	req.open("POST","/signOutGoogle", true);
	req.setRequestHeader("Content-Type","application/json");
	req.onreadystatechange = function() {
		if(this.readyState == 4 && this.status == 200) {
			window.localStorage.removeItem("googleCreds");
			window.localStorage.removeItem("pickerCredToken");
			alert("successfully signed out");
			getUserInfo();
		}
	}
	req.send(reqData);
}
