from fastapi import FastAPI,Depends,UploadFile,File,Form
from database import LocalSession,engine,Base
import shutil
import os
from sqlalchemy.orm import Session
from models import Resource
from schema import Resourceout


def getdb():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI()


@app.get("/")
def user_interface():
    return "WelCome to College Resource Sharing Portal"

@app.post("/notes/",response_model=Resourceout)
def add_notes(db:Session = Depends(getdb),course:str =Form(...),scheme:str = Form(...),semester:str=Form(...),subject:str = Form(...),file:UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"
    
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    
    db_resource = Resource(
        course = course,
        scheme = scheme,
        semester = semester,
        subject = subject,
        file = file_path
    )
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    
    print("Saved to DB:", db_resource.id, db_resource.course)  # debug
    return db_resource
    
@app.get("/notes/",response_model=list[Resourceout])
def get_notes(db:Session = Depends(getdb)):
    return db.query(Resource).all()
