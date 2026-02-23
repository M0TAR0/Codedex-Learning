const pig = {
    name: "Oinky",
    type: "pig",
    age: 7,
    makeSound: function () {
        return pig.name + " is a " + pig.age + " year old " + pig.type + " that goes Oink Oink!";
    }
}

const sheep = {
    name: "Seepy",
    type: "sheep",
    age: 9,
    makeSound: function () {
        return sheep.name + " is a " + sheep.age + " year old " + sheep.type + " that goes beeeeeeeeeeeeeeeeeeeeeeeeeeeeh!";
    }
}

const dog = {
    name: "Firulais",
    type: "dog",
    age: 6,
    makeSound: function () {
        return dog.name + " is a " + dog.age + " year old " + dog.type + " that goes woof!";
    }
}

console.log(pig.makeSound());
console.log(sheep.makeSound());
console.log(dog.makeSound());