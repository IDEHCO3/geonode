var projection_base = 'EPSG:3857';
var rio_center = new ol.proj.transform([-42.5,-22.3], 'EPSG:4326', projection_base);
var rio_zoom = 8;

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
    var app = angular.module("map_detail",[]);

    app.controller('MapController', ['$rootScope', function($rootScope){
        var scope = $rootScope;

        scope.loadMapData = function(center_logitude, center_latitude, zoom){
            var center = new ol.proj.transform([center_logitude, center_latitude], 'EPSG:4326', projection_base);
            map.getView().setCenter(center);
            map.getView().setZoom(zoom);
        };
    }]);
})();
