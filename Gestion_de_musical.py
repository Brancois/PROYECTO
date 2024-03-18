import requests
import json
import uuid
from Song import Song
from Album import Album
from Playlist import Playlist


def get_playlists():
    """
    Obtiene la informacion de playlists de la API.

    Return:
        Un diccionario que contiene la información de la API de playlists.
    """
    response = requests.get(
        'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json')
    data = json.loads(response.text)
    return data


def get_albums():
    """
    Obtiene los informacion de álbumes de la API.

    Return:
        Un diccionario que contiene la informacion de la API de playlists.
    """
    response = requests.get(
        'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json')
    data = json.loads(response.text)
    return data


class GestionDeMusical:
    """
    Clase para gestionar la música, es decir, los álbumes y listas de reproducción.

    Args:
        album_data (list): Una lista de diccionarios representando datos de álbum.
        playlist_data (list): Una lista de diccionarios representando datos de listas de reproducción.

    Attributes:
        album_data (list): Datos de álbum.
        playlist_data (list): Datos de listas de reproducción.
        albums (list): Lista de objetos Album.
        songs (list): Lista de objetos Song.
        playlists (list): Lista de objetos Playlist.
    """

    def __init__(self, album_data, playlist_data):
        """
        Inicializa la clase, es el constructor.
        """
        self.album_data = album_data
        self.playlist_data = playlist_data
        self.albums = []
        self.songs = []
        self.playlists = []

    def register(self):
        """
        Registra los álbumes y playlists en forma de objetos, utilizando los datos de la API.
        """
        for album in self.album_data:
            id = album['id']
            name = album['name']
            description = album['description']
            cover = album['cover']
            published = album['published']
            genre = album['genre']
            artist = album['artist']
            tracklist = []
            for t in album['tracklist']:
                song_id = t['id']
                song_name = t['name']
                duration = t['duration']
                link = t['link']
                new_song = Song(song_id, song_name, duration, link)
                tracklist.append(new_song)
            new_album = Album(id, name, description, cover,
                              published, genre, artist, tracklist)
            self.albums.append(new_album)

        for playlist in self.playlist_data:
            id = playlist['id']
            name = playlist['name']
            description = playlist['description']
            creator = playlist['creator']
            tracks = []
            for s in playlist['tracks']:
                tracks.append(s)
            new_playlist = Playlist(id, name, description, creator, tracks)
            self.playlists.append(new_playlist)

    def create_album(self, musician):
        """
        Crea un nuevo álbum con la información proporcionada.

        Args:
            musician (objeto): Objeto que representa al músico creador del álbum.
        """
        id = uuid.uuid4()
        name = input('Ingrese el nombre del album: ')
        description = input('Ingrese una descripcion del album: ')
        cover = input(
            'Ingrese un link con la foto de la portada de su album: ')
        date = input(
            'Ingrese la fecha de hoy (fecha de publicacion del album): ')
        genre = input('Ingrese el genero musical de su album: ')
        artist = musician.name
        tracklist = []
        while True:
            song_id = uuid.uuid4()
            song_name = input('Ingrese el nombre de la cancion: ')
            song_duration = input('Ingrese la duracion de la cancion: ')
            song_link = input('Ingrese el link de la cancion: ')
            new_song = Song(song_id, song_name, song_duration, song_link)
            tracklist.append(new_song)
            option = input('Desea agregar otra cancion?: ').lower()
            if option == 'si':
                continue
            elif option == 'no':
                break
        new_album = Album(id, name, description, cover,
                          date, genre, artist, tracklist)
        musician.albums.append(new_album)
        self.albums.append(new_album)

    def confirm_musician(self, name):
        """
        Confirma si el usuario con el nombre dado es un músico registrado.

        Args:
            name (str): El nombre del músico a confirmar.

        Return:
            objeto or None: Si se encuentra el músico, devuelve el objeto de músico correspondiente. Si no, devuelve None.
        """
        for user in self.users:
            if user.name == name:
                for u in self.users:
                    if u.type == 'musician':
                        return user
        return None

    def create_playlist(self, listener):
        """
        Crea una nueva lista de reproducción con la información proporcionada.

        Args:
            listener (objeto): Objeto que representa al oyente que crea la lista de reproducción.
        """
        id = uuid.uuid4
        name = input('Ingrese iun nombre para su playlist: ')
        description = input('Ingrese una descripcion de su playlist: ')
        creator = listener.name
        tracks = input('Ingrese los id de las canciones que desea agregar: ')
        new_playlist = Playlist(id, name, description, creator, tracks)
        listener.plalists.append(new_playlist)

    def confirm_listener(self, name):
        """
        Confirma si el usuario con el nombre dado es un oyente registrado.

        Args:
            name (str): El nombre del oyente a confirmar.

        Returns:
            objeto or None: Si se encuentra el oyente, devuelve el objeto de oyente correspondiente. Si no, devuelve None.
        """
        for user in self.users:
            if user.name == name:
                for u in self.users:
                    if u.type == 'listener':
                        return user
        return None
