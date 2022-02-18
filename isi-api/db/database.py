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


def get_address_by_id(addrId: str):
    """ get user's address by id

    Args:
        addrId (str): address id

    Returns:
        dict: status(success, error), address
    """
    playload = {'status': '', 'address': {}}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `address` WHERE `addrId`=%s"
                cursor.execute(sql, (addrId,))
                result = cursor.fetchone()
                if (result is None):
                    playload['status'] = 'error'
                    return playload
                playload['status'] = 'success'
                playload['address'] = result
                return playload
    except:
        playload['status'] = 'error'
        return playload


def get_user_address_list(accId: str):
    """ get user's address list

    Args:
        accId (str): user id

    Returns:
        dict: status(success, error), address list
    """
    playload = {'status': '', 'address_list': []}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `address` WHERE `ACCID`=%s"
                cursor.execute(sql, (accId,))
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
                cursor.execute(sql, (pName, brand, price,
                               pDesc, thumbnail, pic, pid))
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
        dict: status(success, duplicated, error), cartid
    """
    playload = {'status': '', 'cartid': ''}
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
                    playload['cartid'] = cartid
                    return playload
                else:
                    playload['status'] = 'duplicated'
                    return playload
    except:
        playload['status'] = 'error'
        return playload


def update_product_quantity_in_cart(pid: str, accId: str, quantity: int):
    """ Update product quantity in shopping cart

    Args:
        pid (str): product id
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
                sql = "UPDATE `shopping_cart` SET `QUANTITY` = %s WHERE `PID` = %s AND `ACCID` = %s"
                cursor.execute(sql, (quantity, pid, accId))
                connection.commit()
                playload['status'] = 'success'
                return playload
    except:
        playload['status'] = 'error'
        return playload


