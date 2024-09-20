from flask import Flask
import asyncio

app = Flask(__name__)
i = 0

@app.route("/")
def index():
    global i
    return f"Working: {i}"

async def increment():
    global i
    while True:
        await asyncio.sleep(600)
        i += 1

if __name__ == "__main__":
    asyncio.create_task(increment())
    app.run(host='0.0.0.0', port=3000)
