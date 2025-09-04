import enum
from Singleton import Singleton


class LogScope(enum.StrEnum):
    Info = "INFO"
    Warning = "WARN"
    Error = "ERR"
    Critical = "CRIT"


class Logger(Singleton):
    @staticmethod
    def __format_message(scope: LogScope, message: str) -> str:
        return f"{scope.value}: {message}"

    @staticmethod
    def print_message(scope: LogScope, message: str) -> None:
        print (Logger.__format_message(scope, message))

    def info(self, message: str) -> None:
        self.print_message(LogScope.Info, message)

    def warning(self, message: str) -> None:
        self.print_message(LogScope.Warning, message)

    def error(self, message: str) -> None:
        self.print_message(LogScope.Error, message)

    def critical(self, message: str) -> None:
        self.print_message(LogScope.Critical, message)
