class Jeton:
    def __init__(self, caratere: str):
        self.caractere = caratere

    def get_caractere(self):
        return self.caractere

    def __str__(self):
        return self.caractere

    def __eq__(self, other):
        if not isinstance(other, Jeton):
            return False

        return self.caractere == other.caractere

    def __repr__(self):
        return f"Jeton({self.caractere})"


class Rond(Jeton):
    def __init__(self):
        super().__init__("O")


class Croix(Jeton):
    def __init__(self):
        super().__init__("X")