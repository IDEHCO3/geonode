var source_base = new ol.source.TileWMS({
    url: 'http://127.0.0.1:8080/geoserver/geonode/wms',
    params: { LAYERS: 'geonode:33mee250gc_sir', VERSION: '1.1.1' }
});

var feature1 = new ol.Feature({
    name: 'nome',
    type: 'Point',
    geometry: new ol.geom.Point([-42.5,-22.3])
});

var features_stream = [];

features_stream.push(feature1);

var source_stream = new ol.source.Vector({
    features: features_stream
});

var map = new ol.Map({
    target: 'map',
    renderer: 'canvas',
    layers: [
        new ol.layer.Tile({
            title: "Rio de Janeiro",
            source: source_base
        }),

        new ol.layer.Vector({
            title: "Tweeter Stream",
            source: source_stream
        })
    ],
    view: new ol.View({
        projection: 'EPSG:4326',
        center: [-42.60, -22.41],
        zoom: 7
    })
});
