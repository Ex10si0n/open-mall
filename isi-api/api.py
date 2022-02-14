import os
import re
import sys
from turtle import up
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

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


@app.get("/api/address/{accid}")
def get_address(accid: str):
    from db.database import get_user_address_list
    return get_user_address_list(accid)


@app.get("/api/address_by_id/{addrId}")
def get_addrId(addrId: str):
    from db.database import get_address_by_id
    return get_address_by_id(addrId)


@app.get("/api/img/{filename}")
async def root(filename: str):
    return FileResponse(os.path.join(fpath, 'img/' + filename))


@app.get("/api/products")
def test():
    from db.database import get_all_products
    return get_all_products()


@app.get("/api/product/{id}")
def get_product_by_id(id: str):
    from db.database import get_product_by_id
    return get_product_by_id(id)


@app.get("/api/cart/add/{pid}/{accid}/{quantity}")
def add_product_to_cart(pid: str, accid: str, quantity: int):
    from db.database import add_product_to_cart
    return add_product_to_cart(pid, accid, quantity)


@app.get("/api/cart/del/{pid}/{accId}")
def delete_product_from_cart(pid: str, accId: str):
    from db.database import delete_product_from_cart
    return delete_product_from_cart(pid, accId)


@app.get("/api/cart/products/{accId}")
def get_cart_by_id(accId: str):
    from db.database import get_all_products_in_cart
    return get_all_products_in_cart(accId)


@app.get("/api/cart/update/{pid}/{accId}/{quantity}")
def update_product_from_cart(pid: str, accId: str, quantity: int):
    from db.database import update_product_quantity_in_cart
    return update_product_quantity_in_cart(pid, accId, quantity)
