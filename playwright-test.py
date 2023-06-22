from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(locale="zh-tw")

    # Open new page
    page = context.new_page()

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Click form[name="f"] span span
    page.click("span.soutu-btn")
    with page.expect_file_chooser() as fc_info:
        page.click("input[type=\"file\"]")
    file_chooser = fc_info.value
    file_chooser.set_files("foo.png")

    # Upload 新建文本文档.txt
    page.wait_for_url("https://graph.baidu.com/**")

    page.click("span:has-text(\"设置\")")
    # Click text=换一换
    page.click("text=换一换")
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
