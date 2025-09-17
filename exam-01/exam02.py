# Hint:
# แก้โค้ดให้สามารถรัน หลาย task พร้อมกัน ได้ถูกต้อง
# Result:
# Processing data
# Processing data
# Processing data
# Processing data
# Processing data

import asyncio

async def fetch_data():
    await asyncio.sleep(2)
    return "data"
async def process():
    await asyncio.sleep(2)
    data = await fetch_data()
    print("Processing", data)

async def main():
    # start many tasks
    started_tasks = [asyncio.create_task(process()) for _ in range(5)]
    # allow some of the tasks time to start
    await asyncio.sleep(0.1)
    for task in started_tasks:
        await task

asyncio.run(main())

