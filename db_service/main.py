import asyncio

from db.session import sessionmanager
from db.models.base import Base


async def main():
    while True:
        async with sessionmanager.connect() as connection:
            print(f'In session!!Base tables -> {Base.metadata.tables}', flush=True)
            await asyncio.sleep(10000)


asyncio.run(main())
