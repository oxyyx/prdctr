from loguru import logger
import asyncpg
from fastapi import FastAPI
from app.core.settings import Settings


async def connect_to_db(app: FastAPI, settings: Settings) -> None:
    logger.info(f"Connecting to database: {settings.DATABASE_URL}")

    app.state.pool = await asyncpg.create_pool(
        str(settings.DATABASE_URL)
    )

    logger.info("Connected.")


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Disconnecting from database.")

    await app.state.pool.close()

    logger.info("Disconnected.")