from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Inventory Management API"}

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))