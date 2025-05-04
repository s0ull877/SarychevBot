import asyncio
from interface_bot.main import start_polling
from logger import get_logger


if __name__ == '__main__':

    logger = get_logger()

    try:
        asyncio.run(start_polling())
    except KeyboardInterrupt:
        pass
    except Exception as ex:
        logger.error(ex)
