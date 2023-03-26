import argparse
import asyncio
import websockets
import json

ws_host = 'ws://qreader.htb:5789'

async def ws_connect(url, message):
    async with websockets.connect(url) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        return response

def version(path, version=None):
    if version is None:
        message = {}
    else:
        message = {'version': version}
    response = asyncio.run(ws_connect(f"{ws_host}/{path}", json.dumps({
        'version': version })))
    print(response)
    data = json.loads(response)
    if 'error' not in data.keys():
        version_info = data['message']
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--version', type=str, help='The version number')
    parser.add_argument('--path', type=str, help='The path to connect')
    args = parser.parse_args()

    if args.path:
        if args.path == 'update':
            version(args.path)
        elif args.version:
            version(args.path, args.version)
        else:
            print("Please provide a version number using the --version argument.")
    else:
        print("Please provide a path using the --path argument.")

