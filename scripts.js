var data;
var sheetID;

function getValues(object, level = 0) {
  if (typeof object == "string") {
    return object;
  }

  if (level >= 10) {
    return null;
  }
  var keys = Object.keys(object);

  var outputStr = "<br><div class='test'></div>";
  for (key of keys) {
    if (key != "0") {
      for (var i = 0; i < level; i++) {
        outputStr += "--";
      }
      outputStr += key + ": " + getValues(object[key], level + 1) + "<br>";
    }
  }

  return outputStr;
}

function showParticipant(eventKey, participantID) {
  console.log(eventKey, participantID);
  var object = data[eventKey][participantID];
  var output = document.getElementById("output")
  output.innerHTML = ""
  var keys = Object.keys(object);
  for (key of keys) {
    tr = document.createElement('tr')
    
    heading = document.createElement("td")
    heading.innerHTML = key
    tr.append(heading)
    
    
    value = document.createElement("td")
    value.innerHTML = object[key]
    tr.append(value)

    output.append(tr)
  }

}

function exportData() {
  //this function gets the json data ready to push to sheets
  var exportMode = document.getElementById("exportMode").value;

  if (exportMode == "select") {
    //export only selected events"
    console.log("exporting selected events");
    var newObject = {};
    var checkboxes = document.getElementsByClassName("eventSelectionCheckbox");
    for (checkbox of checkboxes) {
      if (checkbox.checked) {
        newObject[checkbox.value] = data[checkbox.value];
      }
    }
    console.log(Object.keys(newObject));
    pushToSheets(newObject);
  } else {
    //export all events in data
    console.log("exporting all events");
    pushToSheets(data);
  }
}

function pushToSheets(object) {
  //put code to write to a sheet here
  //the "object" parameter is the json data we're writing

  console.log(object);

  //if we're doing sheet destination control, use this outline
  var sheetDestination = document.getElementById("sheetMode").value;
  if (sheetDestination == "new") {
    //put code to create/write to a new sheet here
    console.log("writing to new sheet");
    var pushObject = { mode: "new", object: object };

    var r = new XMLHttpRequest();
    r.open("POST", "/pushData", true);
    r.setRequestHeader("Content-Type", "application/json");
    r.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        console.log(this.response);
      }
    };

    var data = JSON.stringify(pushObject);
    data = data.replace("\n", "");
    data = data.replace("'", '"');
    console.log(data);

    r.send(data);
  } else {
    if (sheetID != null) {
      switch (sheetDestination) {
        case "replace":
          //put code to replace an existing sheet's data here
          console.log(
            "writing to an existing sheet (replacing) with id " + sheetID
          );

          var pushObject = { mode: "replace", object: object };

          var r = new XMLHttpRequest();
          r.open("POST", "/pushData", true);
          r.setRequestHeader("Content-Type", "application/json");
          r.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
              console.log(this.response);
            }
          };

          var data = JSON.stringify(pushObject);
          data = data.replace("\n", "");
          data = data.replace("'", '"');
          console.log(data);

          r.send(data);

          break;
        default:
          alert(
            "there was an error exporting to an existing sheet: unknown export mode"
          );
          break;
      }
    } else {
      alert(
        "there was an error exporting to an existing sheet: sheet not selected"
      );
    }
  }
}

function showEventCheckboxes(value) {
  var eventCheckboxes = document.getElementById("selectedEvents");
  if (value == "select") {
    eventCheckboxes.style.visibility = "visible";
    eventCheckboxes.style.position = "relative";
    eventCheckboxes.style.zIndex = 1;
  } else {
    eventCheckboxes.style.visibility = "hidden";
    eventCheckboxes.style.position = "absolute";
    eventCheckboxes.style.zIndex = -10;
  }
}

function showEvent(eventKey) {
  var object = data[eventKey];
  var keys = Object.keys(object);
  var selection = document.getElementById("participantSelection");
  selection.innerHTML = "";
  selection.oninput = function () {
    showParticipant(eventKey, this.value);
  };
  for (key of keys) {
    var option = document.createElement("option");
    option.value = key;
    option.innerHTML = key;
    selection.appendChild(option);
  }
  selection.value = keys[0];
  showParticipant(eventKey, keys[0]);
}

function setButtons(object) {
  var keys = Object.keys(object);
  var buttons = document.getElementById("eventSelection");
  buttons.innerHTML = "";
  buttons.oninput = function () {
    showEvent(this.value);
  };

  var eventCheckboxes = document.getElementById("selectedEvents");

  for (key of keys) {
    var option = document.createElement("option");
    option.value = key;
    option.innerHTML = key;
    buttons.appendChild(option);

    var checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.className = "eventSelectionCheckbox";
    checkbox.value = key;
    checkbox.checked = true;
    var label = document.createElement("label");
    label.htmlFor = key;
    label.innerHTML = key;
    eventCheckboxes.appendChild(checkbox);
    eventCheckboxes.appendChild(label);
    eventCheckboxes.appendChild(document.createElement("br"));
  }
  buttons.value = keys[0];
  showEvent(keys[0]);
}

function chooseSheet() {
  //TODO: put code to choose a sheet here and set the global "sheetID" variable to the id or however sheets are identified
  console.log("choosing sheet");

  //placeholder id
  sheetID = "1";

  document.getElementById("sheetName").innerHTML = sheetID;
}

function showSheetSelection(value) {
  let sheetSelection = document.getElementById("sheetSelection");
  if (value == "new") {
    sheetSelection.style.visibility = "hidden";
    sheetSelection.style.position = "absolute";
    sheetSelection.style.zIndex = -10;
  } else {
    sheetSelection.style.visibility = "visible";
    sheetSelection.style.position = "relative";
    sheetSelection.style.zIndex = 1;
  }
}

function getData() {
  document.getElementById("mainButton").innerHTML = "Working...";
  var r = new XMLHttpRequest();
  r.open("GET", "/pullData", true);
  r.onreadystatechange = function () {
    if (this.status == 200 && this.readyState == 4) {
      var parsedRes = JSON.parse(r.response);
      data = parsedRes;
      setButtons(data);
      document.getElementById("mainButton").innerHTML = "Refresh Data";
    }
  };
  r.send();
}

function showImportEventCheckboxes(value) {
  checkboxDiv = document.getElementById("checkboxes");
  if (value == "select") {
    checkboxDiv.style.visibility = "visible";
    checkboxDiv.style.display = "block";
  } else {
    checkboxDiv.style.visibility = "hidden";
    checkboxDiv.style.display = "none";
  }

  document.getElementById("message").style.visibility = "hidden";
}
