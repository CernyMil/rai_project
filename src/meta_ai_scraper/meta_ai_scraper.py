from __future__ import annotations

from playwright.sync_api import Page, sync_playwright

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

            page.wait_for_timeout(60_000)
            browser.close()

    def _open_meta_ai(self, page: Page) -> None:
        page.goto("https://www.meta.ai/", wait_until="domcontentloaded")
        page.wait_for_timeout(5_000)
        if page.locator("text=Welcome to Meta AI").is_visible():
            page.click("text=Continue")    
        page.get_by_text("Year").click()
        page.get_by_text("1990").click()
        page.get_by_role("Button", name="Continue").click()
        page.locator("//span[normalize-space()='Create' and not(@dir)]").click()
        page.get_by_role("Button", name="Log in").click()
        page.get_by_role("button", name="Decline optional cookies").click()
        page.wait_for_timeout(60_000) #timewout for user login

    def _send_prompt(self, page: Page, prompt: str) -> None:
        textarea = page.get_by_role("textbox", name="Describe your image...")

        if textarea is not None:
            textarea.fill(prompt)
            textarea.press("Enter")
        