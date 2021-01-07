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

fetch(`get_locations`)
    .then(response => response.json())
    .then(data => locations = data)
    .then(() => locations.forEach(addMarkers))
    .then(() => locations.forEach(get_plants_by_user))

async function get_plants_by_user(locations) {
    let response = await fetch(`get_plants_by_user/${locations.id}`)
    let text = await response.json()
    console.log(text)
}

function addMarkers(locations) {
    console.log(locations)

    // fetch(`get_plants_by_user/${locations.id}`)
    //     .then(response => response.json())
    //     .then(data => console.log(data))

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
        content: "<a href='http://127.0.0.1:8000/other_user/${locations.id}'>" + locations.first_name + "</a>" 
        + "<br>" + locations.email + "<br>" + "Available plants:"
    });
    google.maps.event.addListener(marker, 'click', function() {
        window.location.href = this.url;
        this['infowindow'].open(map, this);
    });
    google.maps.event.addListener(marker, 'mouseover', function() {
        // this['infowindow'].open(map, this);
    });
    google.maps.event.addListener(marker, 'mouseout', function() {
        // this['infowindow'].close(map, this);
    });
  }
