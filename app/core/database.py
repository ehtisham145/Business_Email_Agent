from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    """This function will create a session that
will automatically close once user has done its work"""
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()