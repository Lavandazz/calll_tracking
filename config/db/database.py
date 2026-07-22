from config.settings_env import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


ADB_URL = settings.get_sync_db_url()
engine = create_engine(url=ADB_URL)
sync_sessionmaker = sessionmaker(bind=engine, expire_on_commit=False)
