from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from  ..config import get_settings

settings = get_settings()
engine = create_engine(settings.sqlalchemy_database_uri, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations.

    Yields:
        sqlalchemy.orm.Session: A local SQLAlchemy session.

    Examples:

        >>> with session_scope() as session:
        ...    session.add(Table1(url="https://www.example.com"))
        ...    session.commit()
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
