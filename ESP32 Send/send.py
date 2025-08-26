# simulate_esp32.py
import asyncio
import websockets
import random
import time

WS_SERVER = "ws://<#Your IP address here>:8765"  # Change to your Flask WebSocket server IP

async def send_data():
    async with websockets.connect(WS_SERVER) as websocket:
        print("Connected to WebSocket server")

        while True:
            # Generate random sensor values
            node_id = "Node1"
            humidity = round(random.uniform(50, 90), 2)  # 50% to 90%
            temperature = round(random.uniform(30, 45), 2)  # 30°C to 45°C
            fan_level = 0  # can be 0 for testing

            message = f"{node_id},{humidity},{temperature},{fan_level}"
            await websocket.send(message)
            print(f"Sent: {message}")

            # Wait 5 seconds
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(send_data())
