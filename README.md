# Meta AI Scraper

Generate randomized Meta AI image prompts and submit them through an automated browser session.

## What it does
- Builds prompts from curated attribute lists (age, gender, country, mood, expression, lighting, background, camera details)
- Opens Meta AI in Chromium and submits the generated prompt
- Downloads the resulting image to [output_data](output_data)

## Requirements
- Python 3.12+
- Playwright (Chromium)

## Install
Using uv (recommended):

```bash
pip install uv
uv sync
uv run -- playwright install --with-deps chromium

