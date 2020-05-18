
class Error(Exception):
   """Base class for other exceptions"""
   pass

class AddTransactionError(Error):
    """Raised when you can't create a transaction for Person"""
    pass

class InvalidNumberError(Error):
    """Raised when input is not an int or float"""
    pass

class InvalidDateError(Error):
    """Raised when date string is not a valid date"""
    pass
