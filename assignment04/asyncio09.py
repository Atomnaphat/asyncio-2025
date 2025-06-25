# cancel task
import asyncio

async def slow_task():
    await asyncio.sleep(3)

async def main():
    task = asyncio.create_task(slow_task())
    print("ยกเลิก task ใน 1 วิ")
    await asyncio.sleep(1) # รอ 1 วินาที
    task.cancel() # สั่งยกเลิก task
    try:
        await task # พยายามรอ task ที่ถูกยกเลิก
    except asyncio.CancelledError:
        print("Task ถูก cancel แล้ว")

asyncio.run(main())