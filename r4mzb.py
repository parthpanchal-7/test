"""AI-style sample module with clear structure and helper functions."""

from typing import Dict, List, Tuple


def count_words(text: str) -> Dict[str, int]:
    """Return a word-frequency dictionary for normalized lowercase words."""
    frequencies: Dict[str, int] = {}
    for token in text.lower().split():
        frequencies[token] = frequencies.get(token, 0) + 1
    return frequencies


def top_n_words(text: str, n: int = 3) -> List[Tuple[str, int]]:
    """Return the top-N words sorted by frequency then alphabetically."""
    frequencies = count_words(text)
    ranked = sorted(frequencies.items(), key=lambda item: (-item[1], item[0]))
    return ranked[: max(n, 0)]


if __name__ == "__main__":
    sample = "AI tools can analyze code quality and code structure"
    print(top_n_words(sample, 3))
