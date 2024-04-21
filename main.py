import json
import os
from typing import Literal, Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException
import random
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from mangum import Mangum

from sqlalchemy import create_engine, MetaData, Table, select, Column, Integer, String, Boolean
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base


# Run locally
# $ uvicorn main:app --reload

# Run on ec2 server (python3 = 3.10.x)
# $ python3 -m uvicorn main:app --reload


url = URL.create(
    drivername="mysql+pymysql",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    port=os.getenv("DB_PORT")
)


engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()
handler = Mangum(app)


@app.get("/")
async def root():
    return {"message": "Welcome to the SD API Test Server!"}


@app.get("/v1/members/")
async def getUsers():
    db = SessionLocal()
    print("check")
    # Define your SQLAlchemy model
    metadata = MetaData()
    member = Table('member', metadata, autoload=True, autoload_with=engine)
    # Execute a SELECT query
    query = select([member])
    result = db.execute(query)
    # Fetch results
    member_data = result.fetchall()
    # Close the database session
    db.close()
    # Return the query results
    return {"member": member_data}

