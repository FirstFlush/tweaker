
from typing import Iterable, Optional, Callable
from rapidfuzz import fuzz, process


class FuzzyMatcher:
    """
    Utility for fuzzy string matching and best-match lookup.
    """

    def __init__(self, scorer: Optional[Callable] = None):
        self.scorer = scorer or fuzz.WRatio

    def best_match(
            self, 
            query: str, 
            choices: Iterable[str],
            score_cutoff: float = 90.0
    ) -> tuple[str, float] | None:
        """
        Returns the best matching string from choices for the query,
        along with its score, if the score is above the cutoff.
        """
        result = process.extractOne(
            query,
            choices,
            scorer=self.scorer,
        )
        if result:
            match, score, _ = result
            return (match, score) if score >= score_cutoff else None

    def best_matches(
            self, 
            query: str, 
            choices: Iterable[str],
            limit: int = 5, 
            score_cutoff: float = 50.0
    ) -> list[tuple[str, float]]:
        """
        Returns up to `limit` matches from choices for the query,
        each with a similarity score above the cutoff.
        """
        results = process.extract(
            query,
            choices,
            scorer=self.scorer,
            limit=limit,
        )
        return [(choice, score) for (choice, score, _) in results if score >= score_cutoff]
