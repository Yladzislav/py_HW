"""
3) Создайте асинхронную функцию fetch_multiple_urls(urls), которая:
 - Делает конкурентные GET-запросы к списку URL (используйте aiohttp или httpx).
 - Возвращает ответы в том же порядке, что и URL. 

Пример:
urls = ["https://example.com", "https://google.com"]
results = await fetch_multiple_urls(urls)  # [response1, response2]
"""
import aiohttp
import asyncio

async def fetch_mult_urls(session, url):
        print(f"connection to {url}")
        async with session.get(url) as response:
            print(f"status : {response.status}")

async def main():
    urls = ["https://leetcode.com/",
            "https://mail.google.com",
            "https://www.youtube.com",
            "https://github.com"
            ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_mult_urls(session, url) for url in urls]
        await asyncio.gather(*tasks)
    # print(responses, sep = '\n')

asyncio.run(main())
    
