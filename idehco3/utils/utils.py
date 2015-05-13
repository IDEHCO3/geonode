
import unicodedata
import simplejson
from django.http import HttpResponse
import shapefile

class JsonResponse(HttpResponse):
    """
        JSON Response
    """
    def __init__(self, content, mimetype='application/json', status=None, content_type=None):
        super(JsonResponse, self).__init__(
            content=simplejson.dumps(content),
            mimetype=mimetype,
            status=status,
            content_type=content_type
        )

class GeoJson:
    def __init__(self):
        self.data = {"type": "FeatureCollection"}
        self.data["features"] = []

    def addFeature(self, geometry, properties):
        if geometry or properties:
            feature = {"type": "Feature", "geometry": geometry, "properties": properties}
            self.data["features"].append(feature)

    def addGeometry(self, type, coordinates):
        if type == "Line":
            type = "LineString"
        if type == "MultiLine":
            type = "MultiLineString"
        types = ["Point", "LineString", "Polygon", "MultiPoint", "MultiLineString", "MultiPolygon"]
        if type or coordinates or type not in types:
            geometry = {"type": type, "coordinates": coordinates}
            return geometry
        else:
            return None

    def addGeometryCollection(self, geometries):

        if type(geometries) is not dict:
            return None

        if geometries and geometries[0].has_key("type") and geometries[0].has_key("coordinates"):
            return {"type": "GeometryCollection", "geometries": geometries}
        else:
            return None

    def addCRS(self, projection):
        self.data["crs"] = {"type": "name", "properties": {"name": projection}}

    def getGeoJsonData(self):
        return self.data

def getGeoJsonURLFromLayer(layer):
    url = "http://localhost:8080/geoserver/geonode/wfs?service=wfs&version=2.0.0&request=GetFeature&"
    url = url + "typeNames=" + unicodeToString(layer.typename) + "&srsName=EPSG:4326&outputformat=application/json"
    return url

def getGeoJsonFromLayer(layer):
    layer_file = layer.get_base_file()[0]
    if layer_file == None:
        print "There isn't a reference to the shapefile."
        return None

    layer_path = unicodeToString(layer_file.file._get_path())
    shape_file = shapefile.Reader(layer_path)
    geojson_shape = GeoJson()
    #TODO - It is need to iterate for shape_file records and put it inside geojson_shape, and in the end return the geojson_file

    return geojson_shape



def unicodeToString(text):
    return unicodedata.normalize("NFKD", text).encode('ascii', 'ignore')