import pytest

from prompt_generator import PromptGenerator  


TEST_PROMPT="A realistic selfie photo of a 58-year-old male person from Argentina, with mood miserable and expression of pained expression, lighting shade under trees, with background in an office, and additional camera details realistic photography style."

def test_prompt_generator():
    generator = PromptGenerator(seed=42)
    prompt = generator.generate()
    assert prompt == TEST_PROMPT