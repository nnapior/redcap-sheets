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
			console.log(this.response);
		}
	}
	req.send();
}