"""
1) Напишите асинхронную функцию fetch_url(url), которая:
 - Имитирует HTTP-запрос (используйте asyncio.sleep(1) вместо реального запроса).
 - Возвращает "данные" с URL (например, f"Data from {url}").

Запустите параллельно запросы к 5 разным URL и соберите результаты.

Ожидаемый результат:
Все запросы выполняются параллельно, общее время ~1 секунда (а не 5 секунд).
"""
import asyncio
import time

t1 = time.time()

async def fetch_url(url):
    await asyncio.sleep(1)
    print(time.time() - t1)
    return f"data from : {url}"

tasks : list = []
async def main():
    for x in range(0,5):
        tasks.append(asyncio.create_task(fetch_url(x)))
        print(time.time() - t1)
    res = await asyncio.gather(*tasks)
    print(*res, sep = '\n')

asyncio.run(main())