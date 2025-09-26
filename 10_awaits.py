import asyncio

async def slow_task():
    print("Starting slow task... ")
    await asyncio.sleep(2)
    print("SLow task done")
    return "Finished"

async def main():
    print("Start")
    result = await slow_task()
    print("Result: ", result)
    
asyncio.run(main())