import asyncio
import httpx
import time

STUDENT_ID = "6410301001"  # เปลี่ยนเป็นรหัสนักศึกษาของคุณ
API_URL = f"http://127.0.0.1:8088/fire/{STUDENT_ID}"

async def launch_rocket(rocket_no, start_zero):
    start_time = time.perf_counter() - start_zero
    async with httpx.AsyncClient() as client:
        resp = await client.get(API_URL)
        data = resp.json()
        time_to_target = data["time_to_target"]
    end_time = time.perf_counter() - start_zero
    return {
        "rocket_no": rocket_no,
        "start_time": start_time,
        "time_to_target": time_to_target,
        "end_time": end_time
    }

async def main():
    print("Rocket prepare to launch ...")
    start_zero = time.perf_counter()
    tasks = [asyncio.create_task(launch_rocket(i+1, start_zero)) for i in range(3)]
    results = await asyncio.gather(*tasks)
    results.sort(key=lambda x: x["end_time"])
    print("Rockets fired:")
    for r in results:
        print(
            f"Rocket-{r['rocket_no']} | "
            f"start_time: {r['start_time']:.2f} sec | "
            f"time_to_target: {r['time_to_target']:.2f} sec | "
            f"end_time: {r['end_time']:.2f} sec"
        )
    total_time = max(r["end_time"] for r in results)
    print(f"\nTotal time for all rockets: {total_time:.2f} sec")

if __name__ == "__main__":
    asyncio.run(main())