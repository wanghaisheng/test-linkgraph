import asyncio
# import botright
import time
import os
import platform
from playwright.async_api import expect,async_playwright

STATUS_CONTAINER='.ant-row.ant-row-no-wrap.ant-row-space-between'
processing="Creating clusters takes up to 2 minutes"
finished="topic ideas found"

async def not_finished(page) -> bool:
    s = await page.locator(STATUS_CONTAINER).text_content()
    print('current text:',s)
    return s.find(finished) != -1
async def nologin():
    os_type = platform.system()
    
    async with async_playwright() as playwright:
        headless=True
        if os_type in ["Windows","Darwin"]:
            headless=False
        
        browser =  await playwright.chromium.launch(headless=headless)

        # botright_client = await botright.Botright(headless=True)
    

        # browser = await botright_client.new_browser()
        # Set up the SOCKS5 proxy configuration

        os_type = platform.system()

        proxy_server = {"server":'socks5://127.0.0.1:1080'} # Replace with your SOCKS5 proxy server details

        context = await browser.new_context(
            proxy=proxy_server,
            bypass_csp=True  # Optional: Add any other context options as needed
        )
        keyword = os.getenv('keyword')        
        page=None
        if os_type in ["Windows","Darwin"]:
            page = await context.new_page()
            keyword ="temu"

        else:
            page = await browser.new_page()
            
        # url="https://www.linkgraph.com/content-planner-tool/"
        # await page.goto(url)
        # visible = await page.get_by_role('keyword').is_visible()
        # await page.get_by_role('keyword').fill(keyword)
        # await page.locator('.display-flex > button:nth-child(2)').click()
        url = "https://dashboard.linkgraph.com/content/content-planner/public?keyword=" + keyword
        response =await page.goto(url)
        try:
        
            quota="#__next > div > div:nth-child(2) > div:nth-child(2) > div.sc-McAUB.dmSUED > div > div.sc-eZkcaX.kOaJEY"
            s = await page.locator(quota).text_content()

            if   "Your Content Ideas quota was consumed" in s:
            
            
                print('there is no left quota for this ip')

            else:
                await page.wait_for_url("https://dashboard.linkgraph.com/content/content-planner/public/**")
                start=0
                start_time = time.time()

                while True: 
                    done=await not_finished(page)
                    if done:
                        break
                    
                    print(f'Still preparing, waiting another{start}* 30 seconds')
                    time.sleep(30)
                    start=start+1
                    await page.reload()
                # End the timer
                end_time = time.time()

                # Calculate the running time
                running_time = end_time - start_time          
                print("Running Time:", running_time, "seconds")
                
                print('URL:',page.url)

                try:
                    sel='//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div'
                    # sel='ant-collapse-item ant-collapse-no-arrow'
                    clusters_locator = page.locator(sel)
                    print(await clusters_locator.text_content())

                    # sel="#__next > div > div > div:nth-child(2) > div:nth-child(2) > div.sc-fduepK.hAwtCS > div > div > div:nth-child(3) > div > div > div > div:nth-child(1)"
                    # clusters_locator = page.locator(sel)
                    # print(await clusters_locator.text_content())
                    if await clusters_locator.is_visible():
                        print('find All Clusters')
                        await clusters_locator.click()
                    else:
                        print('is_visible is failed')
                except:
                    print('xpath is failed')
            
                os.makedirs(".output", exist_ok=True)
                await page.screenshot(path="./output/1.png", full_page=True)
                view_cluster_sel='//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div'

                counts = await page.locator(view_cluster_sel).count()
                print('counts:', counts)
            
                for i in range(0,counts):   
                    # topic=await page.locator(view_cluster_sel).nth(i)
                    print(f'i{i}')
                    button='//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div['+i+1+']/div/button'
                    # //*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div/button/div
                    print(f'button:{button}')
                    view_cluster_button= page.locator(button)
                    if await view_cluster_button.is_visible():
                        print(f'find {i} button')
                    await view_cluster_button.click()
                    MONTHLY_SEARCH_VOLUME=await page.locator("//html/body/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]").text_content()
                    TOTAL_TRAFFIC=await page.locator("//html/body/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]").text_content()
                    RANKING_POTENTIAL=await page.locator("//html/body/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div").text_content()
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
            
                #       # Continue by using the Page
                # await botright_client.close()
                await browser.close()
        except:
            print('can not load quota check ',page.url)
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
