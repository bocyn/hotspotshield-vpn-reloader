import os


LOG_FORMAT = (
    "\033[1;94m{asctime:s} \033[1;92m{levelname:8s} "
    "\033[0;96m{threadName} {name}.{funcName}\033[0m {message}"
)


KEEP_ALIVE_INTERVAL = int(os.getenv("KEEP_ALIVE_INTERVAL", 5))
PRINT_STATUS_INTERVAL = int(os.getenv("PRINT_STATUS_INTERVAL", 5))
DISCONNECT_INTERVAL = int(os.getenv("DISCONNECT_INTERVAL", 60 * 3))  # God loves the trinity ;)

