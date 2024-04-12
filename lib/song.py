class Song:
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}
    count = 0  

    @classmethod
    def add_song_to_genre(cls, genre):
        '''Class method to keep track of the genre of each song'''
        cls.genres.add(genre)
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_song_to_artist(cls, artist):
        '''Class method to keep track of the artist of each song'''
        cls.artists.add(artist)
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

    @classmethod
    def add_song_to_count(cls):
        '''Class method to increment the count of Song objects'''
        cls.count += 1

    def __init__(self, name, artist, genre):
        '''Initialize a Song object with name, artist, and genre'''
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_genre(genre)
        Song.add_song_to_artist(artist)
        Song.add_song_to_count()

    pass
