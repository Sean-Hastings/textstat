
from ..utils import typed_cache
from ..counts import count_chars, count_words

@typed_cache
def chars_per_word(text: str, ignore_spaces: bool = True) -> float:
    """Calculate the average word length in characters.

    This function is a combination of the functions `counts.count_chars` and
    `counts.count_words`.

    Parameters
    ----------
    text : str
        A text string.
    ignore_spaces : bool
        whether to include spaces in the character count

    Returns
    -------
    float
        The average number of characters per word.

    """
    try:
        return count_chars(text, ignore_spaces=ignore_spaces) / count_words(text)
    except ZeroDivisionError:
        return count_chars(text, ignore_spaces=ignore_spaces)
