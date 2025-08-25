from fastapi import FastAPI,Depends,UploadFile,File,Form,Query
from database import LocalSession,engine,Base
import shutil
import os
from sqlalchemy.orm import Session
import models
from fastapi.responses import FileResponse


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


@app.get("/download/")
def download_resources(
    db:Session = Depends(getdb),
    course : str = Query(...),
    scheme : int = Query(...),
    semester :int = Query(...),
    subject : str = Query(...)
    ):
    
    record = (
        db.query(models.Resource).filter(
            models.Resource.course == course,
            models.Resource.scheme == scheme,
            models.Resource.semester == semester,
            models.Resource.subject == subject
        )
    ).first()
    
    if not record:
        return {"error": "No file found for the given filters"}

    # file_path = os.path.join("uploads", record.file)

    file_path = record.file.replace("\\", "/")
    
    if not os.path.exists(file_path):
        return {"error": "File not found on server"}
    
    return FileResponse(path=file_path, filename=record.file, media_type="application/octet-stream")
