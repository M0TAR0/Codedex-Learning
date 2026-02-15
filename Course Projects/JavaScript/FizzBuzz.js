let limitNumber = 15;

for (let currentNumber = 1; currentNumber <= limitNumber; currentNumber++) {
    if ( (currentNumber%3 == 0) && (currentNumber%5 == 0) ){
        console.log("FizzBuzz");
        continue;
    } else if (currentNumber%3 == 0) {
        console.log("Fizz");
        continue;
    } else if (currentNumber%5 == 0) {
        console.log("Buzz");
        continue;
    }

    console.log(currentNumber);
}