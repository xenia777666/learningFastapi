from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
 # из расширений библиотеки для бд берем асинхронный движок
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.orm import declarative_base, Mapped, mapped_column


engine = create_async_engine(
   "sqlite+aiosqlite:///tasks.db") #юрл бд+назва бд+драйвер+назв файла)
new_session = async_sessionmaker(engine, expire_on_commit=False )
# Здесь мы создаем асинхронное подключение, которое будет отвечать за отправку запросов в базу
# данных engine. Обратите внимание, что мы говорим SQLAlchemy, что будем использовать
# драйвер для асинхронного кода aiosqlite. После создания engine, с которым уже можно работать,
# мы дополнительно создаем фабрику сессий new_session. Сессия позволяет
# работать не с обычными списками и словарями, а с моделями данных, которые создаются через классы

class Model(DeclarativeBase):
   pass

class TaskTable(Model):  #таблица
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]

async def create_tables():
   async with engine.begin() as conn:
       await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
   async with engine.begin() as conn:
       await conn.run_sync(Model.metadata.drop_all)