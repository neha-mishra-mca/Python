import pytest
from playwright.sync_api import sync_playwright
from pages.map_component import MapComponent

@pytest.fixture(scope="session")
def browser():
    """Browser fixture for all tests"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True for headless
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """Page fixture for each test"""
    context = browser.new_context(
        viewport={'width': 1280, 'height': 720},
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    )
    page = context.new_page()
    
    # Navigate to base URL
    page.goto("https://gruppenplatz.healthycloud.de/HC_GP_Public_Pages/")
    
    yield page
    
    context.close()

@pytest.fixture
def search_component(page):
    """Search component fixture"""
    return SearchComponent(page)

@pytest.fixture
def map_component(page):
    """Map component fixture"""
    return MapComponent(page)
