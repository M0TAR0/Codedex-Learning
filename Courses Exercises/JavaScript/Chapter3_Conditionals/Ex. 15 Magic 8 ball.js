//Program for a Magic 8 Ball

question = "Is Codédex a great learning resource?";
randomAnswer = Math.floor(Math.random() * 10);

//8 Ball Questions
console.log(question);
console.log(randomAnswer);

if (randomAnswer == 1) {
    console.log("Yes - definitely");
} else if (randomAnswer == 2) {
    console.log("It is decidedly so.");
} else if (randomAnswer == 3) {
    console.log("Without a doubt.");
} else if (randomAnswer == 4) {
    console.log("Reply hazy, try again");
} else if (randomAnswer == 5) {
    console.log("Ask again later");
} else if (randomAnswer == 6) {
    console.log("Better not tell you now");
} else if (randomAnswer == 7) {
    console.log("My sources say no.");
} else if (randomAnswer == 8) {
    console.log("Outlook not so good.");
} else if (randomAnswer == 9) {
    console.log("Very doubtful.");
}