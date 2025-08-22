import pytest
from vowels import count_vowels

def test_only_vowels():
    # Строка, содержащая только гласные
    input_str = "aeiouAEIOU"
    expected_count = 10
    assert count_vowels(input_str) == expected_count

def test_no_vowels():
    # Строка без гласных
    input_str = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    expected_count = 0
    assert count_vowels(input_str) == expected_count

def test_mixed_case():
    # Строка с разными регистрами и смешанными символами
    input_str = "AbcDeFghiJklmNoPqRsTuVwXyZ"
    # Гласные: A, e, i, o, u (в разном регистре)
    expected_count = 5
    assert count_vowels(input_str) == expected_count