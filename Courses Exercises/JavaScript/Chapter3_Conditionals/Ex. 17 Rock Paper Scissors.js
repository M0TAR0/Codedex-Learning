//Program for a rock paper scissors

player_election = 1;
computer_election = Math.floor(Math.random() * 3);

if (player_election==0 && computer_election==1) {
    console.log("Player picked:     Rock");
    console.log("Computer picked:   Paper");

    console.log("\nComputer won!");
} else if (player_election==0 && computer_election==2){
    console.log("Player picked:     Rock");
    console.log("Computer picked:   Scissors");

    console.log("\nThe Player won!");
} else if (player_election==1 && computer_election==0){
    console.log("Player picked:     Paper");
    console.log("Computer picked:   Rock");

    console.log("\nThe Player won!");
} else if (player_election==1 && computer_election==2){
    console.log("Player picked:     Paper");
    console.log("Computer picked:   Scissors");

    console.log("\nComputer won!");
} else if (player_election==2 && computer_election==0){
    console.log("Player picked:     Scissors");
    console.log("Computer picked:   Rock");

    console.log("\nComputer won!");
} else if (player_election==2 && computer_election==1){
    console.log("Player picked:     Scissors");
    console.log("Computer picked:   Paper");

    console.log("\nThe Player won!");
} else {
    console.log("Bothe players chose the same!")
    console.log("\nIt's a tie!")
}