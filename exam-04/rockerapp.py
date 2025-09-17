from fastapi import FastAPI, HTTPException
import asyncio
import random

app = FastAPI(title="Asynchronous Rocket Launcher")

async def launch_rocket(student_id: str, eta: float):
    print(f"Rocket {student_id} launched! ETA: {eta:.2f} seconds")
    await asyncio.sleep(eta)
    print(f"Rocket {student_id} reached destination after {eta:.2f} seconds")

@app.get("/fire/{student_id}")
async def fire_rocket(student_id: str):
    # ตรวจสอบ student_id ต้องเป็น 10 หลัก
    if len(student_id) != 10 or not student_id.isdigit():
        raise HTTPException(status_code=400, detail="student_id must be 10 digits")
    # สุ่มเวลาจรวด
    eta = round(random.uniform(1, 2), 2)
    # สร้าง background task
    asyncio.create_task(launch_rocket(student_id, eta))
    # ส่ง response กลับทันที
    return {
        "message": f"Rocket {student_id} fired!",
        "time_to_target": eta
    }