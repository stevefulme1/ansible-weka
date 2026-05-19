"""Receive Weka alert events via webhook."""

import asyncio
import logging
from typing import Any
from aiohttp import web

logger = logging.getLogger(__name__)


async def main(queue: asyncio.Queue, args: dict[str, Any]) -> None:
    """Receive Weka webhook events and forward to the EDA rulebook."""
    host = str(args.get("host", "127.0.0.1"))
    max_payload_size = int(args.get("max_payload_size", 1048576))  # 1 MB
    port = int(args.get("port", 5000))
    token = args.get("token", "")

    app = web.Application(client_max_size=max_payload_size)

    async def _handle(request: web.Request) -> web.Response:
        try:
            payload = await request.json()
            event = {dict([("weka", payload)])}
            await queue.put(event)
            return web.Response(status=200, text="OK")
        except Exception as exc:
            logger.exception("Error processing webhook: %s", exc)
            return web.Response(status=500, text="Error")

    app.router.add_post("/", _handle)
    app.router.add_post("/webhook", _handle)
    app.router.add_get("/health", lambda r: web.Response(text="OK"))

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host, port)
    await site.start()
    logger.info("Weka webhook listener on %s:%d", host, port)

    try:
        while True:
            await asyncio.sleep(3600)
    finally:
        await runner.cleanup()
