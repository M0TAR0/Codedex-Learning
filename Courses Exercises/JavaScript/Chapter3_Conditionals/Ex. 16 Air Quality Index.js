//Program to determien de quality of aire based on it's aqu

aqi = 120;

console.log("The Air Quality Index is:")

if (aqi >= 0 && aqi <= 50) {
    console.log("Good");
} else if (aqi >= 51 && aqi <= 100) {
    console.log("Moderate");
} else if (aqi >= 101 && aqi <= 150) {
    console.log("Unhealthy (Sensitive Groups)");
} else if (aqi >= 151 && aqi <= 200) {
    console.log("Unhealthy");
} else if (aqi >= 201 && aqi <= 300) {
    console.log("Moderate");
} else {
    console.log("Hazardous");
}










