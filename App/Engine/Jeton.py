class Rond:
    def __init__(self):
        self.caractere = "O"

    def get_caractere(self):
        return self.caractere

    def __str__(self):
        return self.caractere


class Croix:
    def __init__(self):
        self.caractere = "X"

    def get_caractere(self):
        return self.caractere

    def __str__(self):
        return self.caractere
