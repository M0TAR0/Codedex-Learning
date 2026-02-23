const departTripTicket = {
    name: "Romel",
    from: "Mexico",
    to: "Washington",
    businessClass: false,
    leaveTime: 14,
    arriveTime: 17,
    flightTime: function() {
        console.log(this.arriveTime-this.leaveTime);
    },

    upgrade: function () {
        if (departTripTicket.businessClass == false){
            departTripTicket.businessClass = true
        } else {
            console.log("Your ticket is already business class!")
        }
    }
}


const returnTripTicket = {
    name: "Romel",
    from: "Washington",
    to: "Mexico",
    businessClass: false,
    leaveTime: 6,
    arriveTime: 13,
    flightTime: function() {
        console.log(this.arriveTime-this.leaveTime);
    },

    upgrade: function () {
        if (departTripTicket.businessClass == false){
            departTripTicket.businessClass = true
        } else {
            console.log("Your ticket is already business class!")
        }
    }
}

returnTripTicket.upgrade();
console.log(departTripTicket);
console.log(returnTripTicket);