let map;

function initMap() {
    var mapDiv = document.getElementById('mapPanel');
    map = new google.maps.Map(mapDiv, {
        center: new google.maps.LatLng(37.7485824,-122.4184108000),
        zoom: 12,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });
    google.maps.event.addListenerOnce(map, 'tilesloaded', addMarkers);
}

function addMarkers() {
    "{% for account in accounts %}"
    var point = new google.maps.LatLng("{{account.latitude}}","{{account.longitude}}");
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

    "{% endfor %}"

  }


//   google.maps.event.addDomListener(window, 'load', initMap);