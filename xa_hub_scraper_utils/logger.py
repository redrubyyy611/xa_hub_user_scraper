from colorama import Fore, Style


def info_log(message: str) -> None:
    """
    Prints an info log message.
    Args:
        message (str): The message to log.
    """
    print(f"> {Fore.BLUE}{message}{Fore.RESET}{Style.RESET_ALL}")


def error_log(message: str) -> None:
    """
    Prints an error log message.
    Args:
        message (str): The message to log.
    """
    print(f"> {Fore.RED}{message}{Fore.RESET}{Style.RESET_ALL}")


def warning_log(message: str) -> None:
    """
    Prints a warning log message.
    Args:
        message (str): The message to log.
    """
    print(f"> {Fore.YELLOW}{message}{Fore.RESET}{Style.RESET_ALL}")


def success_log(message: str) -> None:
    """
    Prints a success log message.
    Args:
        message (str): The message to log.
    """
    print(f"> {Fore.GREEN}{message}{Fore.RESET}{Style.RESET_ALL}")


def bold_text(message: str) -> str:
    """
    Returns the message in bold text.
    Args:
        message (str): The message to format.
    Returns:
        str: The formatted message.
    """
    return f"{Style.BRIGHT}{message}{Style.RESET_ALL}"
