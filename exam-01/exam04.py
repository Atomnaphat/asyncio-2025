#
# ให้หาข้อผิดพลาดและแก้ไขโค้ดให้ทำงานถูกต้อง
# Result:
# Task A started
# Task B started
# Task A finished
# Task B finished
# All tasks done

import asyncio

async def task(name):
    print(f"Task {name} started")
    await asyncio.sleep(2)
    print(f"Task {name} finished")

async def main():
    task_a = asyncio.create_task(task("A"))
    task_b = asyncio.create_task(task("B"))
    await task_a
    await task_b
    print("All tasks done")

asyncio.run(main())

