import asyncio
import logging

from app.database import create_db_and_tables


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info('Creating initial data')
    asyncio.run(create_db_and_tables())
    logger.info('Initial data created')


if __name__ == '__main__':
    main()
