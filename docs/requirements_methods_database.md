### Requirements and their corresponding methods in database.py

| requirement | method                                                       |
| ----------- | ------------------------------------------------------------ |
| A1          | get_all_product()                                    return status, product_list |
| A2          | /                                                            |
| A3          | get_products_by_brand(brand: str)    return status, product_list |
| A4          | get_products_by_name(name: str)     return status, product_list |
| A5          | /                                                            |
| A6          | get_product_by_id(id: str)                     return status , product |
| A7          | Done                                                         |
| B1          | create_account(accName: str, email: str, password: str, accType: str)                        return status, uuid |
| B2          | login_check(email: str, password: str)  return status, uuid, type |
| B3          | update_password(email: str, old_password: str, new_password: str)  return status |
| B4          | /                                                            |
| B5          | Done                                                         |
| C1          | add_product_to_cart(pid: str, accid: str, quantity: int)    return status(success, error, duplicated), cartid |
| C2          | get_all_products_in_cart(accId: str)      return status, shopping_cart_list, amount |
| C3          | check_out(accId: str)      return status, PONO               |
| C4          | update_product_quantity_in_cart(pid: str, accId: str, quantity: int)    return status |
| C5          | delete_product_from_cart(pid: str, accId: str)  return status |
| C6          | add_product_to_cart(pid: str, accid: str, quantity: int)    return status(success, error, duplicated), cartid |
| D1          | get_all_purchase_of_customer(accId: str)     return status, purchase_list |
| D2          | customer_filter_purchase(accId: str, period: str)     (period: current/past)   return status, purchase_list |
| D3          | get_purchase_by_id(pono: str, accId: str, addrId: str)   return status, purchase |
| D4          | cancel_purchase (pono: str)  return status (success, error, forbidden) |
| E1          | Similar to A1, A2, A3, and A6                                |
| E2          | get_product_by_id(id: str)                     return status , product |
| E3          | create_product(pName: str, brand: str, price: float, pDesc: str, thumbnail: str, pic: str) return status, pid |
| E4          |                                                              |
| E5          | update_product(pid: str, pName: str, brand: str, price: float, pDesc: str, thumbnail: str, pic: str)     return status, pid |
| E6          |                                                              |
| F1          | get_all_purchase()    return status, purchase_list           |
| F2          | vendor_filter_purchase(order_status: str)    (order_status:pending/hold/past)         return status, purchase_list |
| F3          | **LACK OF A METHOD ** ship_purchase(pono: str) return status(success, error, forbidden) |
| F4          |                                                              |
| F5          | hold_purchase(pono: str)    return status(success, error, forbidden) |
| F6          | unhold_purchase(pono: str)   return status(success, error, forbidden) |
| F7          | cancel_purchase (pono: str)  return status (success, error, forbidden) |

