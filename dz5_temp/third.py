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

responses = []
async def fetch_mult_urls(urls : list):
    for url in urls:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                print(f"connected to {session._base_url}")
                responses.append(await response.text())

async def main():
    urls = ["https://refactoring.guru/design-patterns/visitor","https://mail.google.com/mail/u/0/#inbox",
            "https://www.youtube.com/watch?v=_4QY1nGFRY8","https://github.com/Yladzislav/py_HW/tree/master/dz4"]
    await fetch_mult_urls(urls)
    print(responses, sep = '\n')

asyncio.run(main())
    
