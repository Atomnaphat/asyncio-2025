import time
import asyncio
from datetime import timedelta

# ค่าคงที่
speed = 1000
Judit_time = 5 / speed
Opponent_time = 55 / speed
opponents = 24
move_pairs = 30

async def game(x):
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        time.sleep(Judit_time)
        print(f"BOARD-{x}-{i+1} Judit made a move with {int(Judit_time*speed)} secs.")
        await asyncio.sleep(Opponent_time)
        print(f"BOARD-{x}-{i+1} Opponent made move with {int(Opponent_time*speed)} secs.")
    elapsed = (time.perf_counter() - board_start_time)*speed
    print(f"BOARD-{x} - >>>>>>>>>>>>> Finished move in {elapsed:.1f} secs.\n")
    return (x, elapsed)

async def main():
    tasks = [game(i) for i in range(opponents)]
    results = []
    for coro in asyncio.as_completed(tasks):
        board_num, elapsed = await coro
        results.append((board_num, elapsed))
    
    # หา board ที่เสร็จเร็วที่สุด
    fastest = min(results, key=lambda x: x[1])
    print(f"*** Board {fastest[0]} finished first in {fastest[1]:.1f} simulated seconds.")
    
    total_elapsed = time.perf_counter() - start_time
    print(f"\nBoard exhibition finished for {opponents} opponents in {timedelta(seconds=speed*round(total_elapsed))} hr.")


if __name__ == "__main__":
    print(f"Number of games: {opponents} games.")
    print(f"Number of move: {move_pairs} pairs.")
    start_time = time.perf_counter()
    asyncio.run(main())
    print(f"Finished in {round(time.perf_counter() - start_time)} real seconds.")
