"""
2) Напишите асинхронную функцию set_async_timer(seconds, callback), которая:
 - Ждёт указанное количество секунд (asyncio.sleep).
 - Вызывает callback функцию после завершения таймера.

Пример:
async def on_timer_end():
    print("Таймер сработал!")

await set_async_timer(2, on_timer_end)  # Через 2 секунды: "Таймер сработал!"
"""

import time
import asyncio

tasks = []
def call(timer):
    t = time.time()
    async def wrapper(seconds):
        t = time.time()
        for s in seconds:
            tasks.append(asyncio.create_task(timer(s)))
            #print(f"wrapper took {time.time() - t} seconds to execute")
        await asyncio.gather(*tasks)
    #print(f"call has been made in {time.time() - t} seconds from start of the programm")
    return wrapper

@call
async def set_async_timer(seconds):
    await asyncio.sleep(seconds)
    print(f"seconds took {seconds}")

seconds_list = list(map(int, input("await seconds : ").split(' ')))
asyncio.run(set_async_timer(seconds_list))

