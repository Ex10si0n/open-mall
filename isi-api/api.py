import os
import re
import sys
from fastapi import FastAPI, Form, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List


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


class LoginData(BaseModel):
    # remember: bool
    email: str
    password: str
    # remember_me: str

class RegisterData(BaseModel):
    email: str
    password: str

class AddressData(BaseModel):
    accId: str
    name: str
    tel: str
    country: str
    city: str
    detailed: str
    tag: str

class ChangePasswordData(BaseModel):
    email: str
    oldPassword: str
    newPassword: str

class CreateProductData(BaseModel):
    pName: str
    brand: str
    price: float
    pDesc: str
    thumbnail: str
    pic: str

class UpdateProductData(BaseModel):
    pid: str
    pName: str
    brand: str
    price: float
    pDesc: str
    thumbnail: str
    pic: str

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

@app.post('/api/address/create')
def create_address(addressData: AddressData):
    from db.database import create_address
    return create_address(addressData.accId, addressData.tel, addressData.name, addressData.city, addressData.country, addressData.detailed, addressData.tag)

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


@app.post('/api/login_check/')
async def login(loginData: LoginData):
    from db.database import login_check
    return login_check(loginData.email, loginData.password)

@app.post('/api/register/')
def register(registerData: RegisterData):
    from db.database import create_account
    return create_account(registerData.email.split('@')[0], registerData.email, registerData.password, 'user')


@app.get('/api/checkout/{accId}/{addrId}')
def checkout(accId: str, addrId: str):
    from db.database import check_out
    return check_out(accId, addrId)


@app.get('/api/order/{accId}')
def get_orders(accId: str):
    from db.database import get_all_purchase_of_customer
    from db.database import get_all_purchase_vendor
    if accId == 'all':
        return get_all_purchase_vendor()
    else:
        return get_all_purchase_of_customer(accId)

@app.post('/api/change_password/')
def change_password(changePasswordData: ChangePasswordData):
    from db.database import update_password
    return update_password(changePasswordData.email, changePasswordData.oldPassword, changePasswordData.newPassword)

@app.get('/api/order/pono/{pono}')
def get_detailed_purchase(pono: str):
    from db.database import get_order_by_pono
    return get_order_by_pono(pono)

@app.get('/api/order/detailed/{pono}')
def get_more_detailed_purchase(pono: str):
    from db.database import get_more_order_by_pono
    return get_more_order_by_pono(pono)

@app.get('/api/purchase/{pono}')
def get_purchase_info_by_id(pono: str):
    from db.database import get_purchase_info_by_id
    return get_purchase_info_by_id(pono)

@app.post('/api/product/create')
def create_product(createProductData: CreateProductData):
    from db.database import create_product
    return create_product(createProductData.pName, createProductData.brand, createProductData.price, createProductData.pDesc, createProductData.thumbnail, createProductData.pic)

@app.post('/api/product/{pid}/update')
def update_product(updateProductData: UpdateProductData):
    from db.database import update_product
    return update_product(updateProductData.pid, updateProductData.pName, updateProductData.brand, updateProductData.price, updateProductData.pDesc, updateProductData.thumbnail, updateProductData.pic)

@app.get('/api/search/name/{pName}')
def get_products_by_name(pName: str):
    from db.database import get_products_by_name
    return get_products_by_name(pName)

@app.get('/api/search/id/{pid}')
def get_products_by_name(pid: str):
    from db.database import get_product_by_id
    return get_product_by_id(pid)

@app.get('/api/search/brand/{brand}')
def get_products_by_brand(brand: str):
    from db.database import get_products_by_brand
    return get_products_by_brand(brand)

@app.get('/api/order/cancel/{type}/{pono}')
def cancel(type: str, pono: str):
    if type == 'vendor':
        from db.database import cancel_purchase
        return cancel_purchase('vendor', pono)
    else:
        from db.database import cancel_purchase
        return cancel_purchase('user', pono)

@app.get('/api/order/deliver/{pono}')
def deliver(pono: str):
    from db.database import ship_purchase
    return ship_purchase(pono)

@app.get('/api/order/hold/{pono}')
def hold(pono: str):
    from db.database import hold_purchase
    return hold_purchase(pono)


@app.get('/api/order/unhold/{pono}')
def unhold(pono: str):
    from db.database import unhold_purchase
    return unhold_purchase(pono)

@app.post('/api/image/upload')
async def upload_image(images: List[UploadFile]):
    for image in images:
        path = os.path.join(fpath, 'img/' + image.filename)
        with open(path, 'wb') as f:
            f.write(image.file.read())
    
