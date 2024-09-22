from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
def get_html(url):
    with sync_playwright() as p:
        chrome = p.chromium
        browser = chrome.launch(headless= False)
        page = browser.new_page()
        page.goto(url)
        result = page.evaluate('() => window.scroll(0,document.body.scrollHeight)')
        # print(f'title of page is {result}')
        page.wait_for_timeout(2000)
        page.wait_for_load_state('networkidle')
        page.wait_for_load_state('domcontentloaded')
        # page.screenshot(path='flip.png')
        html_body = page.inner_html('body')
        parse_html = HTMLParser(html_body)
        return parse_html