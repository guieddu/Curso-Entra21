// 1) Hello, Object
// const user = {};
// user['name'] = 'John';
// user['surname'] = 'Smith';
// user['name'] = 'Peter';
// delete user.name;




// 2) Check for emptiness
// My attempt:
// const schedule = {};
// const isEmpty = (element) => {
//     return(element === '' || element === null) ? true : false;
// }
// (function(x){
//     return isEmpty(x) ? alert(true) : alert(false);
// })(schedule);
// 
// The answer:
// function isEmpty(obj) {
//     for (let key in obj) {
//       // if the loop has started, there is a property
//       return false;
//     }
//     return true;
//   }




// 3) Sum object properties
// let salaries = {
//   John: 100,
//   Ann: 160,
//   Pete: 130
// };
// sum = 0;
// for (let num in salaries) {
//   sum += salaries[num];
// }
// console.log(sum);




// 4) Multiply numeric property values by 2
// function multiplyNumeric(obj) {
//   for (let keyValue in obj) {
//     (typeof obj[keyValue] === 'number') ? obj[keyValue] *= 2 : null;
//   }
// }