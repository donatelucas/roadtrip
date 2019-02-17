console.log("SEE YOU SPACE COWBOY...");

var input;
var playlist;
var ar = [];
var arP = [];

function fetchInput() {
    input = document.getElementById('landmarks').value;
    makeList();
}

function fetchPlayList() {
    playlist = document.getElementById('playlist').value;
    makePlaylist();
}

function makePlaylist(){
    arP = playlist.split(",");
    return arP;
}

function readInput() {
    return input;
}

function makeList(){
    ar = input.split(","); // The split(string) method returns an array
    return ar;
}

function readLists(){
    for (var i = 0; i < ar.length; i++){
        console.log(ar[i])
        console.log(arP[i]);
    }
}
