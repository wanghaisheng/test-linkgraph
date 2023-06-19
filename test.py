import asyncio

import botright


async def main():
    botright_client = await botright.Botright(headless=True)
    browser = await botright_client.new_browser()
    page = await browser.new_page()
    url="https://dashboard.linkgraph.com/content/content-planner/3946af54-e8f1-4f9b-b72f-5b79e6bc5e0e"
    await page.goto(url)

      
    await page.locator("/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[3]/div[1]/div/div/div[1]/svg").click()
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

    await botright_client.close()

if __name__ == "__main__":
    asyncio.run(main())
