from song import Song
import json


class Playlist:
    minimum_bitrate = 128

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if isinstance(song, Song):
            self.songs.append(song)
        else:
            raise TypeError('"Please, use type "Song"!')

    def remove_song(self, song_to_remove_title):
        self.songs = [song for song in self.songs
                      if song.title != song_to_remove_title]

    def total_length(self):
        length = 0
        for song in self.songs:
            length += song.length
        return length

    def remove_disrated(self, rating):
        for song in self.songs:
            if song.rating <= rating and rating in range(Song.minimum_rating, Song.maximum_rating):
                self.remove_song(song.title)
        #if rating in range(Song.minimum_rating, Song.maximum_rating + 1):
        #    self.songs = [s for s in self.songs if s.rating >= rating]
            else:
                message = "Rating must be in the range [{},{}]"
                raise ValueError(message.format(
                    Song.minimum_rating, Song.maximum_rating)
                )

    def remove_bad_quality(self):
        self.songs = [s for s in self.songs if s.bitrate >= self.MIN_BITRATE]

    def show_artists(self):
        artists = set()
        for song in self.songs:
            artists.add(song.artist)
        return list(artists)

    def __str__(self):
        result = ""
        for i in range(len(self.songs)):
            result += str(self.songs[i])
            if i != len(self.songs) - 1:
                result += "\n"
        return result

    def to_JSON(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def save(self, file_name):
        with open(file_name, "w") as writeFile:
            writeFile.write(self.to_JSON())

    @staticmethod
    def load(file_name):
        with open(file_name, "r") as readFile:
            source = json.loads(readFile.read())
            playlist = Playlist(source["name"])
            for song in source["songs"]:
                playlist.add_song(Song(**song))
            return playlist
