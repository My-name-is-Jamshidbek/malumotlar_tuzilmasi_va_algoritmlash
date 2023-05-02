# import requests
#
# n = 0
# while True:
#     n+=1
#     response = requests.get("https://acm.bsuir.by/solve/contests/5/problems/B")
#     print(n)

import asyncio
from aiohttp import ClientSession


async def get_request(url: str) -> None:
    async with ClientSession() as session:
        async with session.get(url=url) as request:
            if request.ok:
                response_text = await request.text()
                print(response_text)

async def main():
    url = 'https://acm.bsuir.by/solve/contests/5/problems/B'
    i =0

    while True:
        await get_request(url=url)
        i += 1
        print(i)

if __name__ == '__main__':
    asyncio.run(main())
