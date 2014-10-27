#!/usr/bin/env python3

from datetime import timedelta


class Song():

    minimum_rating = 1
    maximum_rating = 5

    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = 0
        self.length = length
        self.bitrate = bitrate

    def rate(self, rating):
        if rating in range(self.minimum_rating, self.maximum_rating + 1):
            self.rating = rating
        else:
            raise ValueError('Choose value between {0} and {1}'.format(
                self.minimum_rating, self.maximum_rating))

    def __str__(self):
        time = timedelta(seconds=self.length)
        return "{} {} - {}".format(self.artist, self.title, time)
