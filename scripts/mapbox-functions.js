function myMap(){
    var mapProp = {
    center:new google.maps.LatLng(latitude, longitude),
    
    zoom:5,
};
    var map = new google.maps.Map(document.getElementById('map'),mapProp);
}

var latitude, longitude;

function fetchPoints() {
    for (var i = 0; i < 9; i++){
        latitude = gimme latitude;
        longitude = gimme longitude;
    }

}
