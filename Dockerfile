FROM python:3.14-slim


WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml ./
COPY README.md ./
COPY src ./src
COPY input_data ./input_data
COPY output_data ./output_data

RUN uv sync
RUN uv run -- playwright install --with-deps chromium

ENTRYPOINT ["uv", "run", "--", "meta-scraper"]
CMD ["1"]
