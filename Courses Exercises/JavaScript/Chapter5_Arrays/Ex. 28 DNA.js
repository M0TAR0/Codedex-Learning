// Write code below 💖

let myDNA = [];
const dnaPieces = ["A", "C", "G", "T"];

for(let i = 0; i < 24; i++){
randIndex1 = Math.floor(Math.random()*4);
randIndex2 = Math.floor(Math.random()*4);
randIndex3 = Math.floor(Math.random()*4);

let dnaSequence = "" + dnaPieces[randIndex1] + dnaPieces[randIndex2] + dnaPieces[randIndex3];

myDNA.push(dnaSequence);
}

console.log(myDNA);