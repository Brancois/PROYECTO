import requests
import json
import uuid
import pickle
from Listener import Listener
from Musician import Musician


def get_users():
    """
    Obtiene los datos de usuarios desde la API.

    Return:
        Un diccionario que contiene la información de la API de usuarios.
    """
    response = requests.get(
        'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json')
    data = json.loads(response.text)
    return data


class GestionDePerfil:
    """Clase para gestionar perfiles de usuarios."""

    def __init__(self, data):
        """
        Inicializa la clase, es decir, es el constructor.

        Args:
            data (list): Lista de datos de usuarios desde la API.
        """
        self.data = data
        self.users = []
        self.listeners = []
        self.musicians = []

    def register(self):
        """Registra usuarios en la lista de usuarios."""
        for user in self.data:
            id = user['id']
            name = user['name']
            email = user['email']
            username = user['username']
            type = user['type']
            if type == 'listener':
                liked_albums = []
                liked_songs = []
                playlists = []
                new_listener = Listener(
                    id, name, email, username, type, liked_albums, liked_songs, playlists)
                self.listeners.append(new_listener)
                self.users.append(new_listener)
            elif type == 'musician':
                albums = []
                album_tracklist = []
                t10_songs = []
                total_listens = []
                new_musician = Musician(
                    id, name, email, username, type, albums, album_tracklist, t10_songs, total_listens)
                self.musicians.append(new_musician)
                self.users.append(new_musician)

    def search_user(self, users_name):
        """
        Busca un usuario por su nombre.

        Args:
            users_name (str): Nombre del usuario a buscar.

        Returns:
            objeto o None: El usuario si se encuentra, lo retorna, pero retorna None si no se encuentra.
        """
        for user in self.users:
            if user.name == users_name:
                return user
        return None

    def confirm_user(self, email):
        """
        Confirma la existencia de un usuario por su correo electrónico.

        Args:
            email (str): Correo electrónico del usuario a confirmar.

        Returns:
            objeto o None: El usuario si se encuentra, None si no se encuentra.
        """
        for user in self.users:
            if user.email == email:
                return user
        return None

    def add_user(self):
        """Agrega un nuevo usuario."""
        id = uuid.uuid4()
        name = input("Ingrese su nombre: ")
        email = input("Ingrese su correo electronico: ")
        username = input("Ingrese un nombre de usuario: ")
        type = input("Ingrese si es musico o escucha: ")
        if type.lower() == 'escucha':
            type = 'listener'
            liked_albums = []
            liked_songs = []
            playlists = []
            new_listener = Listener(
                id, name, email, username, type, liked_albums, liked_songs, playlists)
            self.listeners.append(new_listener)
            self.users.append(new_listener)
        elif type.lower() == 'musico':
            type = 'musician'
            albums = []
            album_tracklist = []
            t10_songs = []
            total_listens = []
            new_musician = Musician(
                id, name, email, username, type, albums, album_tracklist, t10_songs, total_listens)
            self.musicians.append(new_musician)
            self.users.append(new_musician)

    def delete_user(self, user):
        """
        Elimina un usuario.

        Args:
            user (User): Usuario a eliminar.
        """
        while True:
            confirm = input(
                'Esta seguro que desea eliminar su cuenta? Este proceso es irreversible... ')
            if confirm.lower() == 'si':
                self.users.remove(user)
                if user in self.listeners:
                    self.listeners.remove(user)
                if user in self.musicians:
                    self.musicians.remove(user)
                break
            elif confirm.lower() == 'no':
                break

    def change_user_info(self, user):
        """
        Cambia la información de un usuario.

        Args:
            user (User): Usuario al que se le cambiará la información.

        Returns:
            User: El usuario con la información actualizada.
        """
        name = input('Ingrese su nuevo nombre: ')
        username = input('Ingrese su nuevo usuario: ')
        user.name = name
        user.username = username
        return user

    def add_objects(self):
        """Agrega objetos a un archivo de texto."""
        with open('users.txt', 'wb') as f:
            pickle.dump(self.users, f)
            pickle.dump(self.musicians, f)
            pickle.dump(self.listeners, f)

    def load_objects(self):
        """Carga objetos desde un archivo de texto."""
        with open('users.txt', 'rb') as f:
            self.users = pickle.load(f)

    def menu(self):
        """Despliega un menú de opciones."""
        print("""Por favor, elija cual informacion desea utilizar:
        1. Info del JSON
        2. Info del TXT""")
        data_option = input('Ingrese su opcion: ')
        while not data_option.isnumeric():
            data_option = input('Ingrese su opcion: ')
        if data_option == '1':
            self.register()
        elif data_option == '2':
            self.load_objects()
        while True:
            print("***GESTION DE PERFIL***")
            options = ['Acceder Cuenta', 'Agregar Cuenta', 'Buscar perfil por nombre',
                       'Cambiar datos de cuenta', 'Eliminar cuenta', 'Salir']
            for i in range(len(options)):
                print(f"{i+1}. {options[i]}")
            option = input('Ingrese su opcion: ')
            while not option.isnumeric() or (int(option)-1) not in range(len(options)):
                option = input('Ingrese su opcion: ')
            if option == '1':
                email = input('Ingrese su correo electronico: ')
                user = self.confirm_user(email)
                if user == None:
                    print('Este usuario no se encuentra registrado!')
                    x = input('Desea registrarse? ').lower()
                    if x == 'si':
                        self.add_user()
                    elif x == 'no':
                        continue
                else:
                    print(user.show())
            elif option == '2':
                self.add_user()
            elif option == '3':
                users_name = input(
                    'Ingrese el nombre del del musico/escucha que desea buscar: ')
                user = self.search_user(users_name)
                if user != None:
                    print(user.show())
                else:
                    print(
                        'Disculpa, parace que ese usuario no se encuentra registrado!')
            elif option == '4':
                email = input('Por favor ingrese su correo electronico: ')
                user = self.confirm_user(email)
                if user != None:
                    self.change_user_info(user)
                else:
                    print('Disculpa, parece que ese usuario no esta registrado')
            elif option == '5':
                email = input('Ingrese su correo registrado: ')
                user = self.confirm_user(email)
                if user != None:
                    self.delete_user(user)
                    print('Usuario eliminado!')
            elif option == '6':
                self.add_objects()
                break
