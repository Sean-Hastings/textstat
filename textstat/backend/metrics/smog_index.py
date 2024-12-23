
from ..utils import typed_cache
from ..counts import count_sentences, count_polysyllable_words

@typed_cache
def smog_index(text: str, lang: str) -> float:
    r"""Calculate the SMOG index.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The SMOG index for `text`.

    Notes
    -----
    The SMOG index is calculated as:

    .. math::

        (1.043*(30*(n\ polysyllabic\ words/n\ sentences))^{.5})+3.1291

    Polysyllabic words are defined as words with more than 3 syllables.
    """
    sentences = count_sentences(text)

    # TODO: why this?
    if sentences < 3:
        return 0.0

    poly_syllab = count_polysyllable_words(text, lang)
    try:
        return (1.043 * (30 * (poly_syllab / sentences)) ** 0.5) + 3.1291
    except ZeroDivisionError:
        return 0.0
