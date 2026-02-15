// Write code below 💖

let myNumber = 100;
let binary = "";
let nextNumber = "";

while (myNumber !== 0){
    if(myNumber % 2 == 0){
        nextNumber = "0";
    }
    else if (myNumber%2 == 1 ) {
        nextNumber = "1";
    }

    binary = nextNumber + binary;

    myNumber = Math.floor(myNumber/2);
}

if (binary == ""){
  binary = "0";
}

console.log(binary);