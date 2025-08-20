from fastapi import FastAPI,Depends
from database import LocalSession,engine,Base


def getdb():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

app = FastAPI()


