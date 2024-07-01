from Cstring import Cstring

class CSentence:
    """
    A class to represent a sentence composed of multiple Cstring objects,
    mimicking an array of strings to construct sentences.

    Attributes:
        string (list[Cstring]): A list of Cstring objects representing words in a sentence.
    """
    def __init__(self, cstrings: list[Cstring] = None):
        """
        Initializes the CSentence with an optional list of Cstring objects.

        Args:
            cstrings (list[Cstring], optional): A list of Cstring objects that make up the sentence.
                                                Defaults to None, which will initialize an empty sentence.
        """
        pass

    def get_sentence(self) -> str:
        """
        Constructs and returns the sentence as a concatenated string of words.

        Returns:
            str: The full sentence constructed from the Cstring objects,
                 where each word is separated by a space.
        """
        pass
