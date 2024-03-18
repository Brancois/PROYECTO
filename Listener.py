from User import User


class Listener(User):
    """
    Clase Listener, que hereda de la clase User.
    """

    def __init__(self, id, name, email, username, type, liked_albums, liked_songs, playlists):
        """
        Inicializa un objeto Listener.

        Args:
            id (int): Identificador único del usuario.
            name (str): Nombre del usuario.
            email (str): Correo electrónico del usuario.
            username (str): Nombre de usuario único del usuario.
            type (str): Tipo de usuario.
            liked_albums (list): Lista de álbumes que le gustan al usuario.
            liked_songs (list): Lista de canciones que le gustan al usuario.
            playlists (list): Lista de playlists guardadas por el usuario.
        """
        super().__init__(id, name, email, username, type)
        self.liked_albums = liked_albums
        self.liked_songs = liked_songs
        self.playlists = playlists

    def show_playlists(self):
        """
        Muestra las playlists del usuario.

        Return:
            str: Una cadena que contiene información sobre las playlists del usuario.
        """
        msj = ""
        for p in self.playlists:
            msj += p.show()
        return msj

    def show(self):
        """
        Muestra la información del usuario, incluyendo sus gustos musicales y playlists.

        Return:
            str: Una cadena con la información del usuario.
        """
        return f"""
    {super().show()}
    Albumes likeados: {self.liked_albums}
    Canciones likeadas: {self.liked_songs}
    Playlist guardados : {self.show_playlists()}

    """
