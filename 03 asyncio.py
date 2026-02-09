import asyncio

async def api_call(name):
    print(f"Start {name}")
    await asyncio.sleep(1)
    print(f"End {name}")
    
async def main(): 
    await asyncio.gather( 
        api_call("A"),
        api_call("B")
    )

asyncio.run(main())