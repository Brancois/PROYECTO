class GestionDeInteracciones:
    """
    Clase para gestionar interacciones como dar likes.
    """

    def __init__(self):
        """
        Constructor de la clase.
        """
        pass

    def add_like(self):
        """
        Permite al usuario dar like a diferentes tipos de contenido.
        """
        print('A que le desea dar like?')
        options = ['Cancion', 'Album', 'Playlist', 'Usuario']
        for i in range(len(options)):
            print(f'{i+1}. {options[i]}')
        op = input('Ingrese su opcion: ')
        while not op.isnumeric() or (int(op)-1) not in range(len(options)):
            op = input('Ingresesu opcion: ')
        if op == '1':
            name = input('Ingrese su nombre: ')
            user = self.validate_user(user)
            if user != None:
                dar_like = input('Le quiere dar like a este perfil: ').lower()
                if dar_like == 'si':
                    self.liked_songs += 1
