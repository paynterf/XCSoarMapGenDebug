# -*- coding: utf-8 -*-
class GeoPoint(object):
    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat

    def __str__(self):
        return "{}, {}".format(self.lat, self.lon)