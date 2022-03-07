import asyncio
from logging import getLogger


logger = getLogger(__name__)


async def run_command(command: str, debug_logs: bool = False) -> str:
    process = await asyncio.create_subprocess_shell(
        cmd=command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    stdout, stderr = stdout.decode(), stderr.decode()

    if debug_logs:
        logger.debug(
            f"command: {command}, "
            f"exit code: '{process.returncode}', stderr: '{stderr}', "
            f"stdout: '{stdout}'".replace("\n", " ")
        )
    if process.returncode:
        logger.exception(f"stderr: {stderr}, stdout: {stdout}")

    return stdout
