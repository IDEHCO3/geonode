var zoom_id = 'id_zoom';
var center_id = ['id_center_longitude','id_center_latitude'];

var projection_base = 'EPSG:3857';
var rio_center = new ol.proj.transform([-42.5,-22.3], 'EPSG:4326', projection_base);
var rio_zoom = 8;
var source_base = new ol.layer.Tile({
    source: new ol.source.OSM()
});

var display = function(id, value) {
  document.getElementById(id).value = value;
};

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

var getLocation = function(evt){
    var map = evt.map;

    var center_3857 = map.getView().getCenter();
    var center = new ol.proj.transform(center_3857, projection_base, 'EPSG:4326');
    var zoom = map.getView().getZoom();

    display(zoom_id, zoom);
    display(center_id[0], center[0]);
    display(center_id[1], center[1]);
};

map.on('moveend',getLocation);

(function(){
    var app = angular.module('map_form',[]);

    app.controller('MapFormController', [ '$scope', function($scope){

        $scope.setZoomId = function(id){
            zoom_id = id;
        };

        $scope.setCenterLogId = function(id_log){
            center_id[0] = id_log;
        };

        $scope.setCenterLatId = function(id_lat){
            center_id[1] = id_lat;
        };
    }]);
})();