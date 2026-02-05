import prompt_generator

def main():
    for _ in range(10):
        generator = prompt_generator.PromptGenerator(seed=42)
        prompt = generator.generate()
        print(prompt)


if __name__ == "__main__":
    main()
