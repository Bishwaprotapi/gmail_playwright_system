from playwright.sync_api import sync_playwright


def login():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        context = browser.new_context()

        page = context.new_page()

        page.goto("https://mail.google.com")

        input("Login complete then press ENTER...")

        context.storage_state(path="storage_state.json")

        browser.close()