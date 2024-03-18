from User import User


class Musician(User):
    """Clase que representa a un músico, hereda de la clase User."""

    def __init__(self, id, name, email, username, type, albums, album_tracklist, t10_songs, total_listens):
        """
        Inicializa un objeto Musician.

        Parámetros:
            id (int): Identificador del músico.
            name (str): Nombre del músico.
            email (str): Correo electrónico del músico.
            username (str): Nombre de usuario del músico.
            type (str): Tipo de usuario.
            albums (list): Lista de objetos Album que el músico ha publicado.
            album_tracklist (list): Lista de listas que contienen las canciones de cada álbum.
            t10_songs (list): Lista de las 10 mejores canciones del músico.
            total_listens (int): Número total de escuchas de las canciones del músico.
        """
        super().__init__(id, name, email, username, type)
        self.albums = albums
        self.album_tracklist = album_tracklist
        self.t10_songs = t10_songs
        self.total_listens = total_listens

    def show_albums(self):
        """
        Genera una cadena de texto con información sobre los álbumes del músico.

        Return:
            str: Cadena de texto con información sobre los álbumes.
        """
        msj = ""
        for a in self.albums:
            msj += a.show()
        return msj

    def show_tracklist(self):
        """
        Genera una cadena de texto con información sobre las listas de canciones de los álbumes del músico.

        Return:
            str: Cadena de texto con información sobre las listas de canciones.
        """
        msj = ""
        for t in self.albums:
            msj += t.show()
        return msj

    def show(self):
        """
        Genera una cadena de texto con toda la información del músico.

        Return:
            str: Cadena de texto legible con información del músico.
        """
        return f"""
    {super().show()}
    Albumes: {self.show_albums()}
    Tracklists: {self.show_tracklist()}
    Top 10 canciones: {self.t10_songs}
    Total de escuchas: {self.total_listens}
    """
