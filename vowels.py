def count_vowels(s: str) -> int:
    """Подсчитывает количество гласных букв в строке."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)