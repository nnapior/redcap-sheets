var data
var sheetID
const sheets = google.sheets({version: 'v4', auth});

//funtion to get # of worksheets
function getWorksheets(params) {
    sheets.spreadsheets.values.get({
        spreadsheetId: '',
        range: '',
      }
    
}

//function to show sheet summary 
function sheet_summary(params) {
    //choose sheet
    chooseSheet();
    //check if data is empty "Sheet is empty"
    const rows = res.data.values;
    if(rows.length){
        console.log('Sheet has values');
    }
    else{
        console.log('Sheet is empty, no data found') ;
    }
    //Show number of data points 
    if(rows.length){
        rows.map((row) => {
            data_points = 0; 
            //if row/cell isn't empty add to datapoint counter
            if(){
                
                data_points+=1;
            }
            console.log('Number of Data Points: ', data_points);
        }
    }
    //show number of etnries

    //show number of incomplete entries 
    
}