def delete_product_from_cart(pid: str, accId: str):
    """ Delete product from shopping cart list

    Args:
        pid (str): product id
        accId (str): user id

    Returns:
        dict: status(success, error)
    """
    playload = {'status': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "DELETE FROM `shopping_cart` WHERE `PID`=%s AND `ACCID`=%s"
                cursor.execute(sql, (pid, accId))
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
        dict: status(success, error), shopping cart list and total order amount
    """
    playload = {'status': '', 'shopping_cart_list': [], 'amount': 0}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `shopping_cart` WHERE `ACCID` = %s"
                cursor.execute(sql, (accId))
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
                        price = product['PRICE']
                        shopping_cart = {
                            'pid': pid,
                            'pname': product['PNAME'],
                            'price': price,
                            'quantity': quantity
                        }
                        playload['amount'] = playload['amount'] + quantity * price
                        playload['shopping_cart_list'].append(shopping_cart)
                    playload['status'] = 'success'
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
                cursor.execute(sql, (accId,))
                result = cursor.fetchall()
                if (len(result) == 0):
                    playload['status'] = 'none'
                    return playload
                else:
                    amount = 0
                    pono = str(uuid.uuid4())
                    sql = "INSERT INTO `purchase` (`PONO`, `ACCID`, `DATE`, `STATUS`, `AMOUNT`) VALUES (%s, %s, %s, %s, %s)"
                    today = date.today().strftime("%Y-%m-%d")
                    cursor.execute(
                        sql, (pono, accId, today, 'pending', 0))
                    connection.commit()
                    for row in result:
                        cartId = row['CARTID']
                        pid = row['PID']
                        quantity = row['QUANTITY']
                        sql = "SELECT PRICE FROM `product` WHERE `PID` = %s"
                        cursor.execute(sql, (pid))
                        product = cursor.fetchone()
                        price = product['PRICE']
                        subtotal = quantity * price
                        amount = amount + subtotal
                        sql = "INSERT INTO `order` (`PONO`, `PRICE`, `OID`, `PID`, `QUANTITY`, `SUBTOTAL`) VALUES (%s, %s, %s, %s, %s, %s)"
                        oid = str(uuid.uuid4())
                        print(sql % (pono, price, oid, pid, quantity, subtotal))
                        cursor.execute(
                            sql, (pono, price, oid, pid, quantity, subtotal))
                        connection.commit()
                        delete_product_from_cart(cartId, accId)
                    sql = "UPDATE `purchase` SET `AMOUNT` = %s WHERE `PONO` = %s"
                    today = date.today().strftime("%Y-%m-%d")
                    cursor.execute(
                        sql, (amount, pono))
                    connection.commit()
                    playload['status'] = 'success'
                    playload['PONO'] = pono
                    return playload
    except:
        playload['status'] = 'error'
        return playload


def get_all_purchase_of_customer(accId: str):
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
                cursor.execute(sql, (accId))
                result = cursor.fetchall()
                if (len(result) == 0):
                    playload['status'] = 'none'
                    return playload
                else:
                    for row in result:
                        purchase = {
                            'pono': row['PONO'],
                            'date': row['DATE'].strftime("%Y-%m-%d"),
                            'amount': row['AMOUNT'],
                            'status': row['STATUS']
                        }
                        playload['purchase_list'].append(purchase)
                    playload['status'] = 'success'
                    return playload
    except:
        playload['status'] = 'error'
        return playload


def get_purchase_by_status(accId: str, status: str):
    """Filter purchase by status

    Args: 
        accId(str): user id, status(str): pending/hold/shipped/cancelled

    Returns:
        dict: status(success, error), purchase_list
    """

    playload = {'status': '', 'purchase_list': []}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `purchase` WHERE `ACCID` = %s AND `STATUS` = %s"
                cursor.execute(sql, (accId, status))
                result = cursor.fetchall()
                if (len(result) == 0):
                    playload['status'] = 'none'
                    return playload
                else:
                    for row in result:
                        purchase = {
                            'pono': row['PONO'],
                            'accId': row['ACCID'],
                            'date': row['DATE'].strftime("%Y-%m-%d"),
                            'amount': row['AMOUNT'],
                            'status': row['STATUS']
                        }
                        playload['purchase_list'].append(purchase)
                    playload['status'] = 'success'
                    return playload
    except:
        playload['status'] = 'error'
        return playload


def customer_filter_purchase(accId: str, period: str):
    """For customer, filter purchase by status

    Args: 
        accId(str): user id, period(str): current/past

    Returns:
        dict: status(success, error), purchase_list
    """
    playload = {'status': '', 'purchase_list': [] }
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                if(period == 'current'):
                    result_pending = get_purchase_by_status(accId, 'pending')
                    result_hold = get_purchase_by_status(accId, 'hold')
                    if(result_pending['status'] == 'none' and result_hold['status'] == 'none'):
                        playload['status'] = 'none'
                        return playload
                    else:
                        for purchase in result_pending['purchase_list']:
                            playload['purchase_list'].append(purchase)
                        for purchase in result_hold['purchase_list']:
                            playload['purchase_list'].append(purchase)
                        playload['status'] = 'success'
                        return playload
                elif(period == 'past'):
                    result_shipped = get_purchase_by_status(accId, 'shipped')
                    result_cancelled = get_purchase_by_status(accId, 'cancelled')
                    if(result_shipped['status'] == 'none' and result_cancelled['status'] == 'none'):
                        playload['status'] = "none"
                        return playload
                    else:
                        for purchase in result_shipped['purchase_list']:
                            playload['purchase_list'].append(purchase)
                        for purchase in result_cancelled['purchase_list']:
                            playload['purchase_list'].append(purchase)
                        playload['status'] = 'success'
                        return playload
                else:
                    playload['status'] = 'error'
                    return playload
    except:
        playload['status'] = 'error'
        return playload


def vendor_filter_purchase(order_status: str):
    """For vendor, filter purchase by status

    Args: 
        order_status(str): pending/hold/past

    Returns:
        dict: status(success, error), purchase_list
    """
    playload = {'status': '', 'purchase_list': [] }
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                if(order_status == 'pending' or order_status == 'hold'):
                    sql = "SELECT * FROM `purchase` WHERE `STATUS` = %s"
                    cursor.execute(sql, (order_status))
                    result = cursor.fetchall()
                    if (len(result) == 0):
                        playload['status'] = 'none'
                        return playload
                    else:
                        for row in result:
                            purchase = {
                                'pono': row['PONO'],
                                'accId': row['ACCID'],
                                'date': row['DATE'].strftime("%Y-%m-%d"),
                                'amount': row['AMOUNT'],
                                'status': row['STATUS']
                            }
                            playload['purchase_list'].append(purchase)
                        playload['status'] = 'success'
                        return playload    
                elif(order_status == 'past'):
                    sql = "SELECT * FROM `purchase` WHERE `STATUS` = %s"
                    cursor.execute(sql, ('shipped'))
                    result_shipped = cursor.fetchall()
                    cursor.execute(sql, ('cancelled'))
                    result_cancelled = cursor.fetchall()
                    if (len(result_shipped) == 0 and len(result_cancelled) == 0):
                        playload['status'] = 'none'
                        return playload
                    else:
                        for row in result_shipped:
                            purchase = {
                                'pono': row['PONO'],
                                'accId': row['ACCID'],
                                'date': row['DATE'].strftime("%Y-%m-%d"),
                                'amount': row['AMOUNT'],
                                'status': row['STATUS']
                            }
                            playload['purchase_list'].append(purchase)
                        for row in result_cancelled:
                            purchase = {
                                'pono': row['PONO'],
                                'accId': row['ACCID'],
                                'date': row['DATE'].strftime("%Y-%m-%d"),
                                'amount': row['AMOUNT'],
                                'status': row['STATUS']
                            }
                            playload['purchase_list'].append(purchase)
                        playload['status'] = 'success'
                        return playload    
                   
                else:
                    playload['status'] = 'error'
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
                cursor.execute(sql, (pono))
                result = cursor.fetchone()
                if (len(result) == 0):
                    playload['status'] = 'none'
                    return playload
                else:
                    date = result['DATE'].strftime("%Y-%m-%d")
                    amount = result['AMOUNT']
                    status = result['STATUS']
                    shipDate = result['SHIPDATE'].strftime("%Y-%m-%d")
                    cancelBy = result['CANCELBY']
                    cancelDate = result['CANCELDATE'].strftime("%Y-%m-%d")
                    sql = "SELECT ACCNAME FROM `account` WHERE `ACCID` = %s"
                    cursor.execute(sql, (accId))
                    account = cursor.fetchone()
                    accName = account['ACCNAME']
                    sql = "SELECT * FROM `address` WHERE `ADDRID` = %s"
                    cursor.execute(sql, (addrId))
                    address = cursor.fetchone()
                    order = get_order_by_pono(pono)['order_list']
                    if (status == 'shipped'):
                        playload['purchase'] = {
                            'pono': pono,
                            'date': date,
                            'accName': accName,
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
                            'accName': accName,
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
                            'accName': accName,
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
                if (len(result) == 0):
                    playload['status'] = 'none'
                    return playload
                else:
                    for row in result:
                        pid = row['PID']
                        price = row['PRICE']
                        quantity = row['QUANTITY']
                        subtotal = row['SUBTOTAL']
                        sql = "SELECT PNAME FROM `product` WHERE `PID` = %s"
                        cursor.execute(sql, (pid))
                        name = cursor.fetchone()
                        pname = name['PNAME']
                        order = {
                            'pname': pname,
                            'quantity': quantity,
                            'price': price,
                            'subtotal': subtotal
                        }
                        playload['order_list'].append(order)
                    playload['status'] = 'success'
                    return playload
    except:
        playload['status'] = 'error'
        return playload


def update_status(pono: str, status: str):
    """Update status

    Args: 
        pono(str): purchase id, status(str): status of purchase

    Returns:
        dict: status(success, error)
    """
    playload = {'status': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "UPDATE `purchase` SET `STATUS` = %s WHERE `PONO` = %s"
                cursor.execute(sql, (status, pono))
                connection.commit()
                playload['status'] = 'success'
                return playload
    except:
        playload['status'] = 'error'
        return playload


def cancel_purchase (pono: str):
    """Cancel order

    Args: 
        pono(str): purchase id

    Returns:
        dict: status(success, error, forbidden)
    """
    playload = {'status': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT STATUS FROM `purchase` WHERE `PONO` = %s"
                cursor.execute(sql, (pono))
                result = cursor.fetchone()
                status = result['STATUS']
                if(status == 'pending' or status == 'hold'):
                    update_status(pono, 'cancelled')
                    playload['status'] = 'success'
                    return playload
                else:
                    playload['status'] = 'forbidden'
                    return playload
    except:
        playload['status'] = 'error'
        return playload


def ship_purchase(pono: str):
    """Ship order

    Args: 
        pono(str): purchase id

    Returns:
        dict: status(success, error, forbidden)
    """
    playload = {'status': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT STATUS FROM `purchase` WHERE `PONO` = %s"
                cursor.execute(sql, (pono))
                result = cursor.fetchone()
                status = result['STATUS']
                if(status == 'pending'):
                    update_status(pono, 'shipped')
                    playload['status'] = 'success'
                    return playload
                else:
                    playload['status'] = 'forbidden'
                    return playload
    except:
        playload['status'] = 'error'
        return playload


def hold_purchase(pono: str):
    """Hold order

    Args: 
        pono(str): purchase id

    Returns:
        dict: status(success, error, forbidden)
    """
    playload = {'status': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT STATUS FROM `purchase` WHERE `PONO` = %s"
                cursor.execute(sql, (pono))
                result = cursor.fetchone()
                status = result['STATUS']
                if(status == 'pending'):
                    update_status(pono, 'hold')
                    playload['status'] = 'success'
                    return playload
                else:
                    playload['status'] = 'forbidden'
                    return playload
    except:
        playload['status'] = 'error'
        return playload

def unhold_purchase(pono: str):
    """Unhold order

    Args: 
        pono(str): purchase id

    Returns:
        dict: status(success, error, forbidden)
    """
    playload = {'status': ''}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT STATUS FROM `purchase` WHERE `PONO` = %s"
                cursor.execute(sql, (pono))
                result = cursor.fetchone()
                status = result['STATUS']
                if(status == 'hold'):
                    update_status(pono, 'shipped')
                    playload['status'] = 'success'
                    return playload
                else:
                    playload['status'] = 'forbidden'
                    return playload
    except:
        playload['status'] = 'error'
        return playload


def get_all_purchase():
    """Get all purchase

    Args: 
        None

    Returns:
        dict: status(success, error), purchase_list
    """
    playload = {'status': '', 'purchase_list': []}
    try:
        connection = create_connection()
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `purchase` ORDER BY `DATE` DESC"
                cursor.execute(sql)
                result = cursor.fetchall()
                if (len(result) == 0):
                    playload['status'] = 'none'
                    return playload
                else:
                    for row in result:
                        pono = row['PONO']
                        date = row['DATE'].strftime("%Y-%m-%d")
                        accId = row['ACCID']
                        amount = row['AMOUNT']
                        status = row['STATUS']
                        sql = "SELECT ACCNAME FROM `account` WHERE `ACCID` = %s"
                        cursor.execute(sql, (accId))
                        name = cursor.fetchone()
                        accName = name['ACCNAME']
                        purchase = {
                            'pono': pono,
                            'date': date,
                            'accName': accName,
                            'amount': amount,
                            'status': status
                        }
                        playload['purchase_list'].append(purchase)
                    playload['status'] = 'success'
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
    # res = get_all_purchase_of_customer('c3f58d35-e6c1-4185-bd49-c99a9ae1f9fa')
    # res = get_purchase_by_status(
    #    'c3f58d35-e6c1-4185-bd49-c99a9ae1f9fa', 'pending')
    # res = get_purchase_by_id('0c09c90f-96f3-40ea-8e6d-b194525da7c3', 'c3f58d35-e6c1-4185-bd49-c99a9ae1f9fa', '98409f31-ee40-404c-b6c5-896c85e3878a')
    # res = update_status('0c09c90f-96f3-40ea-8e6d-b194525da7c3', 'cancelled')
    # res = update_product('11a45010-d203-438c-98ef-2ed2012b2eaf', 'iPhone 13 pro', 'Apple', '9899', 'Phone',
    #                      'img/iphone.png', 'img/iphone-2.png')
    # res = create_product('Nike Air Force 1 Mid 07 LV8', 'Nike', '819', 'Shoes',
    #                     '7e33824f-b8ce-460f-8387-c231c3e0c7b1.webp', '7e33824f-b8ce-460f-8387-c231c3e0c7b1.webp;8d56312f-79ac-4fb8-836e-0326817ddc1e.webp;7e33824f-b8ce-460f-8387-c231c3e0c7b1.webp')
    # res = get_all_purchase()
    # res = get_all_products()
    # res = get_all_products_in_cart('c3f58d35-e6c1-4185-bd49-c99a9ae1f9fa')
    # res = customer_filter_purchase('c3f58d35-e6c1-4185-bd49-c99a9ae1f9fa', 'current')
    # res = vendor_filter_purchase('past')
    # res = cancel_purchase('0c09c90f-96f3-40ea-8e6d-b194525da7c3')
    res = ship_purchase('cabc4448-08e7-4584-b952-a41af5356a09')

    print(res)
