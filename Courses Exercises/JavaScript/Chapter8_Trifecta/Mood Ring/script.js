stoneSelector = document.getElementById("stone");

randomNumber = Math.floor(Math.random()*9)+1;

if (randomNumber == 1){
    stoneSelector = "red";
} else if (randomNumber == 2) {
    stoneSelector.style.backgroundColor = "orange";
} else if (randomNumber == 3) {
    stoneSelector.style.backgroundColor = "yellow";
} else if (randomNumber == 4) {
    stoneSelector.style.backgroundColor = "green";
} else if (randomNumber == 5) {
    stoneSelector.style.backgroundColor = "blue";
} else if (randomNumber == 6) {
    stoneSelector.style.backgroundColor = "#4168e1";
} else if (randomNumber == 7) {
    stoneSelector.style.backgroundColor = "#00008b";
} else if (randomNumber == 8) {
    stoneSelector.style.backgroundColor = "purple";
} else if (randomNumber == 9) {
    stoneSelector.style.backgroundColor = "black";
}