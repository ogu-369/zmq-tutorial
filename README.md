# ZeroMQ Tutorial

This repository provides a basic example of using ZeroMQ to build a simple client-server application. ZeroMQ is a high-performance, asynchronous messaging library designed for distributed systems and concurrent applications.

## File Structure

- `server.py`: A sample server implementation using ZeroMQ that listens for client messages and responds.
- `client.py`: A sample client implementation using ZeroMQ that connects to the server, sends a message, and receives a response.
- `requirements.txt`: A file listing the required Python dependencies.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ogu-369/zmq-tutorial.git
   cd zmq-tutorial
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use 'env\Scripts\activate'
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the server:
   ```bash
   python server.py
   ```

2. In a separate terminal, start the client:
   ```bash
   python client.py
   ```

The client will send a message to the server and receive a response.

## Overview of ZeroMQ

ZeroMQ (ØMQ, ZMQ, or 0MQ) is a high-performance, asynchronous messaging library. It enables scalable and flexible application architectures by supporting various messaging patterns such as request/reply, publish/subscribe, and client/server. It operates without requiring a dedicated message broker, making it lightweight and efficient.

For more details, visit [zeromq.org](https://zeromq.org/get-started/).

