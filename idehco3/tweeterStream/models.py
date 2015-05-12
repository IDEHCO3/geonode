from django.db import models
from geonode.people.models import Profile

# Create your models here.
import tweepy

from idehco3.utils.utils import GeoJson, unicodeToString

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
        return geojson_object.getGeoJsonData()
