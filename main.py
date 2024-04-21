import json
import os
from typing import Literal, Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException
import random
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from mangum import Mangum

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

url = URL.create(
    drivername="mysql",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    port=os.getenv("DB_PORT")
)


engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()


# Run locally
# $ uvicorn main:sd_api_test --reload

# Run on ec2 server (python3 = 3.10.x)
# $ python3 -m uvicorn main:sd_api_test --reload


sd_api_test = FastAPI()
handler = Mangum(sd_api_test)


@sd_api_test.get("/")
async def root():
    return {"message": "Welcome to the SD API Test Server!"}