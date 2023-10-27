// 1) Last loop value
    // 1




// 2) Which values does the while loop show?
	// 1. 1, 2, 3, 4
	// 2. 1, 2, 3, 4, 5




// 3) Which values get shown by the "for" loop?
	// 1. 0,1,2,3,4
	// 2. 0,1,2,3,4




// 4) Output even numbers in the loop
	// for (let +i = 2; i < 11; +i + 2) alert(i); (ignore)

	// for (let i = 2; i < 11; i++) {
	// 	if (i % 2 === 0){
	// 		alert(i);
	// 	}
	// }




// 5) Replace "for" with "while"
	// let i = 0
	// while (i < 3) {
	// 	alert(`number ${i}!`);
	// 	i++
	// }



// 6) Repeat until the input is correct
	// for (;;) {
	// 	let userNumber = +promt("Type a number ");
	// 	if (userNumber == 'null' || userNumber === '') break;

	// 	if (userNumber > 100){
	// 		alert(`The number ${userNumber} is higher than 100`);
	// 		break;
	// 	}
	// }



// 7) Output prime numbers
	// (MY ATTEMPT)
	// num = +prompt();
	// for(i = 2; i <= num; i++) for(j = 2; j < i; j++) if (n % j !== 0) console.log(n); 

	// Right answer
		// let n = 10;
		// nextPrime:
		// for (let i = 2; i <= n; i++) { // for each i...		
		//   for (let j = 2; j < i; j++) { // look for a divisor..
		// 	if (i % j == 0) continue nextPrime; // not a prime, go next i
		//   }		
		//   alert( i ); // a prime
		// }