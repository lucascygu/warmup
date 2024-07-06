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
    (list of "char" (str in python with only one character)): A list of characters representing the string with a null character '\0' at the end.
    """
    def __init__(self, lst: list[str] = None):
        """
        Initializes the Cstring with an optional list of characters.

        Args:
            lst (list[str], optional): A list of characters to initialize the string.
                                       Defaults to None, which initializes an empty string.
        """
        self.lst = lst if lst is not None else []
        self.string = self.lst[:]
        self.string.append('\0')

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
        if index < 0 or index >= len(self.string):
            raise IndexError("Index is out of the valid range")
        return self.string[index]

    def nowstring(self) -> str:
        """
        Returns the Python string representation of the Cstring

        Returns:
            str: The string representation.
        """
        return ''.join(self.string[:-1])

    def newString(self) -> 'Cstring':
        """
        Creates a new copy of the current Cstring.

        Returns:
            Cstring: A new instance of Cstring with the same content.
        """
        new_string = Cstring(self.string[:-1])
        return new_string

    def append(self, char: str):
        """
        Appends a character to the end of the Cstring.

        Args:
            char (str): The character to append.
        """
        if len(char) != 1:
            raise ValueError("Only single characters can be appended")
        self.string.insert(len(self.string) - 1, char)

    def insert(self, index: int, char: str | list[str]):
        """
        Inserts a character or a list of characters at the specified index.

        Args:
            index (int): The index at which to insert the character(s).
            char (str | list[str]): The character or list of characters to insert.
        """
        if isinstance(char, list):
            if any(len(c) != 1 for c in char):
                raise ValueError("All elements in the list must be single characters")
            if index < 0 or index > len(self.string) - 1:
                raise IndexError("Index is out of the valid range")
            self.string = self.string[:index] + char + self.string[index:]
        elif isinstance(char, str):
            if len(char) != 1:
                raise ValueError("Only single characters can be inserted")
            if index < 0 or index > len(self.string) - 1:
                raise IndexError("Index is out of the valid range")
            self.string.insert(index, char)
        else:
            raise TypeError("char must be a str or list[str]")

    def pop(self, index: int = -1) -> str:
        """
        Removes and returns the character at the specified index.

        Args:
            index (int, optional): The index of the character to remove. Defaults to -1 (the last character).

        Returns:
            str: The removed character.
        """
        if len(self.string) <= 1 or index < -len(self.string) or index >= len(self.string) - 1:
            raise IndexError("Index is out of the valid range or null terminator cannot be removed")
        return self.string.pop(index)

    def replace(self, old: str, new: str):
        """
        Replaces all occurrences of a character with another character.

        Args:
            old (str): The character to be replaced.
            new (str): The character to replace with.
        """
        if not isinstance(old, str) or not isinstance(new, str):
            raise ValueError("Both 'old' and 'new' must be strings.")
        if len(old) != 1 or len(new) != 1:
            raise ValueError("Both 'old' and 'new' must be single characters.")
        self.string = [new if char == old else char for char in self.string[:-1]]
        self.string.append('\0')  # Ensure the null character is always at the end

    def strstr(self, substring: 'Cstring') -> int:
        """
        Finds the first occurrence of the substring in the Cstring.

        Args:
            substring (Cstring): The substring to find.

        Returns:
            int: The index of the first occurrence of the substring, or -1 if not found.
        """
        sub_str = substring.nowstring()
        main_str = self.nowstring()
        index = main_str.find(sub_str)
        return index if index != -1 else -1

    def empty(self) -> None:
        """
        Empties the Cstring.
        """
        self.string = ['\0']

    def strrchr(self, char: str) -> int:
        """
        Returns the last index of the specified character in the Cstring.

        Args:
            char (str): The character to find.

        Returns:
            int: The last index of the character, or -1 if not found.
        """
        for i in range(len(self.string) - 2, -1, -1):
            if self.string[i] == char:
                return i
        return -1
