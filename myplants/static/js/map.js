let map;

function initMap() {
    var mapDiv = document.getElementById('mapPanel');
    console.log(lat)
    console.log(lng)
    map = new google.maps.Map(mapDiv, {
        center: new google.maps.LatLng(lat,lng),
        zoom: 12,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });
}

fetch("get_locations")
    .then(response => response.json())
    .then(data => locations = data)
    .then(() => locations.forEach(addMarkers))

function addMarkers(locations) {
    console.log(locations)
    var point = new google.maps.LatLng(locations.latitude,locations.longitude);
    // var image = '{{ STATIC_PREFIX }}'+ 'checkmark.png';
    var marker = new google.maps.Marker({
        position: point,
        map: map,
        // icon: image, 
        // url: 'http://172.16.0.101:8882/zone/' + {{mark.id}},
        // title: '{{ mark.id }}',
    });
    marker['infowindow']  = new google.maps.InfoWindow({
            content: "<h1>'{{account.first_name}}'</h1> <br> '{{ account.city }}'",
    });
    google.maps.event.addListener(marker, 'click', function() {
        //window.location.href = this.url;
            this['infowindow'].open(map, this);
    });
    google.maps.event.addListener(marker, 'mouseover', function() {
        // this['infowindow'].open(map, this);
            });
    google.maps.event.addListener(marker, 'mouseout', function() {
        // this['infowindow'].close(map, this);

    });
  }
