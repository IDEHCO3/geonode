from django.db import models
from geonode.people.models import Profile

# Create your models here.
import tweepy
import unicodedata

class TweeterStream(models.Model):

    name = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    center_longitude = models.FloatField()
    center_latitude = models.FloatField()
    zoom = models.IntegerField()

    creation_date = models.DateTimeField()
    init_date = models.DateTimeField()
    end_date = models.DateTimeField()

    userGeonode = models.ForeignKey(Profile)

class TwitterAuth:
    def __init__(self, consumer_key, consumer_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        try:
            self.redirect_url = self.auth.get_authorization_url()
        except tweepy.TweepError:
            print 'Error! Failed to get request token.'

    def set_access_token(self, access_token, access_token_secret):
        self.auth.set_access_token(access_token, access_token_secret)

class TwitterAPI:
    def __init__(self, auth):
        self.api = tweepy.API(auth)

    def showTweetsAndCoordinates(self):
        public_tweets = self.api.home_timeline()
        for tweet in public_tweets:
            print (tweet.text)
            print (tweet.coordinates)

    def search(self, queryString):
        self.api.search(queryString)

class GeoJson:
    def __init__(self):
        self.geojson = {"type": "FeatureCollection"}
        self.geojson["features"] = []

    def addFeature(self, geometry, properties):
        if geometry or properties:
            feature = {"type": "Feature", "geometry": geometry, "properties": properties}
            self.geojson["features"].append(feature)

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
        self.geojson["crs"] = {"type": "name", "properties": {"name": projection}}

    def getGeoJsonObject(self):
        return self.geojson


def getGeoJsonTwitter(querySearch):
    if querySearch == "" or querySearch == None:
        return ""
    consumer_key = 'ooDmh50X1AUe51gFADaKGIMmI' #owner idehco3 - id: 3062379387
    consumer_secret = 'p2o4S5HyUKwcUfdChXCj9bO0HxhLCrTwhLgjBolKC6JeXoBcUF'
    access_token_secret = 'Qaft1GE1QF5i8YOGIKJLyK6hDkjcbIvkVcnjVEymMGLTo'
    access_token = '3062379387-kH3SFHGabF0RR0afgCIRQLgcVHMlxnDf3HKq2m3'
    auth = TwitterAuth(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = TwitterAPI(auth.auth)

    data_twitter = api.search(querySearch)
    if data_twitter == None:
        return ""

    geojson_object = GeoJson()
    int_count_point = 0
    for tweet in data_twitter:
        if tweet.coordinates == None :
            continue
        int_count_point = int_count_point + 1
        geom = geojson_object.addGeometry(unicodeToString(tweet.coordinates["type"]), tweet.coordinates["coordinates"])
        prop = {"name": unicodeToString(tweet.place.name), "text": unicodeToString(tweet.text)}
        geojson_object.addCRS("EPSG:4326")
        geojson_object.addFeature(geom, prop)

    if int_count_point == 0:
        return ""
    else:
        return geojson_object.getGeoJsonObject()

def unicodeToString(text):
    return unicodedata.normalize("NFKD", text).encode('ascii', 'ignore')
