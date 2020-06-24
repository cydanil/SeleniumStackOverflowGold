import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")  # noqa
    driver.find_element_by_id("email").send_keys(EMAIL)
    driver.find_element_by_id("password").send_keys(PASSWORD)
    driver.find_element_by_id("submit-button").click()

    # That should be it, but let's check that the count is up
    driver.find_element_by_class_name("my-profile").click()

    page = driver.find_element_by_xpath("//*[contains(.,'/100')]")
    # There, it gets ugly, parse the content of the page to find the value
    # no regex. We're looking for a string like this: \n{days_count}/100
    count_end = page.text.find('/100')
    last_line_break = page.text[:count_end].rfind('\n')

    val = int(page.text[last_line_break:count_end])

    print(val)
