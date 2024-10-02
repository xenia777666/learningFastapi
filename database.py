from sqlalchemy.ext.asyncio import create_async_engine
    AsyncSession  # из расширений библиотеки для бд берем асинхронный движок
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

engine = create_async_engine(
   "sqlite+aiosqlite:///tasks.db") #юрл бд+назва бд+драйвер+назв файла)

new_session = async.sessionmaker(engine, expire_on_commit=False )#фабрика создания сессий, открытие трнзакций для создания бд + параметр

class Model(DeclarativeBase):
   pass

class TaskTable(Model)#таблица
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]