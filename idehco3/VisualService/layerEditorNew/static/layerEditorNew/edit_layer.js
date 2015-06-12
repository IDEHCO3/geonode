/**
 * Created by indeco on 5/28/15.
 */
var raster = new ol.layer.Tile({
  source: new ol.source.MapQuest({layer: 'sat'})
});

var  data_geo = document.getElementById("data_geo");
data_geo = JSON.parse(data_geo.innerText.toString());

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
      'geometry': data_geo
    }]
};

var b = new ol.source.GeoJSON({'object': geojsonObject, projection: 'EPSG:3857'});
var source2 = new ol.layer.Vector({source : b});

var map = new ol.Map({
  layers: [raster, source2],
  target: 'map',
  view: new ol.View({
    projection: 'EPSG:3857',
    center: [0, 0],
    zoom: 2
  })
});

// The features are not added to a regular vector layer/source,
// but to a feature overlay which holds a collection of features.
// This collection is passed to the modify and also the draw
// interaction, so that both can add or modify features.
var featureOverlay = new ol.FeatureOverlay({
  style: new ol.style.Style({
    fill: new ol.style.Fill({
      color: 'rgba(255, 255, 255, 0.2)'
    }),
    stroke: new ol.style.Stroke({
      color: '#ffcc33',
      width: 2
    }),
    image: new ol.style.Circle({
      radius: 7,
      fill: new ol.style.Fill({
        color: '#ffcc33'
      })
    })
  })
});
featureOverlay.setMap(map);
featureOverlay.setFeatures(new ol.Collection(source2.getSource().getFeatures()));

var modify = new ol.interaction.Modify({
  features: featureOverlay.getFeatures(),
  // the SHIFT key must be pressed to delete vertices, so
  // that new vertices can be drawn at the same position
  // of existing vertices
  deleteCondition: function(event) {
    return ol.events.condition.shiftKeyOnly(event) &&
        ol.events.condition.singleClick(event);
  }
});
map.addInteraction(modify);

var draw; // global so we can remove it later
function addInteraction() {
  draw = new ol.interaction.Draw({
    features: featureOverlay.getFeatures(),
    type: /** @type {ol.geom.GeometryType} */ (typeSelect.value)
  });
  map.addInteraction(draw);
}

var typeSelect = document.getElementById('type');


/**
 * Let user change the geometry type.
 * @param {Event} e Change event.
 */
typeSelect.onchange = function(e) {
  map.removeInteraction(draw);
  addInteraction();
};

addInteraction();

var save = function(){
  var format = new ol.format.GeoJSON();
  var features = map.getInteractions().getFeature();
  var json = format.writeFeatures(features);
  var text = JSON.stringify(json);
  console.log(text);
}

$("#writeLayer").on('click', save);