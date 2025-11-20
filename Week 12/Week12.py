#Problem 9
class Playlist:
    def __init__(self, name = "New Playlist", songs = []):
        self.name = name
        self.songs = songs
    def add_song(self, song):
        self.songs.append(song)
    def __add__(self, other):
        combined_name = f'{self.name} & {other.name}'
        combined_songs = self.songs + other.songs
        return Playlist(combined_name, combined_songs)
    def __str__(self):
        return f"{self.name} playlist has these songs: {self.songs}"

p1 = Playlist("Christmas", ["Jingle Bells", "Mr. Grinch"])
p2 = Playlist("Country", ["Last Night", "What I Want"])
p1.add_song("Mistle Toe")
new_p = p1 + p2
print(new_p)