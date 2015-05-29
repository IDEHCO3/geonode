var projection_base = 'EPSG:3857';
var rio_center = new ol.proj.transform([-42.5,-22.3], 'EPSG:4326', projection_base);
var rio_zoom = 8;

var geojsonObject = {
  'type': 'FeatureCollection',
  'crs': {
    'type': 'name',
    'properties': {
      'name': 'EPSG:4326'
    }
  },
  'features': [
    {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [-43.0, -22.0]
      }
    }]
};

var source_base = new ol.layer.Tile({
    source: new ol.source.OSM()
});

var map = new ol.Map({
    target: 'map',
    renderer: 'canvas',
    layers: [
        source_base
    ],
    view: new ol.View({
        projection: projection_base,
        center: rio_center,
        zoom: rio_zoom
    })
});

(function(){
    var app = angular.module("map_detail",[]).config(function($httpProvider){
		$httpProvider.defaults.xsrfCookieName = 'csrftoken';
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	});

    app.controller('MapController', [ '$http', '$rootScope', function($http, $rootScope){
        var scope = $rootScope;

        scope.map_data = null;

        scope.loadMapDataUrl = function(url){

            $http.get(url).success(function(data){
                scope.map_data = data;
                var source = new ol.source.GeoJSON({'object': scope.map_data, projection: projection_base});
                var layer = new ol.layer.Vector({
                    source: source
                });
                map.addLayer(layer);

            }).error(function(){
                console.log("Can not load the GeoJson data!");
            });

        };

        scope.loadMapData = function(center, zoom, projection, geoJsonUrl){

            center = [parseFloat(center[0]), parseFloat(center[1])];
            zoom = parseInt(zoom);
            var center_p = new ol.proj.transform(center, projection, projection_base);
            map.getView().setCenter(center_p);
            map.getView().setZoom(zoom);

            scope.loadMapDataUrl(geoJsonUrl);

        };

    }]);
})();
