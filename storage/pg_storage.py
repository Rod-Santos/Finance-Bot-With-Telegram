from aiogram.dispatcher.storage import BaseStorage

class PostgresStorage(BaseStorage):
    async def close(self):
        pass

    async def wait_closed(self):
        pass

    async def get_state(self, *args, **kwargs):
        # Sua lógica para obter o estado do PostgreSQL
        pass

    async def get_data(self, *args, **kwargs):
        # Sua lógica para obter os dados do PostgreSQL
        pass