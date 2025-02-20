class NegativeNumberError(Exception):
    def __init__(self, message: str = "Negative number is not allowed"):
        super().__init__(message)


class ZeroOrNegativeNumberError(Exception):
    def __init__(
        self, message: str = "Zero or negative number is not allowed"
    ):
        super().__init__(message)


class CharacterNotFoundError(Exception):
    def __init__(self, char_id: int):
        message = f"Character with ID {char_id} not found"
        super().__init__(message)
