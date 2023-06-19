import asyncio

import botright



#     context = browser.new_context(base_url="https://api.github.com")
#     api_request_context = context.request
#     page = context.new_page()

#     # Alternatively you can create a APIRequestContext manually without having a browser context attached:
#     # api_request_context = p.request.new_context(base_url="https://api.github.com")


#     # Create a repository.
#     response = api_request_context.post(
#         "/user/repos",
#         headers={
#             "Accept": "application/vnd.github.v3+json",
#             # Add GitHub personal access token.
#             "Authorization": f"token {API_TOKEN}",
#         },
#         data={"name": REPO},
#     )
async def main():
    token="Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoic2xpZGluZyIsImV4cCI6MTcwMjczMTkyMCwianRpIjoiZjNlNGE2MmIwODU0NDk2NTllZjNjZDA2NWJhODU4NWMiLCJyZWZyZXNoX2V4cCI6MTcwMjczMTkyMCwidXNlcl9pZCI6MTc5NTQzLCJjdXN0b21lciI6eyJpZCI6NjMxNzcsImVtYWlsIjoid2hzODYwNjAzQGdtYWlsLmNvbSIsInRlYW1faWRzIjpbXSwiaXNfc3Vic2NyaWJlciI6dHJ1ZSwicXVvdGEiOnsiY2EiOnsiYWxsb3dlZF9wYWdlcyI6MCwiYWxsb3dlZF9vbnBhZ2VfYXVkaXRzIjoyLCJhbGxvd2VkX2ZvY3VzX3Rlcm1zIjo2LCJhbGxvd2VkX3NpdGVfYXVkaXRvcl9wcm9qZWN0cyI6MiwiYWxsb3dlZF9zaXRlX2F1ZGl0b3JfcGFnZXMiOjEwMDAsImNyYXdsZWRfcGFnZXNfYWxsb3dlZF9wZXJfbW9udGgiOjEwMDAsImFsbG93ZWRfYWlfY29udGVudF9nZW5lcmF0aW9uIjozMCwiYWxsb3dlZF9vdHRvX3Byb2plY3RzIjoyfSwiZ3NjIjp7ImFsbG93ZWRfYWN0aXZlX3Byb2plY3RzIjo1LCJhbGxvd2VkX3NpdGVfa2V5d29yZHMiOjUsImFsbG93ZWRfcGFnZXMiOjUsImhpc3RvcmljYWxfbGltaXQiOiI2IG1vbnRocyIsInByb2plY3RfZGVhY3RpdmF0aW9uc19hbGxvd2VkX3Blcl9tb250aCI6NX0sImJsIjp7InVzZV9kZW1vIjp0cnVlLCJidWRnZXQiOjEwLCJtYXhfY29tcGV0aXRvcnNfcGVyX3Byb2plY3QiOjEwLCJtYXhfbnVtYmVyX29mX3Byb2plY3RzIjoxMCwiYWxsb3dlZF9iYWNrbGlua19yZXNlYXJjaGVzIjo1MDAwfSwia2UiOnsibWF4X2tleXdvcmRfbG9va3VwcyI6MTAsIm1heF9rZXl3b3JkX2xvb2t1cHNfcGVyX3dlZWsiOjEwLCJhbGxvd2VkX2NvbXBldGl0b3JfcmVzZWFyY2hlcyI6MTUwMCwiYWxsb3dlZF90cmFja2VkX2tleXdvcmRzIjoyMCwiYWxsb3dlZF90cmFja2VkX3Byb2plY3RzIjo1LCJhbGxvd2VkX2NvbnRlbnRfcGxhbnMiOjIsImFsbG93ZWRfY29tcGV0aXRvcl9yZXNlYXJjaF9wcm9qZWN0cyI6NSwiYWxsb3dlZF9sb2NhbF9zZXJwc19oZWF0bWFwX3NlYXJjaGVzIjoxMDB9LCJwc2kiOnsiYWxsb3dlZF9wc2lfcGFnZXMiOjV9LCJidWxrIjp7ImRhX2NoZWNrZXJfbWF4X2xvb2t1cHNfcGVyX2RheSI6MX0sInFwIjp7ImFsbG93ZWRfaGFyb19yZXBsaWVzIjoyfSwiZXhwaXJlc19hdCI6IjIwMjMtMDctMTYgMDI6MTI6MTcifSwicGxhbiI6IkZyZWUiLCJzZWF0cyI6MSwidHJpYWxfZXhwaXJlc19hdCI6bnVsbCwidGltZXpvbmUiOm51bGwsImlzX3doaXRlbGFiZWwiOm51bGwsIndoaXRlbGFiZWxfZG9tYWluIjpudWxsLCJpc192ZW5kYXN0YV9jbGllbnQiOmZhbHNlLCJwaG9uZV9udW1iZXIiOm51bGwsImNvbXBhbnlfbmFtZSI6Ilx1ODk3Zlx1NTMxN1x1NzM4Ylx1NmQ3N1x1NzUxZiIsImxvZ28iOiJodHRwczovL3N0b3JhZ2UuZ29vZ2xlYXBpcy5jb20vbGlua2dyYXBoLWN1c3RvbWVyLWxvZ28vTG9nb19TVkcuc3ZnP1gtR29vZy1BbGdvcml0aG09R09PRzQtUlNBLVNIQTI1NiZYLUdvb2ctQ3JlZGVudGlhbD1nY3MtZnVsbC1hY2Nlc3MlNDBvcmdhbmljLXJ1bGVyLTIwNzEyMy5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSUyRjIwMjMwNjE5JTJGYXV0byUyRnN0b3JhZ2UlMkZnb29nNF9yZXF1ZXN0JlgtR29vZy1EYXRlPTIwMjMwNjE5VDEzMDUyMFomWC1Hb29nLUV4cGlyZXM9ODY0MDAmWC1Hb29nLVNpZ25lZEhlYWRlcnM9aG9zdCZYLUdvb2ctU2lnbmF0dXJlPTQ0NDE0YzU5ZmM1NjdjZmNhOGVlMTE2MTNhMDZlYjJiOTQ2ZjNiZjJlMjljZDNlYjUyZmEwZDU0N2E1N2E5MDZlN2U5YmFhMzhhNWFlMmYyZjdjODQ2YzdkODljZjY4MzYxZjQ5NjBlMWIwMGJmNjdlZDZjYTNkNjI2ZDcwYjQyNWM5MjU2YzBmYWMwYzU4ZjExYTUxNTllMjdlY2RmOWNhZjZmNGZmNTdiOTQ3N2QwMjBkMGRkYzc2ZTgxMGFhZThmYWFhNTY5ZmNjNzZlYjQ4MjE1Y2UyYzRlNDFiNDQwY2M5ZWI3NmJjZTc0YWVhNTkyYjkyMDQwMzdhMDdiZGM3YTc2N2VkMmRkZDBiYTFlMzY1YmVmYjBjM2U1ODI4MTZhYTBkNzZkYzE1NjNlZDVjMmM3Y2ViYjMwNzQ5NTZhM2ZhNzc1NmE1MWI4MWU3ZjU2NDcwMmY4YzBiMDI3ZWIwMDEzNTAyMmUxNmU0NmY3MGU3YWNlOGRhZmQ3MTg0ZDE5OWRiODQ0MGZiZTQxY2VkYjM4YTBlYWU0NWMxYzEwYTdjNmRhYjMxZTM1MjM5NzJjYzQyNDQ0MTQzNzc0OTUwNGY1YzE0ZTFjMTFmMjdmYjhkMTJiNmJlMGEzZDM5NWFiOGQ1NzcwMTIzZmI3NGY0Y2Q5NzhmMGI2N2YxYmNlIiwic2hvdWxkX2NoaWxkcmVuX3JlY2VpdmVfZW1haWxzIjp0cnVlfX0.YSQG95D-E1DVhGq6Vy7sNoQU_WmM_M-hUFV2IRVr0Vs"
    botright_client = await botright.Botright(headless=True)

    botright_client.add_init_script("""(storage => {
      if (window.location.hostname === 'example.com') {
        const entries = JSON.parse(storage)
        for (const [key, value] of Object.entries(entries)) {
          window.token.setItem(key, value)
        }
      }
    })('""" + token + "')")    
    browser = await botright_client.new_browser()
    page = await browser.new_page()
    url="https://dashboard.linkgraph.com/content/content-planner/3946af54-e8f1-4f9b-b72f-5b79e6bc5e0e"
    await page.goto(url)
    visible = await page.get_by_role("Highest reward with least effort").is_visible()
      
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

    await botright_client.close()

if __name__ == "__main__":
    asyncio.run(main())
