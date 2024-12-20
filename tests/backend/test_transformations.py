import pytest
import textstat.backend.transformations as transformations


@pytest.mark.parametrize(
    "in_text,out_text,rm_apostrophe",
    [
        ("They're here", "Theyre here", True),
        ("They're here", "They're here", False),
        ("They're here, and they're there.", "Theyre here and theyre there", True),
        ("They're here, and they're there.", "They're here and they're there", False),
        (
            "Who's there?I have no time for this... nonsense...my guy! a who's-who, veritably.",
            "Whos thereI have no time for this nonsensemy guy a whoswho veritably",
            True,
        ),
    ],
)
def test_remove_punctuation(in_text: str, out_text: str, rm_apostrophe: bool) -> None:
    assert (
        transformations.remove_punctuation(in_text, rm_apostrophe=rm_apostrophe)
        == out_text
    )