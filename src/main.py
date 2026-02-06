from prompt_generator import PromptGenerator
from meta_ai_scraper import MetaAIScraper

def main():
    #for _ in range(10):
    generator = PromptGenerator(seed=42)
    prompt = generator.generate()
    print(prompt)
    print("Sending prompt to Meta AI:")

    client = MetaAIScraper(headless=False)
    client.run_prompt(prompt)


if __name__ == "__main__":
    main()
