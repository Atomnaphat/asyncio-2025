import asyncio
import httpx

async def fetch_pokemon_info(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

        return {
            "name": data["name"].title(),
            "id": data["id"],
            "base_experience": data["base_experience"]
        }

def get_base_exp(pokemon):
    return pokemon["base_experience"]

async def main():
    names = [
        "pikachu", "bulbasaur", "charmander", "squirtle", "eevee",
        "snorlax", "gengar", "mewtwo", "psyduck", "jigglypuff"
    ]

    tasks = [fetch_pokemon_info(name) for name in names]
    results = await asyncio.gather(*tasks)

    results.sort(key=get_base_exp, reverse=True)

    for p in results:
        print(f"{p['name']} -> ID: {p['id']}, Base Experience: {p['base_experience']}")

asyncio.run(main())
