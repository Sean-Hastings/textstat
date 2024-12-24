from __future__ import annotations

import pytest
from textstat import textstat
from ..backend import resources


@pytest.mark.parametrize(
    "text, float_output, expected",
    [
        (resources.EMPTY_STR, True, 0.0),
        (resources.EMPTY_STR, False, "0th and 1st grade"),
        (resources.EASY_TEXT, True, 4.0),
        (resources.EASY_TEXT, False, "4th and 5th grade"),
        (resources.SHORT_TEXT, True, 2.0),
        (resources.SHORT_TEXT, False, "2nd and 3rd grade"),
        (resources.PUNCT_TEXT, True, 6.0),
        (resources.PUNCT_TEXT, False, "6th and 7th grade"),
        (resources.LONG_TEXT, True, 9.0),
        (resources.LONG_TEXT, False, "9th and 10th grade"),
    ],
)
def test_text_standard(text: str, float_output: bool, expected: float | str) -> None:
    ts = type(textstat)()
    assert ts.text_standard(text, float_output) == expected