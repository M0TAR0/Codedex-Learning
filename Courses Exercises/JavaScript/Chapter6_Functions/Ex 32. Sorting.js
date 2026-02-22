function mean(viewsArray){
    let totalViews = 0;
    let mean = 0;

    for(let i = 0; i < viewsArray.length; i++){
        totalViews += viewsArray[i];
    }

    average = totalViews / viewsArray.length;

    return average;
}

function median(viewsArray){
    let sortedStats;
    let middleIndex;

    sortedStats = viewsArray.sort(function(a,b){return a-b});
    middleIndex = Math.floor((viewsArray.length/2));

    return sortedStats[middleIndex];
}

//Views Array
const recentTikTokViews = [1932, 2300, 453, 5222, 6733, 7402, 8334];
const recentInstagramViews = [936, 2576, 453, 7013, 5489, 7402, 3921];
const recentYouTubeViews = [2300, 453, 5222, 989, 6733, 7402, 2789];

console.log("TikTok");
console.log("Mean: ", mean(recentTikTokViews));
console.log("Median: ", median(recentTikTokViews));
console.log("\n");

console.log("Instagramm");
console.log("Mean: ", mean(recentInstagramViews));
console.log("Median: ", median(recentInstagramViews));
console.log("\n");

console.log("Youtube");
console.log("Mean: ", mean(recentYouTubeViews));
console.log("Median: ", median(recentYouTubeViews));
console.log("\n");