// Team JM:: Maya M, Joseph
// SoftDev pd2
// K29 -- add buttons and bind them to functions
// 2023-04-20w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

// can access these variables in the dev console
var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
//use "f" to call the function
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',			//o["name"] or o['name']
          age : 1024,
          items : [10, 20, 30, 40],		//[index] to access elements
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {			// use o.func(x) to call this
            return x+30;
          }
        };

// adds an item at the end of the list, disappears when you reload HTML
var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

// collects all li elements regardless of which list it's in
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};

// only colors the 1st and last item in the list red
// if the li element doesn't belong to any class, it turns red
// doesn't add red to elements that already has red
var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


// doesn't add any colors to elements that already has that color
var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

const fact = (n) => {
  if(n == 0){
      return 1;
  } 
  return n * fact(n-1);
}
const fib = (n) => {
  if (n < 2) return n;
  return fib(n-1) + fib(n-2);    
}

const gcd = (a,b) => {
  if (a == 0) {
    return b;
    return a;
  } else if (b == 0) {
  } else {
    return gcd(Math.min(a,b), Math.max(a,b) % Math.min(a,b));
  }
}

document.write("5! = "+fact(5));

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};

var fibButton = document.getElementById('fib')
var facButton = document.getElementById('fac')
var gcdButton = document.getElementById('gcd')

fibButton.addEventListener('click', ()=> {
  var thing = document.getElementById("calculatorNans");
  var a = 10
  thing.innerHTML = "the " + a + "th term of the fibonacci sequence is " + fib(a)
})
facButton.addEventListener('click', function() {
  var thing = document.getElementById("calculatorNans");
  var a = 10
  thing.innerHTML = "factorial of " + a + " is " + fact(a)
})
gcdButton.addEventListener('click', function() {
  var thing = document.getElementById("calculatorNans");
  var a = 20
  var b = 37
  thing.innerHTML = "gcd of " + a + " and " + b + " is " + gcd(a,b)
})


