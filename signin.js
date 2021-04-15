function signInREDCap() {
	var req = new XMLHttpRequest();
	req.open("POST","/authREDCap", true);
	req.onreadystatechange = function() {
		if(this.readyState == 4 && this.status == 200) {
			console.log(this.response);
		}
	}
	req.send();
}

function signInGoogle() {
	var req = new XMLHttpRequest();
	req.open("POST","/authGoogle", true);
	req.onreadystatechange = function() {
		if(this.readyState == 4 && this.status == 200) {
			window.localStorage.setItem("googleCreds",this.response);
			alert("successfully signed in");
		}
	}
	req.send();
}

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
			alert("successfully signed out");
		}
	}
	req.send(reqData);
}