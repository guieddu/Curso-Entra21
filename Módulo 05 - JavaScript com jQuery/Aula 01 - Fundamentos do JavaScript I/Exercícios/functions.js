// 1) Is "Else" required?
// There's no difference. Them two do the same thing, the first use the if esle structure and the second one ommit the else.




// 2) Rewrite the function using '?' or '||'
// a. With '?'
// function checkAge(age) {
//     return (age > 18) ? true : confirm('Did parents allow you?');
// }
// 
// b. With '||'
// function checkAge(age) {
//     return (age > 18) || confirm('Did parents allow you?');
// }




// 3) Function min(a, b)
// function min(a, b) {
//     return (a < b) ? a : b;
// }




// 4) Funtion pow(x, n)
// function por(x, n) {
//     let result = x;
//     for (let i = 0; i <= n;) {
//         i++;
//         result *= x;
//     }
//     return result;
// }
// 
// let x = prompt("x?", 1);
// let n = prompt("n?", 1);
// 
// (n <= 0) ? alert(`Power ${n} is not supported, use a positive integer`) : alert(pow(x, n));