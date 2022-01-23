import settings
import pymysql.cursors
import uuid
import password_validator

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
        dict: status, uuid
    """    
    playload = {'status': '', 'uuid': ''}
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
            cursor.execute(sql, (accId, accName, password_validator.hash(password, accId), email, accType))
            connection.commit()
            playload['status'] = 'success'
            playload['uuid'] = accId
            return playload
    playload['status'] = 'error'
    return playload

def login_check(email: str, password: str):
    """ Login check

    Args:
        email (str): user email
        password (str): user password

    Returns:
        dict: status, uuid, type
    """    
    playload = {'status': '', 'uuid': '', 'type': ''}
    connection = create_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `account` WHERE `email`=%s"
            cursor.execute(sql, (email,))
            result = cursor.fetchone()
            if (result is None):
                playload['status'] = 'account_not_registered'
                return playload
            given_hashed_password = password_validator.hash(password, result['ACCID'])
            if given_hashed_password == result['HASHEDPASSWORD']:
                playload['status'] = 'success'
                playload['uuid'] = result['ACCID']
                playload['type'] = result['ACCTYPE']
                return playload
            else:
                playload['status'] = 'invalid_password'
                return playload
    playload['status'] = 'error'
    return playload

def delete_account(email: str, password: str): 
    """ delete a user by email permanently

    Args:
        email (str): user email
        password (str): user password

    Returns:
        dict: status
    """    
    playload = {'status': ''}
    connection = create_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `account` WHERE `email`=%s"
            cursor.execute(sql, (email,))
            result = cursor.fetchone()
            if (result is None):
                playload['status'] = 'account_not_registered'
                return playload
            given_hashed_password = password_validator.hash(password, result['ACCID'])
            if given_hashed_password == result['HASHEDPASSWORD']:
                sql = "DELETE FROM `account` WHERE `email`=%s"
                cursor.execute(sql, (email,))
                connection.commit()
                playload['status'] = 'success'
                return playload
            else:
                playload['status'] = 'authentication_error'
                return playload
    playload['status'] = 'error'
    return playload


# @TODO: update user password

# @TODO: create user's address
    
# @TODO: get user's address by addressID

# @TODO: update user's address

# @TODO: delete user's address

def create_product(pName: str, brand: str, price: float, pDesc: str, thumbnail: str, pic: str, category: str):
    """ Create a new product

    Args:
        pName (str): product name
        brand (str): product brand
        price (float): product price  @TODO: currency calculation
        pDesc (str): product description
        thumbnail (str): thumbnail image
        pic (str): product detail image
        category (str): product category

    Returns:
        dict: status, pid
    """    
    playload = {'status': '', 'pid': ''}
    connection = create_connection()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `product` (`PID`, `PNAME`, `BRAND`, `PRICE`, `PDESC`, `THUMBNAIL`, `PIC`, `CATALOG`)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            pid = str(uuid.uuid4())
            cursor.execute(sql, (pid, pName, brand, price, pDesc, thumbnail, pic, category))
            connection.commit()
            playload['status'] = 'success'
            playload['pid'] = pid
            return playload
    playload['status'] = 'error'
    return playload


# @TODO: get products by name

# @TODO: update product

# @TODO: delete product

# @TODO: add product to shopping cart list

# @TODO: delete certain product from shopping cart list

# @TODO: clear shopping cart list without purchasing

# @TODO: purchase all products in shopping cart list and clear shopping cart
# should create a 'purchase receipt' by the following methods

# @TODO: generate a 'puechase recepit' by method purchase all products in shopping cart list

if __name__ == '__main__':
    res = None
    create = 1
    if create == 1:
        res = create_account("Steve", 'p1908326@ipm.edu.mo', password='somepassword', accType='admin')
        create_account("Jane", 'p1908345@ipm.edu.mo', password='somepassword', accType='admin')
    else:
        res = login_check("p1908326@ipm.edu.mo", password='somepassword')
    # res = create_product("iPhone 13 pro", "Apple", "10899", "Phone", "img/iphone.png", "img/iphone-2.png", "Smart Phone")
    # res = delete_account("p1908326@ipm.edu.mo", "somepassword")
    print(res)