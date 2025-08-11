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

t = time.time()
def call(timer):
    async def wrapper(seconds):
        await timer(seconds)
        print(f"wrapper executed in {time.time() - t} seconds from start of the programm")
    print(f"call has been made in {time.time() - t} seconds from start of the programm")
    return wrapper

@call
async def set_async_timer(seconds):
    await asyncio.sleep(seconds)

asyncio.run(set_async_timer(int(input("await seconds : "))))

