class Friend:
    """
    Clase que representa a un amigo participante en el juego del Amigo Invisible.
    """

    def __init__(self, name, email):
        """
        Inicializa una instancia de Friend.

        Args:
            name (str): Nombre del amigo.
            email (str): Dirección de correo electrónico del amigo.
        """
        self.name = name
        self.email = email

    def get_name(self):
        """
        Obtiene el nombre del amigo.

        Returns:
            str: Nombre del amigo.
        """
        return self.name

    def get_email(self):
        """
        Obtiene la dirección de correo electrónico del amigo.

        Returns:
            str: Dirección de correo electrónico del amigo.
        """
        return self.email