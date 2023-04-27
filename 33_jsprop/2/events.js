// demo 2
// JS event propagation

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];

//creates alerts/pop ups
var clicky = function(e) {
  alert( this.innerHTML );
};

//sets up alert for when tr is clicked
for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

//sets up alert for when td is clicked
for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky);
}

//sets up alert for when table is clicked
table.addEventListener('click', clicky);


// Q: When user clicks on a cell, in what order will the pop-ups appear?
// Order is order of code in .js file -> (td -> tr -> table)