import argparse

from prompt_generator.prompt_generator import PromptGenerator
from meta_ai_scraper.meta_ai_scraper import MetaAIScraper

def main() -> None:
    parser = argparse.ArgumentParser(description="Run Meta AI prompt generation.")
    parser.add_argument(
        "count",
        type=int,
        nargs="?",
        default=1,
        help="Number of prompts to generate and submit.",
    )
    args = parser.parse_args()

    for _ in range(args.count):
        generator = PromptGenerator()
        prompt = generator.generate()
        print(prompt)

        client = MetaAIScraper(headless=False)
        client.run_prompt(prompt)


if __name__ == "__main__":
    main()
