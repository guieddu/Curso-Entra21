// 1) What's the resulf of OR?
    // 2   




// 2) What's the result of OR'ed alerts?
    // 1 then 2






// 3) What is the result of AND?
    // null




// 4) What is the result of AND'ed alerts?
    // 1 then undefine d



// 5) The result of OR AND OR
    // 3   



// 6) Check the range between
    // if (90 >= userAge && userAge >= 14);


// 7) Check the range outside
    /* 
    My tries:
    if (userAge > 90 || userAge < 14) {

    }
    let outside = !(userAge < 90) 
    outside = (userAge < 14)
    if (outside) {}

    // or

    let outside = !(userAge < 90) ? true : (userAge < 14) ? true : false; 
    */
    // correct answer:
    // if (!(age >= 14 && age <= 90))
    // if (age < 14 || age > 90)





// 8) A question about "if"
    // 1. true cause (-1) is true
    // 2. false cause the comparison is false
    // 3. true cause (1) is true



// 9) Check the login
    // let login = prompt("Type your login ");
    // let password;

    // if (login === 'Admin') {
    //     password = prompt("Type the password ");
    //     if (password === "TheMaster") {
    //         alert("Welcome!");
    //     } else if (password === '' || password === null){
    //         alert("Canceled");
    //     } else if (password !== "TheMaster") {
    //         alert("Wrong password");        
    //     } 
    // } else if (login === '' || login === null){
    //     alert("Canceled");    
    // } else if (login !== 'Admin') {
    //     alert("I don't know you");
    // }