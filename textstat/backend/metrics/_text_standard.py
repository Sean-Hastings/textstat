from __future__ import annotations

import math
from collections import Counter

from ..utils._typed_cache import typed_cache
from ._flesch_kincaid_grade import flesch_kincaid_grade
from ._flesch_reading_ease import flesch_reading_ease
from ._smog_index import smog_index
from ._coleman_liau_index import coleman_liau_index
from ._automated_readability_index import automated_readability_index
from ._dale_chall_readability_score import dale_chall_readability_score
from ._linsear_write_formula import linsear_write_formula
from ._gunning_fog import gunning_fog


@typed_cache
def text_standard(text: str, lang: str) -> float:
    grade: list[int] = []

    # Appending Flesch Kincaid Grade
    lower = math.floor(flesch_kincaid_grade(text, lang))
    upper = math.ceil(flesch_kincaid_grade(text, lang))
    grade.append(int(lower))
    grade.append(int(upper))

    # Appending Flesch Reading Easy
    score = flesch_reading_ease(text, lang)
    if score < 100 and score >= 90:
        grade.append(5)
    elif score < 90 and score >= 80:
        grade.append(6)
    elif score < 80 and score >= 70:
        grade.append(7)
    elif score < 70 and score >= 60:
        grade.append(8)
        grade.append(9)
    elif score < 60 and score >= 50:
        grade.append(10)
    elif score < 50 and score >= 40:
        grade.append(11)
    elif score < 40 and score >= 30:
        grade.append(12)
    else:
        grade.append(13)

    # Appending SMOG Index
    lower = math.floor(smog_index(text, lang))
    upper = math.ceil(smog_index(text, lang))
    grade.append(int(lower))
    grade.append(int(upper))

    # Appending Coleman_Liau_Index
    lower = math.floor(coleman_liau_index(text))
    upper = math.ceil(coleman_liau_index(text))
    grade.append(int(lower))
    grade.append(int(upper))

    # Appending Automated_Readability_Index
    lower = math.floor(automated_readability_index(text))
    upper = math.ceil(automated_readability_index(text))
    grade.append(int(lower))
    grade.append(int(upper))

    # Appending Dale_Chall_Readability_Score
    lower = math.floor(dale_chall_readability_score(text, lang))
    upper = math.ceil(dale_chall_readability_score(text, lang))
    grade.append(int(lower))
    grade.append(int(upper))

    # Appending Linsear_Write_Formula
    lower = math.floor(linsear_write_formula(text, lang))
    upper = math.ceil(linsear_write_formula(text, lang))
    grade.append(int(lower))
    grade.append(int(upper))

    # Appending Gunning Fog Index
    lower = math.floor(gunning_fog(text, lang))
    upper = math.ceil(gunning_fog(text, lang))
    grade.append(int(lower))
    grade.append(int(upper))

    # Finding the Readability Consensus based upon all the above tests
    d = Counter(grade)
    final_grade = d.most_common(1)
    return float(final_grade[0][0])
