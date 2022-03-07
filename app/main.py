import asyncio
import logging

from aiorun import run

import config
import tasks


logging.basicConfig(format=config.LOG_FORMAT, level=logging.INFO, style="{")
logger = logging.getLogger(__name__)


async def main():
    asyncio.create_task(tasks.print_status(config.PRINT_STATUS_INTERVAL))
    asyncio.create_task(tasks.disconnect(config.DISCONNECT_INTERVAL))
    locations = await tasks.get_locations()
    await tasks.keep_alive(locations, config.KEEP_ALIVE_INTERVAL)


if __name__ == "__main__":
    run(main(), use_uvloop=True, stop_on_unhandled_errors=True)
