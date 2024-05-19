# aggregator.py

import asyncio
import websockets
import logging
import json
import sys
import ssl
import certifi


class Aggregator:
    def __init__(self, url=None, ping_interval=15):
        self._url = url if url is not None else 'wss://www.seismicportal.eu/standing_order/websocket'
        self.PING_INTERVAL = ping_interval
        self.ssl_context = ssl.create_default_context(cafile=certifi.where())

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def my_processing(self, message):
        try:
            data = json.loads(message)
            logging.info(f"Received data: {json.dumps(data, indent=1)}")
        except Exception:
            logging.exception("Unable to parse JSON message")

    async def listen(self, ws):
        try:
            async for msg in ws:
                self.my_processing(msg)
        except websockets.ConnectionClosed:
            logging.info("Connection closed")

    async def launch_client(self):
        try:
            logging.info("Open WebSocket connection to %s", self._url)
            async with websockets.connect(self._url, ping_interval=self.PING_INTERVAL, ssl=self.ssl_context) as ws:
                logging.info("Waiting for messages...")
                await self.listen(ws)
        except Exception:
            logging.exception("Connection error")


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    aggregator = Aggregator()
    try:
        asyncio.get_event_loop().run_until_complete(aggregator.launch_client())
    except KeyboardInterrupt:
        logging.info("Close WebSocket")
    except Exception as e:
        logging.exception(f"Unexpected error: {e}")
