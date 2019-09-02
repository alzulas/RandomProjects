//I wrote this function in google sheets scripter
//I had a google sheet that showed all the wineries in a certain location
//It also had a list of all possible types of wine and check marks in the boxes to show what wines each winery had
//I had color coded the columns to show red and white, but I wanted to know, over all, how many of each type of wine did each winery have
//I probably cound have easily done this calculation by hand, but it was more interesting to learn how google sheets uses scripts


function wineCounter() {
  //activate sheet, must have wine sheet open for this.
  var sheet = SpreadsheetApp.getActiveSheet();
  var numberOfWhite = 0;
  var numberOfRed = 0;
  var whiteRows = [0, 6, 7, 9, 10, 11, 13, 16, 19, 22, 27, 28, 31, 32, 33, 39, 40]; //these columns hold white wines
  var redRows =  [1, 2, 3, 4, 5, 8, 12, 14, 15, 17, 18, 20, 21, 23, 24, 25, 26, 30, 34, 35, 36, 37, 38, 41] //these columns hold red wines
  //pink column 29
  
  var startRow = 2;  // First row of data to process
  var numRows = 73;   // Number of rows to process
  
  // Fetch the range of cells 
  var dataRange = sheet.getRange(startRow, 12, numRows, 55);
  
  // Fetch values for each row in the Range.
  var data = dataRange.getValues();
  
  for (var i = 0; i < data.length; i++) {
    var row = data[i]; //grab single row
    //console.log(row);
    for (var j = 0; j < row.length; j++) {
      check = row[j]; //single element
      if (check === "✔️"){ //does this box have a check mark in it?
        //if in white wine column, ++ white wines, else if in red wine column, ++ red wines
        if (whiteRows.indexOf(j) != -1){
          numberOfWhite++; 
        }
        else if (redRows.indexOf(j) != -1){
          numberOfRed++;
        };
      };
    };
   //Once it goes through every element in a row, add the number of white wines and the number of red wines to two new columns
   var whiteWineLocation = 'J'+(i+2);
   var redWineLocation = 'K'+(i+2);
   SpreadsheetApp.getActiveSheet().getRange(whiteWineLocation).setValue(numberOfWhite);
   SpreadsheetApp.getActiveSheet().getRange(redWineLocation).setValue(numberOfRed);
   //reset counters
   numberOfWhite = 0;
   numberOfRed = 0;
   };
};
