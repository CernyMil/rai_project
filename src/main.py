from prompt_generator.prompt_generator import PromptGenerator
from meta_ai_scraper.meta_ai_scraper import MetaAIScraper

def main():
    #for _ in range(10):
    generator = PromptGenerator()
    prompt = generator.generate()
    print(prompt)

    client = MetaAIScraper()
    client.run_prompt(prompt)


if __name__ == "__main__":
    main()
