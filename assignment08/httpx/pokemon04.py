import asyncio
import httpx

# ฟังก์ชันดึงข้อมูลโปเกมอนตัวเดียว
async def fetch_pokemon_info(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        
        pokemon_name = data["name"].title()
        pokemon_id = data["id"]
        types = [t["type"]["name"] for t in data["types"]]

        return {
            "Name": pokemon_name,
            "ID": pokemon_id,
            "Types": types
        }

async def main():
    urls = [
        "https://pokeapi.co/api/v2/pokemon/pikachu",
        "https://pokeapi.co/api/v2/pokemon/bulbasaur",
        "https://pokeapi.co/api/v2/pokemon/charmander",
        "https://pokeapi.co/api/v2/pokemon/squirtle",
        "https://pokeapi.co/api/v2/pokemon/eevee",
        "https://pokeapi.co/api/v2/pokemon/snorlax",
        "https://pokeapi.co/api/v2/pokemon/gengar",
        "https://pokeapi.co/api/v2/pokemon/mewtwo",
        "https://pokeapi.co/api/v2/pokemon/psyduck",
        "https://pokeapi.co/api/v2/pokemon/jigglypuff"
    ]

    # เรียก fetch_pokemon_info พร้อมกันหลายๆ URL
    tasks = [fetch_pokemon_info(url) for url in urls]
    results = await asyncio.gather(*tasks)

    # แสดงผลข้อมูลโปเกมอนแต่ละตัว
    for info in results:
        print(f"{info['Name']} -> ID: {info['ID']}, Types: {info['Types']}")

asyncio.run(main())
