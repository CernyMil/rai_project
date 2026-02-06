from __future__ import annotations

from playwright.sync_api import Browser, Page, Playwright, sync_playwright


class MetaAIScraper:
    """Scrapes Meta AI by opening a browser, navigating to the site, and sending prompts."""
    def __init__(self, headless: bool = False) -> None:
        self.headless = headless

    def run_prompt(self, prompt: str) -> None:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=self.headless)
            page = browser.new_page()

            self._open_meta_ai(page)
            self._send_prompt(page, prompt)

            page.wait_for_timeout(30_000)
            browser.close()

    def _open_meta_ai(self, page: Page) -> None:
        page.goto("https://www.meta.ai/", wait_until="domcontentloaded")
        page.wait_for_timeout(5_000)

    def _send_prompt(self, page: Page, prompt: str) -> None:
        textarea = page.wait_for_selector("textarea", timeout=20_000)

        if textarea is not None:
            textarea.fill(prompt)
            textarea.press("Enter")