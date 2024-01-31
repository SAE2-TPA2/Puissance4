# Exception lorsque une colonne est pleine

class ColonnePleineException(Exception):
    def __init__(self, message):
        super().__init__(message)
