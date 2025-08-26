# esp32_simulator.py
import asyncio
import websockets

# Flask WebSocket server URL
WS_SERVER = "ws://#Your IP address here:8765"  # or use your PC local IP

async def listen_commands():
    async with websockets.connect(WS_SERVER) as websocket:
        print("Connected to Flask WebSocket server. Waiting for commands...")

        while True:
            command = await websocket.recv()
            command = command.upper()  # Normalize
            if command == "ON":
                print("[SIMULATOR] ON button pressed")
            elif command == "OFF":
                print("[SIMULATOR] OFF button pressed")
            elif command == "AUTO":
                print("[SIMULATOR] AUTO mode activated")
            else:
                print(f"[SIMULATOR] Unknown command received: {command}")

if __name__ == "__main__":
    asyncio.run(listen_commands())
