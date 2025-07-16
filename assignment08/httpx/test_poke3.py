import asyncio
import httpx

async def fetch_pokemon_info(url):
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        
        # ดึงข้อมูลที่ต้องการ
        pokemon_name = data["name"].title()
        pokemon_id = data["id"]
        height = data["height"]
        weight = data["weight"]
        types = [t["type"]["name"] for t in data["types"]]

        return {
            "Name": pokemon_name,
            "ID": pokemon_id,
            "Height": height,
            "Weight": weight,
            "Types": types
        }

async def main():
    info = await fetch_pokemon_info("pikachu")
    print(f"Name: {info['Name']}")
    print(f"ID: {info['ID']}")
    print(f"Height: {info['Height']}")
    print(f"Weight: {info['Weight']}")
    print(f"Types: {', '.join(info['Types'])}")

asyncio.run(main())
