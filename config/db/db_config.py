from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings_env import settings
from config.db.database import UnitOfWork


ADB_URL = settings.get_sync_db_url()
engine = create_engine(url=ADB_URL)
sync_sessionmaker = sessionmaker(bind=engine, expire_on_commit=False)


def get_db():
    unit_of_work = UnitOfWork(sync_sessionmaker)
    with unit_of_work:
        yield unit_of_work
        