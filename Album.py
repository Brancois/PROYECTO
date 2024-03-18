class Album:
    """
    Representa un álbum musical.
    """

    def __init__(self, id, name, description, cover, published,  genre, artist, tracklist):
        """
        Inicializa una instancia de la clase Album con los atributos proporcionados.

        Args:
            id (int): El id único del álbum.
            name (str): El nombre del álbum.
            description (str): Una descripción del álbum.
            cover (str): La URL de la portada del álbum.
            published (str): La fecha de publicación del álbum.
            genre (str): El género musical del álbum.
            artist (str): El nombre del musico que creó el álbum.
            tracklist (list): Una lista de objetos de canciones que forman la tracklist del álbum.
        """
        self.id = id
        self.name = name
        self.description = description
        self.cover = cover
        self.published = published
        self.genre = genre
        self.artist = artist
        self.tracklist = tracklist

    def show_tracklist(self):
        """
        Devuelve una representación de cadena de la tracklist del álbum.

        Returns:
            str: Una representación de cadena que muestra la lista de canciones del álbum.
        """
        msj = ""
        for song in self.tracklist:
            msj += song.show()
        return msj

    def show(self):
        """
        Devuelve una representación legible del álbum.

        Returns:
            str: Una representación legible que muestra los detalles del álbum, incluida su tracklist.
        """
        return f"""
    Id: {self.id}
    Nombre: {self.name}
    Descripcion: {self.description}
    Portada: {self.cover}
    Publicado: {self.published}
    Genero: {self.genre}
    Artista: {self.artist}
    Likes: {self.likes}
    Tracklist: {self.show_tracklist()}
    """
