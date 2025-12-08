from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        
    def navigate_to(self, url: str):
        """Navigate to a specific URL"""
        self.page.goto(url)
        
    def wait_for_element(self, selector: str, timeout: int = 5000):
        """Wait for element to be visible"""
        return self.page.wait_for_selector(selector, timeout=timeout)
        
    def click_element(self, selector: str):
        """Click an element"""
        self.page.click(selector)
        
    def is_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        return self.page.is_visible(selector)
        
    def wait_for_timeout(self, timeout: int):
        """Wait for specified timeout"""
        self.page.wait_for_timeout(timeout)
        
    def get_page_title(self) -> str:
        """Get page title"""
        return self.page.title()
        
    def take_screenshot(self, path: str):
        """Take screenshot"""
        self.page.screenshot(path=path)
