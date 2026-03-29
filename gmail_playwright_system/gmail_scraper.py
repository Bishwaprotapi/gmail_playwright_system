from playwright.sync_api import sync_playwright
from database import insert_email


def scrape_gmail():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
            storage_state="storage_state.json"
        )

        page = context.new_page()

        page.goto("https://mail.google.com/mail/u/0/#inbox")

        page.wait_for_selector("tr.zA")

        emails = page.query_selector_all("tr.zA")

        for email in emails[:10]:

            sender_el = email.query_selector(".yP")
            subject_el = email.query_selector(".bog")
            time_el = email.query_selector(".xW span")

            if sender_el and subject_el and time_el:

                sender = sender_el.inner_text()
                subject = subject_el.inner_text()
                time = time_el.get_attribute("title")

                insert_email(sender, subject, time)

                print(sender, subject)

        browser.close()