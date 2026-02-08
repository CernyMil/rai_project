
# Meta AI Scraper

Generate randomized Meta AI image prompts and submit them through an automated browser session.

## What it does
- Builds prompts from curated attribute lists (age, gender, country, mood, expression, lighting, background, camera details)
- Opens Meta AI in Chromium and submits the generated prompt
- Downloads the resulting image to output_data

## Requirements
- Python 3.12+
- Playwright (Chromium)

## Install
Using uv (recommended):

```bash
pip install uv
uv sync
uv run -- playwright install --with-deps chromium
```
## Usage

Run a single prompt:
```bash
uv run meta-scraper
```
Run multiple prompts:
```bash
uv run meta-scraper 5
```
For the intended usage you have to be logged in Meta, otherwise you are not able to generate images. 
When you run this script for the first time and your session is not stored in state.json, you will be tasked to log in, there is a 60s timeout for it and you need to be in non-Headless mode.

When you are succesfully logged in, your sesssion is stored in state.json and you can turn on headless mode.

There is also Dockerfile available, however, it is currently not a recommened to use, because of log in problem. Playwright can't open browser in non-Headless mode, when running in container.

Build the image:
```bash
docker build -t meta-ai-scraper .
```
## Tests
Run tests:
```bash
uv run pytest
```