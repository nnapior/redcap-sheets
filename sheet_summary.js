var data
var sheetID
const sheets = google.sheets({version: 'v4', auth});

//check column names to match red cap columns 
function checkColumnNames(){
    //check redcaps columns 
    
    //cehck sheets columns
    const = request{
        spreadsheetId:'',
        range:'',
    };
    try {
        const response = (await sheets.spreadsheets.values.get(request)).data;
        console.log(JSON.stringify(response, null, 2));
      } catch (err) {
        console.error(err);
      }
    sheets.spreadsheets.values.get(request)
}

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
    //show number of empty data points
    if(rows.length){
        rows.map((row) => {
            empty_data_points = 0; 
            //if row/cell isn't empty add to datapoint counter
            if(){

                empty_data_points+=1;
            }
            console.log(empty_data_points, 'Data points are empty');
        }
    } 
    //show number of complete entries 

    //show number of incomplete entries 
    
   
}





