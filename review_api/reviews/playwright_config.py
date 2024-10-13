import os
from playwright.sync_api import sync_playwright

PLAYWRIGHT_BROWSER_TYPE = 'chromium'
PLAYWRIGHT_LAUNCH_OPTIONS = {
    'headless': True,
    'args': ['--disable-gpu', '--window-size=1920,1080']
}

def get_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(**PLAYWRIGHT_LAUNCH_OPTIONS)
        return browser