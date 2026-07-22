from contextlib import AbstractContextManager
from sqlalchemy.orm import sessionmaker


class DatabaseAbstract(AbstractContextManager):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class UnitOfWork(DatabaseAbstract):
    """ 
    Класс для подключения к базе данных через SQLAlchemy.
    """
    def __init__(self, session_maker):
        self.session_maker: sessionmaker = session_maker

    def __enter__(self):
        """
        Возвращаем self — объект UoW, чтобы управлять транзакцией и получать доступ к методам:
        rollback, commit.
        В DI возвращаем атрибут .session, например CaseAlchemyRepository(unit_of_work.session)
        """
        self.session = self.session_maker()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.session.rollback()
        else:
            self.session.commit()

        self.session.close()

    def commit(self):
        if self.session:
            self.session.commit()

    def rollback(self):
        if self.session:
            self.session.rollback()