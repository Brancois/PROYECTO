class Song:
    """Clase que representa una canción.
    """

    def __init__(self, id, name, duration, link):
        """Inicializa una instancia de la clase Song.

        Args:
            id (int): El identificador único de la canción.
            name (str): El nombre de la canción.
            duration (str): La duración de la canción.
            link (str): El enlace de la canción.
        """
        self.id = id
        self.name = name
        self.duration = duration
        self.link = link

    def show(self):
        """Muestra la información de la canción.

        Return:
            str: Una cadena de texto que contiene la información de la canción.
        """
        return f"""
    Id: {self.id}
    Nombre: {self.name}
    Duracion: {self.duration}
    Link: {self.link}
    """
