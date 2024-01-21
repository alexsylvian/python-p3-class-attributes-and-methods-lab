class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        print(cls.genres)
        cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        print(cls.artists)
        cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls):
        if not cls.genre_count:
            cls.genre_count = {}

        for genre in cls.genres:
            cls.genre_count[genre] = 0

        for genre in cls.genres:
            cls.genre_count[genre] += 1


    @classmethod
    def add_to_artist_count(cls):
        if not cls.artist_count:
            cls.artist_count = {}

        for artist in cls.artists:
            cls.artist_count[artist] = 0

        for artist in cls.artists:
            cls.artist_count[artist] += 1


