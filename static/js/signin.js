function signInGoogle2() {
	var req = new XMLHttpRequest();
	req.open("POST","/auth", true);
	req.onreadystatechange = function() {
		console.log(this.response);
		window.location.href = this.response;
		if(this.readyState == 4 && this.status == 200) {
			// window.localStorage.setItem("googleCreds",this.response);
			// alert("successfully signed in");
			// getUserInfo();
		}
	}
	req.send();
}

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
			window.localStorage.setItem("googleCredKey", res["key"]);
			window.localStorage.setItem("googleCredData", res["data"]);
			window.localStorage.setItem("pickerCredToken", btoa(res["token"]));
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
	var obj = {
		"creds":window.localStorage.getItem("googleCredData"),
		 "key":window.localStorage.getItem("googleCredKey")
	 };
	var reqData = JSON.stringify(obj);
	reqData = reqData.replace("\n","");
	reqData = reqData.replace("'", "\'");

	var req = new XMLHttpRequest();
	req.open("POST","/signOutGoogle", true);
	req.setRequestHeader("Content-Type","application/json");
	req.onreadystatechange = function() {
		if(this.readyState == 4 && this.status == 200) {
			window.localStorage.removeItem("googleCredKey");
			window.localStorage.removeItem("googleCredData");
			window.localStorage.removeItem("pickerCredToken");
			alert("successfully signed out");
			getUserInfo();
		}
	}
	console.log(reqData);

	req.send(reqData);
}
