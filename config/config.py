from dataclasses import dataclass
from environs import Env

@dataclass
class DatabaseConfig:
    name: str
    host: str
    user: str
    password: str

@dataclass
class TgBot:
    token: str
    admin_ids: list[int]

@dataclass
class Config:
    bot: TgBot
#    db: DatabaseConfig


# Создаем экземпляр класса Env
env: Env = Env()

# Добавляем в переменные окружения данные, прочитанные из файла .env
env.read_env()

# Создаем экземпляр класса Config и наполняем его данными из переменных окружения
config = Config(
    bot=TgBot(
        token=env('BOT_TOKEN'),
        admin_ids=list(map(int, env.list('ADMIN_IDS')))
    )
)