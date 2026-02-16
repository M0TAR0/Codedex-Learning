const musicPlaylist = [
  "Tom Sawyer",
  "Sabotage",
  "I Wanna Dance With Somebody",
  "Don't Speak",
  "Bulls On Parade",
  "Thriller",
  "The Breaks",
  "Brick",
  "Aeroplane Over the Sea",
  "Tubthumping"
];

oldFirstElement = musicPlaylist.shift();
oldLastElement = musicPlaylist.pop();

musicPlaylist.push("New Element");

musicPlaylist.unshift("First New Element");
musicPlaylist.unshift("Second New Element");

console.log(musicPlaylist);