import zmq
import zmq.asyncio
import asyncio


async def server():
    """Generates a string and pushes it to a ZMQ socket."""

    context = zmq.asyncio.Context()
    socket = context.socket(zmq.PUSH)

    address = "tcp://*:3000"  # Bind to all interfaces on port 3000
    socket.bind(address)

    print(f"Server listening on {address}")

    try:
        while True:
            message = "Hello from server"
            await socket.send_pyobj(message)  # Send as a Python object
            print(f"Sent: {message}")
            await asyncio.sleep(1)  # Send a message every 1 second
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        socket.close()
        context.term()


if __name__ == "__main__":
    print("Server starting...")
    asyncio.run(server())
