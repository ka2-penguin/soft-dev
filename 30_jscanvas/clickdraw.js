// Team Wandering Majestic Merciful Mice:: Maya M., Wilson
// SoftDev pd2
// K30 -- canvas based JS drawing
// 2023-04-24m
// HTML file for JavaScript canvas work

// retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init global state var
var mode = "Rectangle";

//var toggleMode = function(e)
var toggleMode = (e) => {
    console.log("toggling...");
    if(mode === "Rectangle"){
        mode = "circle";
    } else{
        mode = "Rectangle";
    }

    var buttonToggle = document.getElementById("buttonToggle");
    buttonToggle.innerHTML = mode;
}

//var drawRect = function(e) 
var drawRect = (e) => {
    // don't use clientX or clientY -> does not adjust coordinates based on device
    var mouseX = e.offsetX; 
    var mouseY = e.offsetY;
    // console.log("mouseclick at ", mouseX, mouseY);

    ctx.fillStyle = "#FF0000";
    ctx.fillRect(mouseX, mouseY, 100, 200);
}

//var drawCircle = function(e) 
var drawCircle = (e) => {
    // don't use clientX or clientY -> does not adjust coordinates based on device
    var mouseX = e.offsetX; 
    var mouseY = e.offsetY;
    // console.log("mouseclick at ", mouseX, mouseY);

    ctx.fillStyle = "#FF0000";
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 75, 0, 2*Math.PI);
    ctx.fill();
}

//var draw = function(e) 
var draw = (e) => {
    if(mode === "Rectangle"){
        drawRect(e);
    } else{
        drawCircle(e);
    }
}


//var wipeCanvas = function()
var wipeCanvas = () => {
    ctx.clearRect(0, 0, c.width, c.height);
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener('click', toggleMode);

var clearB = document.getElementById("buttonClear");
clearB.addEventListener('click', wipeCanvas);