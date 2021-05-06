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

function signInGoogle() {
	var req = new XMLHttpRequest();
	req.open("POST","/authGoogle", true);
	req.onreadystatechange = function() {
		if(this.readyState == 4 && this.status == 200) {
			var res = JSON.parse(this.response);
			window.localStorage.setItem("googleCredKey", res["key"]);
			window.localStorage.setItem("googleCredData", res["data"]);
			alert("successfully signed in");
			getUserInfo();
		}
	}
	req.send();
}

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
			//alert("successfully signed out");
			getUserInfo();
		}
	}
	console.log(reqData);

	req.send(reqData);
}
