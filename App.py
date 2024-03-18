import uuid
from Listener import Listener
from Musician import Musician
import pickle
from Album import Album
from Song import Song
from Playlist import Playlist


class App:
    """
    Esta clase representa una aplicación que gestiona usuarios, álbumes y listas de reproducción.
    """

    def __init__(self, user_data, album_data, playlist_data):
        """
        Inicializa la aplicación con datos de usuarios, álbumes y listas de reproducción.

        Args:
            user_data (list): Datos de usuarios.
            album_data (list): Datos de álbumes.
            playlist_data (list): Datos de listas de reproducción.
        """
        self.user_data = user_data
        self.album_data = album_data
        self.playlist_data = playlist_data
        self.users = []
        self.albums = []
        self.playlists = []

    def register(self):
        """
        Registra usuarios, álbums y playlists.
        """
        # Registro de usuarios
        for user in self.user_data:
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
                self.users.append(new_listener)
            elif type == 'musician':
                albums = []
                album_tracklist = []
                t10_songs = []
                total_listens = []
                new_musician = Musician(
                    id, name, email, username, type, albums, album_tracklist, t10_songs, total_listens)
                self.users.append(new_musician)

        # Registro de albumes
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
            for user in self.users:
                if user.id == artist:
                    user.albums.append(new_album)
            self.albums.append(new_album)

        # Registro de playlists
        for playlist in self.playlist_data:
            id = playlist['id']
            name = playlist['name']
            description = playlist['description']
            creator = playlist['creator']
            tracks = []
            for s in playlist['tracks']:
                tracks.append(s)
            new_playlist = Playlist(id, name, description, creator, tracks)
            for user in self.users:
                if user.id == creator:
                    user.playlists.append(new_playlist)
            self.playlists.append(new_playlist)

    def search_user(self, users_name):
        """
        Busca un usuario por su nombre.

        Args:
            users_name (str): Nombre del usuario a buscar.

        Return:
            objeto: Objeto del usuario si se encuentra, None si no lo encuentra.
        """
        for user in self.users:
            if user.name == users_name:
                return user
        return None

    def confirm_user(self, email):
        """
        Confirma la existencia de un usuario mediante su correo electrónico.

        Args:
            email (str): Correo electrónico del usuario a confirmar.

        Return:
            objeto: Objeto del usuario si se encuentra, None si no lo encuentra.
        """
        for user in self.users:
            if user.email == email:
                return user
        return None

    def add_user(self):
        """
        Agrega un nuevo usuario a la lista de usuarios.
        """
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
            self.users.append(new_listener)
        elif type.lower() == 'musico':
            type = 'musician'
            albums = []
            album_tracklist = []
            t10_songs = []
            total_listens = []
            new_musician = Musician(
                id, name, email, username, type, albums, album_tracklist, t10_songs, total_listens)
            self.users.append(new_musician)

    def delete_user(self, user):
        """
        Elimina un usuario de la lista de usuarios.

        Args:
            user (object): Objeto del usuario a eliminar.
        """
        while True:
            confirm = input(
                'Esta seguro que desea eliminar su cuenta? Este proceso es irreversible... ')
            if confirm.lower() == 'si':
                self.users.remove(user)
                break
            elif confirm.lower() == 'no':
                break

    def change_user_info(self, user):
        """
        Cambia la información de un usuario.

        Args:
            user (object): Objeto del usuario cuya información se va a cambiar.

        Return:
            objeto: Objeto del usuario con la información actualizada.
        """
        name = input('Ingrese su nuevo nombre: ')
        username = input('Ingrese su nuevo usuario: ')
        user.name = name
        user.username = username
        return user

    def create_album(self, musician):
        """
        Crea un nuevo álbum y lo asocia al músico especificado.

        Args:
            musician (object): Objeto del músico que va a crear el álbum.
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
        Confirma la existencia de un músico mediante su nombre.

        Args:
            name (str): Nombre del músico a confirmar.

        Returns:
            objeto: Objeto del músico si se encuentra, None si no lo consigue.
        """
        for user in self.users:
            if user.name == name:
                for u in self.users:
                    if u.type == 'musician':
                        return user
        return None

    def add_objects(self):
        """
        Guarda la lista de usuarios en un archivo de texto.
        """
        with open('users.txt', 'wb') as f:
            pickle.dump(self.users, f)

    def load_objects(self):
        """
        Carga la lista de usuarios desde un archivo de texto.
        """
        with open('users.txt', 'rb') as f:
            self.users = pickle.load(f)

    def create_playlist(self, listener):
        """
        Crea una nueva lista de reproducción y la asocia al oyente especificado.

        Args:
            listener (object): Objeto del oyente que va a crear la lista de reproducción.
        """
        id = uuid.uuid4()
        name = input('Ingrese un nombre para su playlist: ')
        description = input('Ingrese una descripcion de su playlist: ')
        creator = listener.name
        tracks = input('Ingrese los id de las canciones que desea agregar: ')
        new_playlist = Playlist(id, name, description, creator, tracks)
        listener.playlists.append(new_playlist)

    def confirm_listener(self, name):
        """
        Confirma la existencia de un oyente mediante su nombre.

        Args:
            name (str): Nombre del oyente a confirmar.

        Return:
            objeto: Objeto del oyente si se encuentra, None si no lo consigue.
        """
        for user in self.users:
            if user.name == name:
                for u in self.users:
                    if u.type == 'listener':
                        return user
        return None

    def search_music(self):
        """
        Busca música según criterios específicos (nombre de músico, nombre de álbum o nombre de lista de reproducción).
        """
        options = ['Por nombre del musico',
                   'Nombre del album', 'Nombre del playlist']
        for i in range(len(options)):
            print(f'{i+1}. {options[i]}')
        option = input('Como desea buscar la musica?: ')
        if option == "1":
            name = input('Ingrese el nombre del musico: ')
            for x in self.users:
                if x.name == name:
                    if x.type == 'musician':
                        for i in x.albums:
                            print(f'{x.show()}')
                    elif x.type == 'listener':
                        for i in x.playlists:
                            print(f'{x.show()}')
                else:
                    print('Disculpe, no se ha conseguido a nadie con ese nombre.')
        elif option == '2':
            name = input('Ingrese el nombre del album: ')
            for user in self.users:
                if user.type == 'musician':
                    for x in user.albums:
                        if x.name == name:
                            print(f'{x.show()}')
        elif option == '3':
            name = input('Ingrese el nombre de la playlist: ')
            for user in self.users:
                if user.type == 'listener':
                    for x in user.playlists:
                        if x.name == name:
                            print(f'{x.show()}')

    def add_like(self):
        """
        Permite al usuario dar like a diferentes tipos de elementos (canción, álbum, lista de reproducción, usuario).
        """
        print('A que le desea dar like?')
        options = ['Cancion', 'Album', 'Playlist', 'Usuario']
        for i in range(len(options)):
            print(f'{i+1}. {options[i]}')
        op = input('Ingrese su opcion: ')
        while not op.isnumeric() or (int(op)-1) not in range(len(options)):
            op = input('Ingrese su opcion: ')
        if op == '1':
            email = input('Ingrese su correo: ')
            user = self.confirm_user(email)
            if user != None:
                dar_like = input('Le quiere dar like a este perfil: ').lower()
                if dar_like == 'si':
                    user.likes += 1

    def menu(self):
        """
        Muestra un menú de opciones para acceder a diferentes módulos de la aplicación.
        """
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
            print('A que modulo desea acceder?')
            op = ['Gestion de Perfil', 'Gestion de Musical',
                  'Gestion de interacciones', 'Salir']
            for i in range(len(op)):
                print(f'{i+1}. {op[i]}')
            option = input('Ingrese su opcion: ')
            while not option.isnumeric() or (int(option)-1) not in range(len(op)):
                option = input('Ingrese su opcion: ')
            if option == '1':
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
                        email = input(
                            'Por favor ingrese su correo electronico: ')
                        user = self.confirm_user(email)
                        if user != None:
                            self.change_user_info(user)
                        else:
                            print(
                                'Disculpa, parece que ese usuario no esta registrado')
                    elif option == '5':
                        email = input('Ingrese su correo registrado: ')
                        user = self.confirm_user(email)
                        if user != None:
                            self.delete_user(user)
                            print('Usuario eliminado!')
                    elif option == '6':
                        break
            elif option == '2':
                while True:
                    print('***GESTION DE MUSICAL***')
                    options = ['Crear album', 'Crear playlist',
                               'Buscar musica', 'Salir']
                    for i in range(len(options)):
                        print(f'{i+1}. {options[i]}')
                    option = input('Ingrese su opcion: ')
                    while not option.isnumeric() or (int(option)-1) not in range(len(options)):
                        option = input('Ingrese su opcion: ')
                    if option == '1':
                        name = input('Ingrese su nombre: ')
                        musician = self.confirm_musician(name)
                        if musician != None:
                            self.create_album(musician)
                        else:
                            print(
                                'Disculpe, debe ser un musico para poder subir un album.')
                    elif option == '2':
                        name = input('Ingrese su nombre: ')
                        listener = self.confirm_listener(name)
                        if listener != None:
                            self.create_playlist(listener)
                        else:
                            print(
                                'Disculpe, debe ser esucha para crear una playlist.')
                    elif option == '3':
                        self.search_music()
                    elif option == '4':
                        break
            elif option == '3':
                while True:
                    print('***GESTION DE INTERACCIONES***')
                    options = ['Dar likes']
                    for i in range(len(options)):
                        print(f'{i+1}. {options[i]}')
                    op = input('Ingrese su opcion: ')
                    while not op.isnumeric() or (int(op)-1) not in range(len(options)):
                        op = input('Ingrese su opcion: ')
                    if op == '1':
                        self.add_like()
            elif option == '4':
                self.add_objects()
                break
