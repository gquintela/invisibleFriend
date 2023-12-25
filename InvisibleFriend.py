import random

class InvisibleFriend:
    """
    Clase que representa el juego del Amigo Invisible.
    """
    def __init__(self, friend_list, email_sender, mail_key ):
        """
        Inicializa una instancia de InvisibleFriend.

        Args:
            friend_list (list): Lista de objetos Friend que representan a los participantes.
            email_sender (str): Dirección de correo electrónico para enviar los mails.
            mail_key (str): Clave de acceso para enviar correos electrónicos.
        """
        self.friend_list = friend_list
        self.email_sender = email_sender
        self.mail_key = mail_key

    def shuffle_friend_list(self):
        """
        Mezcla la lista de amigos para asignar regalos de forma aleatoria.
        """
        random.shuffle(self.friend_list)

    def send_emails(self):
        """
        Envía correos electrónicos a cada participante indicándole a quién debe hacerle regalo.
        """
        for i in range(len(self.friend_list) - 1):
            # el i amigo le tiene que regalar al amigo i + 1
            self.send_email(self.friend_list[i].get_name(),self.friend_list[i + 1].get_email())

        # el ultimo amigo le tiene que regalar al primero
        last_position = len(self.friend_list) - 1
        self.send_email(self.friend_list[last_position].get_name(),self.friend_list[0].get_email())

    def send_email(self, friend_name, friend_to_gift_email):
        """
        Envía un correo electrónico a un amigo con la información de a quién debe hacerle regalo.

        Args:
            friend_name (str): Nombre del amigo al que se le hará el regalo.
            friend_to_gift_email (str): Dirección de correo electrónico del amigo al que se le hará el regalo.
        """

        # CAMBIAR METODO PARA QUE MANDE EL MAIL, TENES PARA USAR 
        # self.email_sender y self.mail_key
        print(f"Este mail se envia a {friend_to_gift_email}:")
        print(f"Le tenés que regalar a {friend_name}\n")
