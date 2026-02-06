from __future__ import annotations

import random
from typing import List, Optional

from loader import load_list


class PromptGenerator:
    """Generates random prompts for Meta AI based on predefined lists of attributes."""
    def __init__(self, seed: Optional[int] = None) -> None:
        self._rng: random.Random = random.Random(seed)

        self.ages: List[int] = list(range(18, 70))
        self.genders: List[str] = load_list("genders.json", str)
        self.countries: List[str] = load_list("countries.json", str)
        self.moods: List[str] = load_list("moods.json", str)
        self.expressions: List[str] = load_list("expressions.json", str)
        self.lighting: List[str] = load_list("lighting.json", str)
        self.backgrounds: List[str] = load_list("backgrounds.json", str)
        self.camera_details: List[str] = load_list("camera_details.json", str)

    def generate(self) -> str:
        age: int = self._rng.choice(self.ages)
        gender: str = self._rng.choice(self.genders)
        country: str = self._rng.choice(self.countries)
        mood: str = self._rng.choice(self.moods)
        expresion: str = self._rng.choice(self.expressions)
        lighting: str = self._rng.choice(self.lighting)
        background: str = self._rng.choice(self.backgrounds)
        camera_detail: str = self._rng.choice(self.camera_details)
        
        return (
            f"A realistic selfie photo of a {age}-year-old {gender} person from {country}, "
            f"with mood {mood} and expression of {expresion}, "
            f"lighting {lighting}, "
            f"with background {background}, "
            f"and additional camera details {camera_detail}."
        )
