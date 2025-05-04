class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def __str__(self):
        return f"La contraseña de {self.username} es '{self.password}'"
    
usuario1 = Usuario("Beñat", "a1b2c3")
print(usuario1)  # La contraseña de Beñat es 'a1b2c3'