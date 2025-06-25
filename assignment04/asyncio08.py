# get Exception
import asyncio

async def error_task():
    await asyncio.sleep(1)
    raise ValueError("เกิดข้อผิดพลาด")

async def main():
    task = asyncio.create_task(error_task())
    try:
        await task
    except Exception: # สามารถระบุเป็น ValueError ได้ ถ้าต้องการจับเฉพาะเจาะจง
        print("Exception ที่เกิด:", task.exception())

asyncio.run(main())