from Gestion_de_musical import get_albums
from Gestion_de_musical import get_playlists
from Gestion_de_perfil import get_users
from App import App


def main():
    """
    Función principal que inicializa la aplicación y muestra el menú principal.
    """
    # Se crea una instancia de la clase App con datos obtenidos de funciones de informacion
    app = App(get_users(), get_albums(), get_playlists())
    app.menu()


# Se llama main para iniciar la aplicación.
main()
