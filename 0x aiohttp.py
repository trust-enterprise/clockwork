import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        data = await response.json()
        return data[:5]

async def main():
    async with aiohttp.ClientSession() as session:
        task = fetch(session, "https://api.github.com/users")
        results = await asyncio.gather(task)

        for users in results:
            print(len(users))
            for user in users:
                print(user['login'])

asyncio.run(main())