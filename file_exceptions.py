class FileNotExpectedTypeError(Exception):
    """
    Raised when the file uploaded isn't the right type
    """
    pass

class IllegalArgumentError(ValueError):
    """
    Raised if input from commandline exceeds 2 arguments
    """
    pass