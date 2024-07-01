"""
I&CS 33 Warm up Project
Summer 2024
Author: Chenhan Lyu

When C was developed in the early 1970s,
the computing environment was vastly different.
Memory and processing power were both severely limited.
C was developed alongside Unix, primarily by the same people,
and its features were influenced by the needs and constraints of system programming in that context.
Simplicity and efficiency were paramount,
thus the use of null-terminated character arrays (C strings) was a practical choice.
In C, the terminated character is "\0".
In this Warmup project, you are required to mimic the behavior of C strings.
"""




class Cstring:
    """
    A class to mimic a C-style string using Python list to handle characters,


    Attributes:
        (list of "char" (str in python with only one character)): A list of characters representing the string with a
                           null character '\0' at the end.
    """
    def __init__(self, lst: list[str] = None):
        """
        Initializes the Cstring with an optional list of characters.

        Args:
            lst (list[str], optional): A list of characters to initialize the string.
                                       Defaults to None, which initializes an empty string.
        """
        pass

    def at(self, index: int) -> str:
        """
        Accesses the character at the specified index.

        Args:
            index (int): The index of the character to access.

        Returns:
            str: The character at the specified index.

        Raises:
            IndexError: If the index is out of the valid range
        """
        pass

    def string(self) -> str:
        """
        Returns the Python string representation of the Cstring

        Returns:
            str: The string representation.
        """
        pass

    def newString(self) -> 'Cstring':
        """
        Creates a new copy of the current Cstring.

        Returns:
            Cstring: A new instance of Cstring with the same content.
        """
        pass

    def append(self, char: str) -> None:
        """
        Appends a character to the end of the Cstring

        Args:
            char (str): The character to append.
        """
        pass
    def pop(self) -> str:
        """
        Pops and returns the first character of the Cstring.

        Returns:
            str: The character that was removed from the beginning.
        """
        pass

    def empty(self) -> None:
        """
        Empties the Cstring
        """
        pass

    def length(self) -> int:
        """
        Returns the length of the Cstring

        Returns:
            int: The length of the string.
        """
        pass

    def insert(self, index: int, char) -> None:
        """
        Inserts a character or a list of characters at a specified index.

        Args:
            index (int): The index at which to insert.
            char (str | list[str]): The character or list of characters to insert.

        Raises:
            IndexError: If the index is out of the valid range for insertion.
        """
        pass

    def replace(self, index: int, char: str) -> None:
        """
        Replaces the character at a specified index.

        Args:
            index (int): The index of the character to replace.
            char (str): The new character to be placed at the specified index.
        """
        pass

    def strstr(self, start_index: int, end_index: int) -> 'Cstring':
        """
        Extracts a substring from the Cstring and returns it as a new Cstring.

        Args:
            start_index (int): The starting index of the substring.
            end_index (int): The ending index of the substring.

        Returns:
            Cstring: The new Cstring containing the substring.

        Raises:
            IndexError: If either index is out of range.
        """
        pass

    def strrchr(self, char: str) -> int:
        """
        Returns the last index of the specified character in the Cstring.

        Args:
            char (str): The character to find.

        Returns:
            int: The last index of the character, or -1 if not found.
        """
        pass
