from fastapi import FastAPI,Depends,UploadFile,File,Form
from database import LocalSession,engine,Base
import shutil
import os
from sqlalchemy.orm import Session
import models


def getdb():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(bind=engine)

if not os.path.exists("uploads"):
    os.makedirs("uploads")

app = FastAPI()


@app.get("/")
def user_interface():
    return "WelCome to College Resource Sharing Portal"

@app.post("/notes/")
def add_notes(
    course: str =Form(...),
    scheme: int = Form(...),
    semester: int=Form(...),
    subject: str = Form(...),
    file: UploadFile = File(...),
    db:Session = Depends(getdb)
    ):
    
    file_path = os.path.join("uploads", file.filename)
    
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    
    db_resource = models.Resource(
        course = course,
        scheme = scheme,
        semester = semester,
        subject = subject,
        file = file_path
    )
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource
    
@app.get("/notes/",)
def get_notes(db:Session = Depends(getdb)):
    return db.query(models.Resource).all()
