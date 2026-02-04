import logging

import prompt_generator

def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.NOTSET)
    for _ in range(10):
        generator = prompt_generator.PromptGenerator()
        prompt = generator.generate()
        print(prompt)


if __name__ == "__main__":
    main()
