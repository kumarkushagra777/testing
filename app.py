import asyncio

async def main():
    i = 0
    while True:
        await asyncio.sleep(600)
        print(f"working: {i}")
        i += 1

# To run the async function
if __name__ == "__main__":
    asyncio.run(main())
