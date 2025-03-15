import zmq
import zmq.asyncio
import asyncio
import os


async def main():
    """Asynchronously connects to a ZMQ publisher using push/pull, receives messages, and prints them."""

    context = zmq.asyncio.Context()
    socket = context.socket(zmq.PULL)
    address = os.environ.get("ZMQ_PUB_ADDRESS", "tcp://127.0.0.1:3000")

    print(f"Connecting to {address}")
    socket.connect(address)

    try:
        while True:
            # No polling needed with PULL! zmq.recv() is non-blocking when connected
            msg = await socket.recv_pyobj()  # Run recv in a separate thread

            print(f"Message received: {msg}")
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        socket.close()
        context.term()


if __name__ == "__main__":
    print("App starting...")
    asyncio.run(main())
