from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ._count_syllables import count_syllables
from ..selections._list_words import list_words


@typed_cache
def count_monosyllable_words(text: str, lang: str) -> int:
    """counts monosyllable words"""
    return len([w for w in list_words(text) if count_syllables(w, lang) == 1])
