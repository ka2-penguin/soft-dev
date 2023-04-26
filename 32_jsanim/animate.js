// Team Wandering Majestic Merciful Mice:: Maya M., Wilson
// SoftDev pd2
// K32 -- DVD JS animation
// 2023-04-26m

var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");
var dvdButton = document.getElementById("dvd");

var ctx = c.getContext("2d");

ctx.fillStyle = "cyan";

var requestID;

var radius = 10;
var growing = true;


var drawDot = (e) => {
    clear(e);
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

var dvdLogoSetup = function() {
    cancelAnimationFrame(requestID);

    var rectWidth = 60;
    var rectHeight = 40;

    var rectX = Math.random() * (500-rectWidth);
    var rectY = Math.random() * (500-rectHeight);

    console.log(rectX,rectY)

    var xVel = 1;
    var yVel = 1;

    var logo = new Image();
    logo.src = "logo_dvd.jpg";
    var dvdLogo = function() {
        clear();
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
        if (rectX <= 0 || rectX >= 500-rectWidth) {
            xVel *= -1;
        }
        rectX += xVel;

        if (rectY <= 0 || rectY >= 500-rectHeight) {
            yVel *= -1;
        }
        rectY += yVel;
        // console.log(rectX)
        

        cancelAnimationFrame(requestID);
        requestID = requestAnimationFrame(dvdLogo);
    }
    dvdLogo();
}

var stopIt = () => {
    cancelAnimationFrame(requestID);
}


var clear = () => {
    // e.preventDefault();
    ctx.clearRect(0, 0, c.width, c.height);
}

dotButton.addEventListener('click', drawDot);
stopButton.addEventListener('click', stopIt);
dvdButton.addEventListener('click',dvdLogoSetup)
