class User:
    """
    Clase que representa a un usuario.
    """

    def __init__(self, id, name, email, username, type):
        """
        Inicializa un nuevo objeto de usuario con los atributos proporcionados.

        Args:
            id (str): El identificador único del usuario.
            name (str): El nombre del usuario.
            email (str): El correo electrónico del usuario.
            username (str): El nombre de usuario del usuario.
            type (str): El tipo de usuario.
        """
        self.id = id
        self.name = name
        self.email = email
        self.username = username
        self.type = type

    def show(self):
        """
        Muestra la información del usuario.

        Return:
            str: Una cadena que representa la información del usuario.
        """
        return f"""
    Id: {self.id}
    Nombre: {self.name}
    Correo: {self.email}
    Username: {self.username}
    Tipo: {self.type}
    """
