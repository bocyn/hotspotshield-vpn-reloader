import asyncio
import random
import re

from helpers import run_command

from logging import getLogger


logger = getLogger(__name__)


async def print_status(interval: int):
    while True:
        output = await run_command(command=f"hotspotshield status")
        logger.info(f"\n{output}")
        await asyncio.sleep(interval)


async def get_locations() -> list:
    output = await run_command(command="hotspotshield locations")
    pattern = re.compile(r"[A-Z]{2,5}")
    locations = re.findall(pattern, output)
    logger.info(f"{locations=}")
    return locations


async def is_connected() -> bool:
    pattern = "VPN connection state : connected"
    output = await run_command(command=f"hotspotshield status")
    if pattern in output:
        return True
    else:
        logger.warning(False)
        return False


async def connect(location: str):
    await run_command(command=f"hotspotshield connect {location}")


async def keep_alive(locations: list, interval: int):
    while True:
        if not await is_connected():
            await connect(random.choice(locations))
            await asyncio.sleep(interval)
        await asyncio.sleep(interval)


async def disconnect(interval: int):
    while True:
        await asyncio.sleep(interval)
        await run_command(command=f"hotspotshield disconnect")
        logger.info("hotspotshield disconnect")
