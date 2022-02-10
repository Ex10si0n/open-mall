import settings
import pymysql.cursors
import uuid
import password_validator
from datetime import date

imgdir = 'img/'


def create_connection():
    return pymysql.connect(host=settings.db_host,
                           user=settings.db_user,
                           password=settings.db_password,
                           database=settings.database,
                           cursorclass=pymysql.cursors.DictCursor)


def create_account(accName: str, email: str, password: str, accType: str):
    """ Create a new account

    Args:
        accName (str): user nickname
        email (str): user email address
        password (str): user password
        accType (str): user account type (admin, customer, vendor)

    Returns:
        dict: status(email_exists, success, error), uuid
    """
    playload = {'status': '', 'uuid': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `account` WHERE `email`=%s"
                cursor.execute(sql, (email,))
                result = cursor.fetchall()
                if (len(result) != 0):
                    playload['status'] = 'email_exists'
                    return playload
                sql = "INSERT INTO `account` (`ACCID`, `ACCNAME`, `HASHEDPASSWORD`, `EMAIL`, `ACCTYPE`) VALUES (%s, %s, %s, %s, %s)"
                accId = str(uuid.uuid4())
                cursor.execute(sql, (accId, accName, password_validator.hash(
                    password, accId), email, accType))
                connection.commit()
                playload['status'] = 'success'
                playload['uuid'] = accId
                return playload
    except:
        playload['status'] = 'error'
        return playload


def login_check(email: str, password: str):
    """ Login check

    Args:
        email (str): user email
        password (str): user password

    Returns:
        dict: status(account_not_registered, success, invalid_password), uuid, type
    """
    playload = {'status': '', 'uuid': '', 'type': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `account` WHERE `email`=%s"
                cursor.execute(sql, (email,))
                result = cursor.fetchone()
                if (result is None):
                    playload['status'] = 'account_not_registered'
                    return playload
                given_hashed_password = password_validator.hash(
                    password, result['ACCID'])
                if given_hashed_password == result['HASHEDPASSWORD']:
                    playload['status'] = 'success'
                    playload['uuid'] = result['ACCID']
                    playload['type'] = result['ACCTYPE']
                    return playload
                else:
                    playload['status'] = 'invalid_password'
                    return playload
    except:
        playload['status'] = 'error'
        return playload


def delete_account(email: str, password: str):
    """ delete a user by email permanently

    Args:
        email (str): user email
        password (str): user password

    Returns:
        dict: status(account_not_registered, success,
                     authentication_error, error)
    """
    playload = {'status': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `account` WHERE `email`=%s"
                cursor.execute(sql, (email,))
                result = cursor.fetchone()
                if (result is None):
                    playload['status'] = 'account_not_registered'
                    return playload
                given_hashed_password = password_validator.hash(
                    password, result['ACCID'])
                if given_hashed_password == result['HASHEDPASSWORD']:
                    sql = "DELETE FROM `account` WHERE `email`=%s"
                    cursor.execute(sql, (email,))
                    connection.commit()
                    playload['status'] = 'success'
                    return playload
                else:
                    playload['status'] = 'authentication_error'
                    return playload
    except:
        playload['status'] = 'error'
        return playload


def update_password(email: str, old_password: str, new_password: str):
    """ update user password

    Args:
        email (str): user email
        old_password (str): old password
        new_password (str): new password

    Returns:
        dict: status(account_not_registered, success, authentication_error)
    """
    playload = {'status': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `account` WHERE `email`=%s"
                cursor.execute(sql, (email,))
                result = cursor.fetchone()
                if (result is None):
                    playload['status'] = 'account_not_registered'
                    return playload
                given_hashed_password = password_validator.hash(
                    old_password, result['ACCID'])
                if given_hashed_password == result['HASHEDPASSWORD']:
                    playload['status'] = 'success'
                    sql = "UPDATE `account` SET `hashedpassword` = %s WHERE `email` = %s"
                    new_password_hashed = password_validator.hash(
                        new_password, result['ACCID'])
                    cursor.execute(sql, (new_password_hashed, email))
                    connection.commit()
                    return playload
                else:
                    playload['status'] = 'authentication_error'
                    return playload
    except:
        playload['status'] = 'error'


def create_address(accId: str, tel: str, name: str, city: str, country: str, detailed: str, tag: str):
    """ create user's address

    Args:
        accId (str): user id
        tel (str): user telephone number
        name (str): user name
        city (str): user city
        country (str): user country
        detailed (str): user detailed address

    Returns:
        dict: status(success, error)
    """
    playload = {'status': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO `address` (`ADDRID`, `ACCID`, `TEL`, `NAME`, `CITY`, `COUNTRY`, `DETAILED`, `TAG`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                addrId = str(uuid.uuid4())
                cursor.execute(
                    sql, (addrId, accId, tel, name, city, country, detailed, tag))
                connection.commit()
                playload['status'] = 'success'
                return playload
    except:
        playload['status'] = 'error'
        return playload


def get_user_address_list(addId: str):
    """ get user's address list

    Args:
        addId (str): user id

    Returns:
        dict: status(success, error), address list
    """
    playload = {'status': '', 'address_list': []}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `address` WHERE `ACCID`=%s"
                cursor.execute(sql, (addId,))
                result = cursor.fetchall()
                if (len(result) == 0):
                    playload['status'] = 'success'
                    return playload
                else:
                    playload['status'] = 'success'
                    for row in result:
                        address = {
                            'addrId': row['ADDRID'],
                            'tel': row['TEL'],
                            'name': row['NAME'],
                            'city': row['CITY'],
                            'country': row['COUNTRY'],
                            'detailed': row['DETAILED'],
                            'tag': row['TAG']
                        }
                        playload['address_list'].append(address)
                    return playload
    except:
        playload['status'] = 'error'
        return playload


def update_user_address(addId: str, tel: str, name: str, city: str, country: str, detailed: str, tag: str):
    """ update user's address

    Args:
        addId (str): user id
        tel (str): user telephone number
        name (str): user name
        city (str): user city
        country (str): user country
        detailed (str): user detailed address

    Returns:
        dict: status(success, error)
    """
    playload = {'status': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "UPDATE `address` SET `TEL`=%s, `NAME`=%s, `CITY`=%s, `COUNTRY`=%s, `DETAILED`=%s `TAG`=%s WHERE `ADDRID`=%s"
                cursor.execute(
                    sql, (tel, name, city, country, detailed, tag, addId))
                connection.commit()
                playload['status'] = 'success'
                return playload
    except:
        playload['status'] = 'error'
        return playload


def delete_address(addId: str, accId: str):
    """ delete user's address

    Args:
        addId (str): user id
        accId (str): user id

    Returns:
        dict: status(success, error)
    """
    playload = {'status': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "DELETE FROM `address` WHERE `ADDRID`=%s AND `ACCID`=%s"
                cursor.execute(sql, (addId, accId))
                connection.commit()
                playload['status'] = 'success'
                return playload
    except:
        playload['status'] = 'error'
        return playload


def create_product(pName: str, brand: str, price: float, pDesc: str, thumbnail: str, pic: str):
    """ Create a new product

    Args:
        pName (str): product name
        brand (str): product brand
        price (float): product price  @TODO: currency calculation
        pDesc (str): product description
        thumbnail (str): thumbnail image
        pic (str): product detail image

    Returns:
        dict: status(success, error), pid
    """
    playload = {'status': '', 'pid': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO `product` (`PID`, `PNAME`, `BRAND`, `PRICE`, `PDESC`, `THUMBNAIL`, `PIC`)  VALUES (%s, %s, %s, %s, %s, %s, %s)"
                pid = str(uuid.uuid4())
                cursor.execute(sql, (pid, pName, brand, price,
                               pDesc, thumbnail, pic))
                connection.commit()
                playload['status'] = 'success'
                playload['pid'] = pid
                return playload
    except:
        playload['status'] = 'error'
        return playload


def get_all_products():
    """ Get all products

    Args:
        None

    Returns:
        dict: status(success, none, error), product list
    """
    playload = {'status': '', 'product_list': []}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `product`"
                cursor.execute(sql)
                result = cursor.fetchall()
                if (len(result) == 0):
                    playload['status'] = 'none'
                    return playload
                else:
                    playload['status'] = 'success'
                    for row in result:
                        product = {
                            'pid': row['PID'],
                            'pname': row['PNAME'],
                            'brand': row['BRAND'],
                            'price': row['PRICE'],
                            'pdesc': row['PDESC'],
                            'thumbnail': row['THUMBNAIL'],
                            'pic': row['PIC'],
                        }
                        playload['product_list'].append(product)
                    return playload
    except:
        playload['status'] = 'error'
        return playload

def get_product_by_id(id: str):
    """ Get product by id

    Args:
        id (str): product id

    Returns:
        dict: status(success, none, error), product
    """
    playload = {'status': '', 'product': {}}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `product` WHERE `PID`=%s"
                cursor.execute(sql, (id,))
                result = cursor.fetchall()
                if (len(result) == 0):
                    playload['status'] = 'none'
                    return playload
                else:
                    playload['status'] = 'success'
                    for row in result:
                        product = {
                            'pid': row['PID'],
                            'pname': row['PNAME'],
                            'brand': row['BRAND'],
                            'price': row['PRICE'],
                            'pdesc': row['PDESC'],
                            'thumbnail': row['THUMBNAIL'],
                            'pic': row['PIC'],
                        }
                        playload['product'] = product
                    return playload
    except:
        playload['status'] = 'error'
        return playload

def get_products_by_brand(brand: str):
    """ Get products by brand

    Args:
        brand (str): product brand

    Returns:
        dict: status(success, error), product list
    """
    playload = {'status': '', 'product_list': []}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `product` WHERE `BRAND`=%s"
                cursor.execute(sql, (brand,))
                result = cursor.fetchall()
                if (len(result) == 0):
                    playload['status'] = 'success'
                    return playload
                else:
                    playload['status'] = 'success'
                    for row in result:
                        product = {
                            'pid': row['PID'],
                            'pName': row['PNAME'],
                            'brand': row['BRAND'],
                            'price': row['PRICE'],
                            'pDesc': row['PDESC'],
                            'thumbnail': row['THUMBNAIL'],
                            'pic': row['PIC'],
                        }
                        playload['product_list'].append(product)
                    return playload
    except:
        playload['status'] = 'error'
        return playload


def get_products_by_name(name: str):
    """ Get products by name

    Args:
        name (str): product name

    Returns:
        dict: status(success, error), products
    """
    playload = {'status': '', 'products': []}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `product` WHERE `PNAME` LIKE %s"
                cursor.execute(sql, ('%' + name + '%',))
                result = cursor.fetchall()
                if (result is None):
                    playload['status'] = 'error'
                    return playload
                playload['status'] = 'success'
                playload['products'] = result
                return playload
    except:
        playload['status'] = 'error'
        return playload

def update_product(pid: str, pName: str, brand: str, price: float, pDesc: str, thumbnail: str, pic: str):
    """ Update product

    Args:
        pid (str): product id
        pName (str): product name
        brand (str): product brand
        price (float): product price  @TODO: currency calculation
        pDesc (str): product description
        thumbnail (str): thumbnail image
        pic (str): product detail image

    Returns:
        dict: status(success, error), pid
    """
    playload = {'status': '', 'pid': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "UPDATE `product` SET `PNAME`=%s, `BRAND`=%s, `PRICE`=%s, `PDESC`=%s, `THUMBNAIL`=%s, `PIC`=%s WHERE `PID`=%s"
                cursor.execute(sql, (pName, brand, price, pDesc, thumbnail, pic, pid))
                connection.commit()
                playload['status'] = 'success'
                playload['pid'] = pid
                return playload
    except:
        playload['status'] = 'error'
        return playload

def update_product_price(pid: str, new_price: int):
    """ Update product's price

    Args:
        pid (str): product id
        new_price (int): new price

    Returns:
        dict: status(success, error)
    """
    playload = {'status': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "UPDATE `product` SET `PRICE` = %s WHERE `PID` = %s"
                cursor.execute(sql, (new_price, pid))
                connection.commit()
                playload['status'] = 'success'
                return playload
    except:
        playload['status'] = 'error'
        return playload


def delete_product(pid: str):
    """ Delete product

    Args:
        pid (str): product id

    Returns:
        dict: status(success, error)
    """
    playload = {'status': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "DELETE FROM `product` WHERE `PID` = %s"
                cursor.execute(sql, (pid,))
                connection.commit()
                playload['status'] = 'success'
                return playload
    except:
        playload['status'] = 'error'
        return playload


def add_product_to_cart(pid: str, accid: str, quantity: int):
    """ Add product to shopping cart list

    Args:
        pid (str): product id
        accid (str): user id
        quantity (int): product quantity

    Returns:
        dict: status(success, error), cartid
    """
    playload = {'status': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `shopping_cart` WHERE `PID`=%s AND `ACCID`=%s"
                cursor.execute(sql, (pid, accid))
                result = cursor.fetchone()
                if (result is None):
                    sql = "INSERT INTO `shopping_cart` (`CARTID`, `PID`, `ACCID`, `QUANTITY`) VALUES (%s, %s, %s, %s)"
                    cartid = str(uuid.uuid4())
                    cursor.execute(sql, (cartid, pid, accid, quantity))
                    connection.commit()
                    playload['status'] = 'success'
                    return playload
                else:
                    playload['status'] = 'error'
                    return playload
    except:
        playload['status'] = 'error'
        return playload


def update_product_quantity_in_cart(cartId: str, accId: str, quantity: int):
    """ Update product quantity in shopping cart

    Args:
        cartId (str): cart id
        accId (str): user id
        quantity (int): product quantity

    Returns:
        dict: status(success, error)
    """
    playload = {'status': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "UPDATE `shopping_cart` SET `QUANTITY` = %s WHERE `CARTID` = %s AND `ACCID` = %s"
                cursor.execute(sql, (quantity, cartId, accId))
                connection.commit()
                playload['status'] = 'success'
                return playload
    except:
        playload['status'] = 'error'
        return playload


def delete_product_from_cart(cartId: str, accId: str):
    """ Delete product from shopping cart list

    Args:
        cartId (str): shopping cart id
        accId (str): user id

    Returns:
        dict: status(success, error)
    """
    playload = {'status': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "DELETE FROM `shopping_cart` WHERE `CARTID`=%s AND `ACCID`=%s"
                cursor.execute(sql, (cartId, accId))
                connection.commit()
                playload['status'] = 'success'
                return playload
    except:
        playload['status'] = 'error'
        return playload


def delete_all_product_from_cart(accId: str):
    """ Delete all product from shopping cart list

    Args:
        accId (str): user id

    Returns:
        dict: status(success, error)
    """
    playload = {'status': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "DELETE FROM `shopping_cart` WHERE `ACCID`=%s"
                cursor.execute(sql, (accId,))
                connection.commit()
                playload['status'] = 'success'
                return playload
    except:
        playload['status'] = 'error'
        return playload


def get_all_products_in_cart(accId: str):
    """ List all product in cart

    Args: 
        accId(str): user id

    Returns:
        dict: status(success, error), product
    """
    playload = {'status': '', 'shopping_cart_list': []}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `shopping_cart` WHERE `ACCID` = %s"
                cursor.execute(sql,(accId))
                result = cursor.fetchall()
                if (len(result) == 0):
                    playload['status'] = 'none'
                    return playload
                else:
                    for row in result:
                        sql = "SELECT PNAME, PRICE FROM `product` WHERE `PID` = %s"
                        pid = row['PID']
                        quantity = row['QUANTITY']
                        cursor.execute(sql, (pid))
                        product = cursor.fetchone()
                        shopping_cart= {
                            'pname': product['PNAME'],
                            'price': product['PRICE'],
                            'quantity': quantity
                        }
                        playload['status'] = 'success'
                        playload['shopping_cart_list'].append(shopping_cart)
                        return playload
    except:
        playload['status'] = 'error'
        return playload 


def check_out(accId: str):
    """Check out all items in the shopping cart and create a purchase order

    Args: 
        accId(str): user id

    Returns:
        dict: status(success, error), purchase order number
    """
    playload = {'status': '', 'PONO': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `shopping_cart` WHERE `ACCID` = %s"
                cursor.execute(sql,(accId,))
                result = cursor.fetchall()
                if (len(result) == 0):
                    playload['status'] = 'none'
                    return playload
                else:
                    amount = 0
                    pono = str(uuid.uuid4())
                    for row in result:
                        cartId = row['CARTID']
                        pid = row['PID']
                        quantity = row['QUANTITY']
                        sql = "SELECT PRICE FROM `product` WHERE `PID` = %s"
                        cursor.execute(sql,(pid))
                        product = cursor.fetchone()
                        price = product['PRICE']                 
                        subtotal = quantity * price
                        amount = amount + subtotal
                        sql = "INSERT INTO `order` (`PONO`, `PRICE`, `OID`, `PID`, `QUANTITY`, `SUBTOTAL`) VALUES (%s, %s, %s, %s, %s, %s)"
                        oid = str(uuid.uuid4())
                        print('pono:' + pono)
                        print(price)
                        print('oid:' + oid)
                        print('pid:' + pid)
                        print(quantity)
                        print(subtotal)
                        cursor.execute(sql,(pono, price, oid, pid, quantity, subtotal))
                        connection.commit()
                        delete_product_from_cart(cartId, accId)
                    sql = "INSERT INTO `purchase` (`PONO`, `ACCID`, `DATE`, `STATUS`, `AMOUNT`) VALUES (%s, %s, %s, %s, %s)"
                    today = date.today().strftime("%Y-%m-%d")
                    cursor.execute(sql,(pono, accId, today, 'pending', amount))
                    connection.commit()
                    playload['status'] = 'success'
                    playload['PONO'] = pono
                    return playload
    except:
        playload ['status'] = 'error'
        return playload    


def get_all_purchase(accId: str):
    """List all purchase orders that the customer has placed

    Args: 
        accId(str): user id

    Returns:
        dict: status(success, error), purchase_list
    """
    playload = {'status': '', 'purchase_list': []}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `purchase` WHERE `ACCID` = %s ORDER BY `DATE` DESC"
                cursor.execute(sql,(accId))
                result = cursor.fetchall()
                if (len(result) == 0):
                    playload['status'] = 'none'
                    return playload
                else:
                    for row in result:
                        purchase = {
                            'pono': row['PONO'],
                            'date': row['DATE'],
                            'amount': row['AMOUNT'],
                            'status': row['STATUS']
                        }
                        playload['status'] = 'success'
                        playload['purchase_list'].append(purchase)
                        return playload
    except:
        playload['status'] = 'error'
        return playload
    

def get_purchase_with_particular_status(accId: str, status: str):
    """Show 'current purchase' with status 'pending' and 'hold', and show 'past purchases' with status 'shipped' and 'cancelled'
    
    Args: 
        accId(str): user id, status(str): current/past

    Returns:
        dict: status(success, error), purchase_list
    """

    playload = {'status': '', 'purchase_list': []}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `purchase` WHERE `ACCID` = %s AND (`STATUS` = %s OR `STATUS` = %s)"
                if(status == 'current'):
                    cursor.execute(sql,(accId, 'pending', 'hold'))
                elif (status == 'past'):
                    cursor.execute(sql,(accId, 'shipped', 'cancelled'))  
                else:
                    playload['status'] = 'wrong status'
                    return playload
                result = cursor.fetchall()
                if (len(result) == 0):
                    playload['status'] = 'none'
                    return playload
                else:
                    for row in result:
                        purchase = {
                            'pono': row['PONO'],
                            'date': row['DATE'],
                            'amount': row['AMOUNT'],
                            'status': row['STATUS']
                        }
                        playload['status'] = 'success'
                        playload['purchase_list'].append(purchase)
                        return playload
    except:
        playload['status'] = 'error'
        return playload


def get_purchase_by_id(pono: str, accId: str, addrId: str):
    """Get purchase by id
    
    Args: 
        pono(str): purchase id, accId(str): user id, addrId(str): address Id

    Returns:
        dict: status(success, error), purchase
    """
    playload = {'status': '', 'purchase': {}}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `purchase` WHERE `PONO` = %s"
                cursor.execute(sql,(pono))
                result = cursor.fetchone()
                if (len(result) == 0):
                    playload['status'] = 'none'
                    return playload
                else:
                    date = result['DATE']
                    amount = result['AMOUNT']
                    status = result['STATUS']
                    shipDate = result['SHIPDATE']
                    cancelBy = result['CANCELBY']
                    cancelDate = result['CANCELDATE']
                    sql = "SELECT PNAME FROM `account` WHERE `ACCID` = %s"
                    cursor.execute(sql, (accId))
                    account = cursor.fetchone()
                    accname = account['ACCNAME']
                    sql = "SELECT * FROM `address` WHERE `ADDRID` = %s"
                    cursor.execute(sql, (addrId))
                    address = cursor.fetchone()
                    order = get_order_by_pono(pono)['order_list']
                    if (status == 'shipped'):
                        playload['purchase'] = {
                            'pono': pono,
                            'date': date,
                            'accname': accname,
                            'address': address,
                            'amount': amount,
                            'status': status,
                            'shipDate': shipDate,
                            'order': order
                        }
                    elif(status == 'cancelled'):
                         playload['purchase'] = {
                            'pono': pono,
                            'date': date,
                            'accname': accname,
                            'address': address,
                            'amount': amount,
                            'status': status,
                            'cancelDate': cancelDate,
                            'cancelBy': cancelBy,
                            'order': order
                        }
                    else:
                        playload['purchase'] = {
                            'pono': pono,
                            'date': date,
                            'accname': accname,
                            'address': address,
                            'amount': amount,
                            'status': status,
                            'order': order
                        }
                        playload['status'] = 'success'
                        return playload
    except:
        playload['status'] = 'error'
        return playload                   


def get_order_by_pono(pono: str):
    """Get order by pono

    Args: 
        pono(str): purchase id

    Returns:
        dict: status(success, error), order_list
    """     
    playload = {'status': '', 'order_list': []}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT PID, PRICE, QUANTITY, SUBTOTAL FROM `order` WHERE `PONO` = %s"
                cursor.execute(sql, (pono))
                result = cursor.fetchall()
                for row in result:
                    pid = row['PID']
                    price = row['PRICE']
                    quantity = row['QUANTITY']
                    subtotal = row['SUBTOTOAL']
                    sql = "SELECT PNAME FROM `produce` WHERE `PID` = %s"
                    cursor.execute(sql,(pid))
                    pname = cursor.fetchone()
                    order = {
                        'pname': pname,
                        'quantity': quantity,
                        'price': price,
                        'subtotal': subtotal
                    }
                    playload['status'] = 'success'
                    playload['order_list'].append(order)
                    return playload
    except:
        playload['status'] = 'error'
        return playload
                    
                    





# @TODO: purchase all products in shopping cart list and clear shopping cart
# should create a 'purchase receipt' by the following methods

# @TODO: generate a 'purchase recepit' by method purchase all products in shopping cart list


if __name__ == '__main__':
    res = None
    # res = create_account("Steve", 'p1908326@ipm.edu.mo',
    #                      password='somepassword', accType='admin')
    # res = login_check("p1908326@ipm.edu.mo", password='newpassword')
    # res = create_product("iPhone 13", "Apple", "8899", "Phone",
    #                    "img/iphone.png", "img/iphone-2.png")
    # res = delete_account("p1908326@ipm.edu.mo", "somepassword")
    # res = update_password("p1908326@ipm.edu.mo", "somepassword", "newpassword")
    # res = get_products_by_name("iPhone")
    # res = update_product_price("9078f1ac-82db-461c-a6db-3b16ec6e6011", 6099)
    # res = delete_product("123")
    # res = add_product_to_cart(
    #    "11a45010-d203-438c-98ef-2ed2012b2eaf", 'c3f58d35-e6c1-4185-bd49-c99a9ae1f9fa', 1)
    # res = create_address('c3f58d35-e6c1-4185-bd49-c99a9ae1f9fa', '18740060111', 'Steve Yan', 'Macao SAR',
    #                     'China', 'Rua de Bruxelas, Nam On Gardon, Macao Polytechnic Institute Student Hostel')
    # res = get_user_address_list('c3f58d35-e6c1-4185-bd49-c99a9ae1f9fa')
    # res = delete_address('c5a498da-a01b-47c2-8475-b6546a84ad2a',
    #                     'c3f58d35-e6c1-4185-bd49-c99a9ae1f9fa')
    # res = delete_product_from_cart(
    #    'bea69416-d9a2-42b5-8323-bf2778093562', 'c3f58d35-e6c1-4185-bd49-c99a9ae1f9fa')
    # res = get_all_products_in_cart('c3f58d35-e6c1-4185-bd49-c99a9ae1f9fa')
    # res = check_out('c3f58d35-e6c1-4185-bd49-c99a9ae1f9fa')
    # res = update_product('11a45010-d203-438c-98ef-2ed2012b2eaf', 'iPhone 13 pro', 'Apple', '9899', 'Phone',
    #                      'img/iphone.png', 'img/iphone-2.png')
    # res = create_product('Nike Air Force 1 Mid 07 LV8', 'Nike', '819', 'Shoes',
    #                     '7e33824f-b8ce-460f-8387-c231c3e0c7b1.webp', '7e33824f-b8ce-460f-8387-c231c3e0c7b1.webp;8d56312f-79ac-4fb8-836e-0326817ddc1e.webp;7e33824f-b8ce-460f-8387-c231c3e0c7b1.webp')
    res = get_all_products()

    print(res)
