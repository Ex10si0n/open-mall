import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

fpath = os.path.join(os.path.dirname(__file__), 'db')
sys.path.append(fpath)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/products")
def test():
    from db.database import get_all_products
    return get_all_products()

