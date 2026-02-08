from src.prompt_generator.prompt_generator import PromptGenerator 


TEST_PROMPT="A realistic selfie photo of a 58-year-old male person from Argentina, with miserable mood and pained expression expression, shade under trees lighting, with in an office background, and additional camera details: realistic photography style."

def test_prompt_generator():
    generator: PromptGenerator = PromptGenerator(seed=42)
    prompt = generator.generate()
    assert prompt == TEST_PROMPT