
class UserInputException(Exception):
    pass

class UnknownCommand(UserInputException):
    def __init__(self, command):
        message = (
            'неизвестная команда \'' + command + '\''
        )
        super().__init__(message)

class WrongCommandFormat(UserInputException):
    def __init__(self, reason):
        message = (
            'неверный формат команды. ' + reason
        )
        super().__init__(message)
