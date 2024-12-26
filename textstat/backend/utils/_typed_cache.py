from __future__ import annotations

from functools import lru_cache
from typing import Callable

from .constants import CACHE_SIZE, T, P


def typed_cache(func: Callable[P, T]) -> Callable[P, T]:
    """Decorator to cache function results without losing type info.

    Parameters
    ----------
    func : Callable
        The function to cache.

    Returns
    -------
    Callable
        The cache-wrapped function.

    """
    return lru_cache(maxsize=CACHE_SIZE)(func)  # type: ignore
