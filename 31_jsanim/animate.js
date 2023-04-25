// Team Wandering Majestic Merciful Mice:: Maya M., Wilson
// SoftDev pd2
// K31 -- canvas based JS animation
// 2023-04-25m

var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "cyan";

var requestID;

var radius = 10;
var growing = true;


var drawDot = (e) => {
    clear();
    ctx.beginPath();
    ctx.arc(250, 250, radius, 0, 2*Math.PI);
    ctx.fill();

    if (growing) {
        radius += 1;
    } else {
        radius -= 1;
    }

    if (growing && radius > 250) {
        growing = false;
    } else if (!growing && radius == 0) {
        growing = true;
    }

    cancelAnimationFrame(requestID);
    requestID = requestAnimationFrame(drawDot);

}

var stopIt = () => {
    cancelAnimationFrame(requestID);
}


var clear = () => {
    ctx.clearRect(0, 0, c.width, c.height);
}

dotButton.addEventListener('click', drawDot);
stopButton.addEventListener('click', stopIt);