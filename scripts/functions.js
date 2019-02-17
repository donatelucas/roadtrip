console.log("SEE YOU SPACE COWBOY...");

var input;
var playlist_input;
var landmarks = [];
var playlist = [];

function fetchInput() {
    input = document.getElementById('landmarks').value;
    makeList();
}

function fetchPlayList() {
    playlist_input = document.getElementById('playlist').value;
    makePlaylist();
    setSong();
}

function makePlaylist(){
    playlist = playlist_input.split(",");
    return playlist;
}

function readInput() {
    return input;
}

function makeList(string){
    landmarks = input.split(","); // The split(string) method returns an array
    return landmarks;
}

function readLists(){
    for (var i = 0; i < landmarks.length; i++){
        console.log(landmarks[i]);
    }
}

function getLandmarks(){
    return landmarks;
}

function readPlayList(){
    for (var i = 0; i < playlist.length; i++){
        console.log(playlist[i]);
    }
}

function setSong(){
    document.getElementById('now_playing').innerHTML = "Now playing: " + playlist[0];
}

$(()=>{
    function serverRequest(url,method,obj,callback){
        if(method == 'GET'){
            $.get(url,(data)=>{
                callback(data);
            });
        }else{
            $.post(url,obj,(data)=>{
                callback(data);
            });
        }
    }

});
