from __future__ import annotations

import os

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError, sync_playwright

class MetaAIScraper:
    """Scrapes Meta AI by opening a browser, navigating to the site, and sending prompts."""
    def __init__(self, headless: bool = False, storage_state_path: str = "state.json") -> None:
        self.headless = headless
        self.storage_state_path = storage_state_path

    def run_prompt(self, prompt: str) -> None:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=self.headless)
            context = browser.new_context(
                storage_state=self.storage_state_path if os.path.exists(self.storage_state_path) else None
            )
            page = context.new_page()

            self._open_meta_ai(page)
            self._navigate_to_login_page(page)
            context.storage_state(path=self.storage_state_path)
            
            self._send_prompt(page, prompt)
            self._download_image(page)

            page.wait_for_timeout(60_000)
            browser.close()

    def _open_meta_ai(self, page: Page) -> None:
        """Opens the Meta AI homepage and waits for it to load."""
        page.goto("https://www.meta.ai/", wait_until="domcontentloaded")
        page.wait_for_timeout(5_000)
        

    def _navigate_to_login_page(self, page: Page) -> None:
        """Handles the initial navigation and login flow on Meta AI, if not already logged in."""
        if page.locator("text=Welcome to Meta AI").is_visible():
            page.click("text=Continue")    
            page.get_by_text("Year").click()
            page.get_by_text("1990").click()
            page.get_by_role("Button", name="Continue").click()
            page.get_by_role("Button", name="Log in").click()
            page.get_by_role("button", name="Decline optional cookies").click()
        
    
    def _send_prompt(self, page: Page, prompt: str) -> None:
        """Finds the prompt input area, types the prompt, and submits it."""
        textarea = page.locator("[data-testid='composer-input'][contenteditable='true']")
        textarea.wait_for(state="visible", timeout=60_000)
        textarea.click()
        page.keyboard.type(prompt, delay=20)
        page.keyboard.press("Enter")
            
    def _download_image(self, page: Page) -> None:
        """Waits for the download button to appear and clicks it to download the generated image."""
        download_selector = '[aria-label="Download"], [aria-label="Stáhnout"]'
        download_button = page.locator(download_selector).first
        try:
            download_button.wait_for(state="visible", timeout=60_000)
            download_button.scroll_into_view_if_needed()
            with page.expect_download(timeout=60_000) as download_info:
                download_button.click(force=True)
        except PlaywrightTimeoutError:
            page.locator('[aria-label="View media"], [aria-label="Zobrazit média"]').first.click(force=True)
            download_button.wait_for(state="visible", timeout=60_000)
            with page.expect_download(timeout=60_000) as download_info:
                download_button.click(force=True)
        download = download_info.value
        output_path = os.path.join("./output_data", download.suggested_filename)
        download.save_as(output_path)