// Team Wandering Majestic Merciful Mice:: Maya Mori, Wilson Mach
// SoftDev pd2
// K27 -- Basic functions in JavaScript
// 2023-04-04
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn

// (define (fact n) 
//   (if (= n 0) 
//       1 
//       (* n (fact (- n 1)))
//   )
// )

function fact(n){
    if(n == 0){
        return 1;
    } 

    return n * fact(n-1);
}

function fib(n) {
    if(n == 0){
        return 0;
    }

    if (n == 1){
        return 1;
    }

    return fib(n-1) + fib(n-2);    
}

// let x = fib(3);
// console.log(x);

//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
