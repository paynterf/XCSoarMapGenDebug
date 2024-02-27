# -*- coding: utf-8 -*-
class GeoPoint(object):
    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat

    def __str__(self):
        return "{}, {}".format(self.lat, self.lon)

class Waypoint(GeoPoint):
    def __init__(self):
        self.altitude = None
        self.name = ""
        self.short_name = ""
        self.icao = ""
        self.country_code = ""
        self.surface = None
        self.runway_len = None
        self.runway_dir = None
        self.freq = None
        self.type = None
        self.cup_type = None
        self.comment = None

    def __str__(self):
        return "{}, {}, {}, {}".format(
            self.name, super(Waypoint, self).__str__(), self.altitude, self.type
        )