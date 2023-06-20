import asyncio

import botright
import time 
import os

import re
from playwright.async_api import expect

async def nologin():
    botright_client = await botright.Botright(headless=True)

    browser = await botright_client.new_browser()
    page = await browser.new_page()

    # url="https://www.linkgraph.com/content-planner-tool/"
    # await page.goto(url)
    # visible = await page.get_by_role('keyword').is_visible()
    # await await page.get_by_role('keyword').fill(keyword)
    # await await page.locator('.display-flex > button:nth-child(2)').click()
    keyword=os.getenv('keyword')
   
    url="https://dashboard.linkgraph.com/content/content-planner/public?keyword="+keyword
    await page.goto(url)

    time.sleep(120)
    # print(await page.content())
    locator = page.locator('button.ant-btn.ant-btn-default.sc-bczRLJ.gtzvtM')
    print(await locator.text_content())
    await expect(locator).to_have_text("Export")
    # /html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div[1]/div/div/div[1]/svg
    # await page.get_by_role("button", name="All Clusters").click()

    # counts=await page.get_by_role("button", name="View Cluster").count()
    await page.screenshot(path="1.png", full_page=True)
 
    # counts= await page.locator("div.sc-jMFEJM.eaxCEo > div > div > div.ant-collapse-item.ant-collapse-item-active.ant-collapse-no-arrow > div.ant-collapse-content.ant-collapse-content-active > div > div > div").count()
    # print('coubts',counts)
    # for i in range(0,counts):   
    #     topic=await page.get_by_role("button", name="View Cluster").nth(i)
    #     print(f'i{i}')
        
    #     await topic.click()
    #     MONTHLY_SEARCH_VOLUME=await page.locator("div.sc-jNxMLV:nth-child(1)").text_content()
    #     TOTAL_TRAFFIC=await page.locator("div.sc-jNxMLV:nth-child(2)").text_content()
    #     RANKING_POTENTIAL=await page.locator("div.sc-jNxMLV:nth-child(3)").text_content()
    #     row_counts=await page.locator("tr.ant-table-row:nth-child").count()
    #     print(f'MONTHLY_SEARCH_VOLUME{MONTHLY_SEARCH_VOLUME}')
    #     print(f'TOTAL_TRAFFIC-{TOTAL_TRAFFIC}')
    #     print(f'RANKING_POTENTIAL-{RANKING_POTENTIAL}')
    #     print(f'row_counts-{row_counts}')

    #     for i in range(0,row_counts):
    #       KEYWORDS_IN_CLUSTER =await page.locator("td.ant-table-cell").nth(1)
    #       MSV =await page.locator("td.ant-table-cell").nth(2)
    #       CPC =await page.locator("td.ant-table-cell").nth(3)
    #       print(f'KEYWORDS_IN_CLUSTER-{KEYWORDS_IN_CLUSTER}')
    #       print(f'MSV-{MSV}')
    #       print(f'CPC-{CPC}')

    #       # Continue by using the Page
    await botright_client.close()

async def main():
    botright_client = await botright.Botright(headless=True)

    browser = await botright_client.new_browser()
    page = await browser.new_page()
    loginURL="https://dashboard.linkgraph.com/login"
    await page.goto(loginURL)
    username=os.getenv('username')
    password=os.getenv('password')
    keyword=os.getenv('keyword')

    await page.get_by_placeholder('email@example.com').fill(username)
    await page.get_by_placeholder('Password').fill(password)
    await page.locator('.ant-form > div:nth-child(7)').click()

    url="https://dashboard.linkgraph.com/content/content-planner"
    await page.goto(url)
    visible = await page.get_by_placeholder('Enter a keyword like "Garden Tools"').is_visible()
    await page.get_by_placeholder('Enter a keyword like "Garden Tools"').fill(keyword)
    time.sleep(120)
    locator = page.locator('tr.ant-table-row:nth-child(1) > td:nth-child(4) > div:nth-child(1) > button:nth-child(1) > span:nth-child(1)')
    await expect(locator).to_contain_text("View Topics")
    await locator.click()

    await page.locator("//html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[3]/div[1]/div/div/div[1]/svg").click()
    counts=await page.get_by_label("View Cluster").count()
    for i in range(0,counts):   
        topic=await page.get_by_label("View Cluster").nth(i)
        await topic.click()
        MONTHLY_SEARCH_VOLUME=await page.locator("div.sc-jNxMLV:nth-child(1)").text_content()
        TOTAL_TRAFFIC=await page.locator("div.sc-jNxMLV:nth-child(2)").text_content()
        RANKING_POTENTIAL=await page.locator("div.sc-jNxMLV:nth-child(3)").text_content()
        row_counts=await page.locator("tr.ant-table-row:nth-child").count()
        print(f'MONTHLY_SEARCH_VOLUME{MONTHLY_SEARCH_VOLUME}')
        print(f'TOTAL_TRAFFIC-{TOTAL_TRAFFIC}')
        print(f'RANKING_POTENTIAL-{RANKING_POTENTIAL}')
        print(f'row_counts-{row_counts}')

        for i in range(0,row_counts):
          KEYWORDS_IN_CLUSTER =await page.locator("td.ant-table-cell").nth(1)
          MSV =await page.locator("td.ant-table-cell").nth(2)
          CPC =await page.locator("td.ant-table-cell").nth(3)
          print(f'KEYWORDS_IN_CLUSTER-{KEYWORDS_IN_CLUSTER}')
          print(f'MSV-{MSV}')
          print(f'CPC-{CPC}')

          # Continue by using the Page
    await page.goto(url)
    visible=    await page.get_by_role("button", name="View Topics").is_visible()
    await page.get_by_label("more").click()
    # await page.locator(".ant-dropdown-menu-title-content > span:nth-child(1)").click()
    await botright_client.close()

if __name__ == "__main__":
    asyncio.run(nologin())
