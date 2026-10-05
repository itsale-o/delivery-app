from models import db
from sqlalchemy.orm import sessionmaker

def session_db():
    try:
        Session = sessionmaker(bind=db)
        session = Session()

        yield session
    finally:
        session.close()