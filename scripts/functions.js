console.log("See ya Space Cowboy");

var input;
var ar = [];

function fetchInput() {
    input = document.getElementById('landmarks').value;
    makeList();
}

function readInput() {
    return input;
}

function makeList(){
    ar = input.split(","); // The split(string) method returns an array
    return ar;
}

function readList(){
    for (var i = 0; i < ar.length; i++){
        console.log(ar[i]);
    }
}
