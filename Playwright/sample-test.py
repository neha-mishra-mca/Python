from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://github.com/neha-mishra-mca/neha-mishra-mca")
    print(page.title())
    page.screenshot(path="github_page.png")
    browser.close()