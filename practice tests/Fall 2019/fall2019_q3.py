from typing import List, Tuple, Optional


class Playlist:
    """A class to represent a list of songs

    === Attributes ===
    songs_list: A list of all the songs that are currently present in the
                playlist
    current_song_index: the index of the current song
    """
    # Attribute types:
    songs_list: list[tuple]
    current_song_index = 0

    def __init__(self):
        """Initalises the class playlist
        """
        self.songs_list = []
        self.current_song_index = 0

    def add_song(self, song_name: str, song_artist: str, song_length: float) ->\
            None:
        """Adds a song to the current playlist with the song_name, song_artist
        and song_length
        """

        song_tuple = (song_name, song_artist, song_length)

        if len(self.songs_list) == 0:
            self.songs_list.append(song_tuple)
        else:
            for item in self.songs_list:
                if song_tuple[0] == item[0]:
                    return None
                else:
                    self.songs_list.append(song_tuple)

    def get_total_duration(self) -> int:
        """Returns the total duration of the playlist
        """
        total_duration = 0
        for item in self.songs_list:
            total_duration = total_duration + item[2]
        return total_duration

    def play_next(self) -> Optional[str]:
        """Returns the next song that is being played and its artist
        """
        if len(self.songs_list) == 0:
            return None
        else:
            name = self.songs_list[self.current_song_index][0]
            artist = self.songs_list[self.current_song_index][1]
            self.current_song_index += 1
            return str(name) + ' by ' + str(artist)

    def reset(self) -> None:
        """Resets the playlist to the beginning
        """
        self.current_song_index = 0

    def get_songs_by(self, artist: str) -> list[str]:
        """Return a list of all the songs by a given artist
        """
        returned_list = []
        for item in self.songs_list:
            if item[1] == artist:
                returned_list.append(item[0])

        return returned_list


p1 = Playlist()
p1.add_song("Free Falling", "Tom Petty", 4.5)
p1.add_song('Zombie Zoo', 'Tom Petty', 3.5)
p1.get_songs_by('Tom Petty')
