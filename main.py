import json
import os
from typing import Literal, Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException
import random
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from mangum import Mangum

# Execute the command below to run this API test server
# $ uvicorn main:sd_api_test --reload

sd_api_test = FastAPI()
handler = Mangum(sd_api_test)


@sd_api_test.get("/")
async def root():
    return {"message": "Welcome to the SD API Test Server!"}