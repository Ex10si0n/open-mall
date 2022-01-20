import settings
import pymysql.cursors
import uuid
import password_validator

connection = pymysql.connect(host=settings.db_host,
                             user=settings.db_user,
                             password=settings.db_password,
                             database=settings.database,
                             cursorclass=pymysql.cursors.DictCursor)

def test():
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `account` WHERE `email`=%s"
            cursor.execute(sql, ('p1908326@ipm.edu.mo',))
            result = cursor.fetchall()[0]
            print(result)

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
    ret = {'status': '', 'uuid': ''}
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `account` WHERE `email`=%s"
            cursor.execute(sql, (email,))
            result = cursor.fetchall()
            if (len(result) != 0):
                ret['status'] = 'email_exists'
                return ret
            sql = "INSERT INTO `account` (`ACCID`, `ACCNAME`, `HASHEDPASSWORD`, `EMAIL`, `ACCTYPE`) VALUES (%s, %s, %s, %s, %s)"
            accId = str(uuid.uuid4())
            cursor.execute(sql, (accId, accName, password_validator.hash(password, accId), email, accType))
            connection.commit()
            ret['status'] = 'success'
            ret['uuid'] = accId
            return ret
    ret['status'] = 'error'
    return ret

def login_check(email: str, password: str):
    """ Login check

    Args:
        email (str): user email
        password (str): user password

    Returns:
        dict: status, uuid, type
    """    
    ret = {'status': '', 'uuid': '', 'type': ''}
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `account` WHERE `email`=%s"
            cursor.execute(sql, (email,))
            result = cursor.fetchone()
            if (result is None):
                ret['status'] = 'account_not_registered'
                return ret
            given_hashed_password = password_validator.hash(password, result['ACCID'])
            if given_hashed_password == result['HASHEDPASSWORD']:
                ret['status'] = 'success'
                ret['uuid'] = result['ACCID']
                ret['type'] = result['ACCTYPE']
                return ret
            else:
                ret['status'] = 'invalid_password'
                return ret
    ret['status'] = 'error'
    return ret
    
if __name__ == '__main__':
    res = None
    # res = create_account("Steve", 'p1908326@ipm.edu.mo', password='somepassword', accType='admin')
    res = login_check("p1908326@ipm.edu.mo", password='somepassword')
    print(res)