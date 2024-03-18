class Playlist:
    """
    Representa una lista de reproducción que contiene varias canciones.
    """

    def __init__(self, id,  name, description, creator, tracks):
        """
        Inicializa una nueva instancia de Playlist.

        Args:
            id (int): El identificador único de la lista de reproducción.
            name (str): El nombre de la lista de reproducción.
            description (str): La descripción de la lista de reproducción.
            creator (str): El nombre del escucha de la lista de reproducción.
            tracks (list): Lista de canciones que pertenecen a la lista de reproducción.
        """
        self.id = id
        self.name = name
        self.description = description
        self.tracks = tracks
        self.creator = creator

    def show_tracks(self):
        """
        Devuelve una cadena de texto que representa todas las canciones de la lista de reproducción.

        Return:
            str: Una cadena de texto que contiene el nombre de cada canción en la lista de reproducción.
        """
        msj = ""
        for track in self.tracks:
            msj += track
        return msj

    def show(self):
        """
        Devuelve una cadena de texto que representa la información completa de la lista de reproducción.

        Return:
            str: Una cadena de texto que contiene el Id, título, descripción, creador y canciones de la lista de reproducción.
        """
        return f"""
    Id : {self.id}
    Titulo: {self.name}
    Descripcion: {self.description}
    Creador: {self.creator}
    Canciones: {self.show_tracks()}
    """
