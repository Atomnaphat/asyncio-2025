# all tasks
import asyncio

async def dummy():
    await asyncio.sleep(2)

async def main():
    t1 = asyncio.create_task(dummy(), name="Task A")
    t2 = asyncio.create_task(dummy(), name="Task B")
    await asyncio.sleep(0.1) # ให้ tasks ได้เริ่มทำงานก่อน

    all_tasks = asyncio.all_tasks() # ดึง tasks ทั้งหมดที่อยู่ใน Event Loop ปัจจุบัน
    print("Task ทั้งหมดใน loop:")
    for t in all_tasks:
        print("-", t.get_name()) # พิมพ์ชื่อของแต่ละ task

asyncio.run(main())