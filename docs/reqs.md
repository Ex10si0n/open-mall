# Functional Requirements

| Subject                                                      | Database                | Web  | API   | Integration |
| ------------------------------------------------------------ | ----------------------- | ---- | ----- | ----------- |
| **(A1)** A customer may **browse
products** in a list of products. The list shows basic information of products, including product name, brand, price and a thumbnail image. Each product belongs to one of the pre-defined brands. (You can also use category instead of brand). | :ballot_box_with_check: | W5   | W3    | W5          |
| **(A2)** The product list supports **
paging**. The customer can navigate the product list by ‘page up’, ‘page down’ and jumping to a specific page. Paging works properly after applying a filter or sorting as listed below. | :ballot_box_with_check: | W7   | W7    | W7          |
| **(A3)** The customer can **filter** the product list **by
brand**. They can also list products of all brands. | :ballot_box_with_check: |      | W3    |             |
| **(A4)** The customer may filter the product list by **searching
keywords** in the product name. This function work correctly with the brand filter. | :ballot_box_with_check: | W7   | W3    | W7          |
| **(A5)** The customer may **sort** the product list **by
price**. | :ballot_box_with_check: |      |       |             |
| **(A6)** The customer may select a product in the product list to go to the product detail page. The **product detail
page** shows information for one product, which includes the product name, brand, price and a thumbnail image. In addition, the product detail page also shows detail description as a list of at least two properties. For example, the product detail page for a book may show authors, ISBN, publisher, release date and number of pages. | :ballot_box_with_check: | W3   | W3    | W3          |
| **(A7)** The product detail page supports display of **one or more detailed
photographs** of the selected product. | :ballot_box_with_check: | W3   | W3    | W3          |
| **(B1)** A customer may **register a new
account**. They have to provide full name, email address, password and shipping address. After registration, the user is logged in automatically. | :ballot_box_with_check: | W5   | W2 W3 | W5          |
| **(B2)** A customer may **log in** and **log
out**, and the interface shows the name of the current user. The product list and product detail page are accessible to customers without login. On the other hand, the shopping cart and purchase tracking are only accessible after login. | :ballot_box_with_check: | W3   | W2    | W5          |
| **(B3)** The customer can **change
password**. There is strength requirement for password. The password should contain at least 6 characters, in which there must be at least one digit and one capital letter. | :ballot_box_with_check: | W5   | W2    | W5          |
| **(
B4)** If a customer tries to add a product to the shopping cart on the product detail page without first logging in, the system **
redirects** the user **to the login
page**. After successful login, the system redirects the user back to the original product detail page. | :ballot_box_with_check: |      |       |             |
| **(B5)** The server only saves **hash
values** of customers’ passwords. Passwords are never saved in plain text in the server. | :ballot_box_with_check: | W5   | W1    | W5          |
| **(C1)** The customer **adds a
product** to his/her shopping cart by clicking a button in the product detail page. The quantity to buy is assumed to be 1. The items in shopping cart are persisted across user sessions. Next time the customer logs in, they can still see the items in the shopping cart. | :ballot_box_with_check: | W4   | W3    | W4          |
| **(C2)** The customer can **list the
products** in his/her shopping cart in a shopping cart page. In this page, the entry for each product shows the product name, price and the quantity to buy. The page also shows the total order amount (i.e. how much the customer has to pay in total) in the shopping cart. The customer can click an item in the shopping cart to go to the product detail page of the entry. | :ballot_box_with_check: | W3   | W3    | W4          |
| **(C3)** The customer can press a button in the shopping cart page to **check
out** all items in the shopping cart. This action creates a purchase order with a newly allocated unique P.O. number, and clears the content of the cart. After checkout, the system shows the purchase order detail page of the newly created purchase order. *(
refer to requirement D3)*. | :ballot_box_with_check: | W3   | W3    | W5          |
| **(C4)** The shopping cart page allows the customer to **change the
quantity** of an item. This allows the customer to order more than one piece of a product (e.g. buy two copies of a book). | :ballot_box_with_check: | W3   | W3    | W4          |
| **(C5)** The customer can **remove an
item** from the shopping cart. | :ballot_box_with_check: | W3   | W3    | W4          |
| **(C6)** If the customer adds a **duplicate
product** to the shopping cart, theapplication will give a warning message and does not change the content of the shopping cart. | :ballot_box_with_check: | W4   | W4    | W4          |
| **(D1)** The **purchase tracking
page** lists the purchase orders that the customer has placed. This page shows the following for each purchase order: the P.O. number, the purchase date, the total order amount and the purchase order status. The purchase orders are displayed in reverse chronological order of purchase date. When the customer clicks an entry in the list, they can see the detail in a purchase order detail page. | :ballot_box_with_check: | W5   | W3    | W5          |
| **(
D2)** The customer can filter the list of purchase orders in two ways. First, the page only shows ‘current purchases’ with status ‘pending’ and ‘hold’. Second, the page only shows ‘past purchases’ with status ‘shipped’ and ‘cancelled’. | :ballot_box_with_check: |      | W3    |             |
| **(D3)** The **purchase order detail
page** shows the P.O. number, the purchase date, the customer name, the shipping address, the total order amount and the purchase order status. If the order is shipped, this page shows the shipment date. If the order is cancelled, the page shows the order cancel date and who (customer or vendor) cancelled the order. The page also includes, for each product in the purchase order, the product name, the quantity, the unit price and the subtotal. | :ballot_box_with_check: | W6   | W3    | W6          |
| **(D4)** Before a purchase order is shipped, the customer can **cancel the
order**. This can be done by clicking a button in the purchase order detail page. This action will change the status of the purchase order to ‘cancelled’. Note that this action is only available for purchase orders in the status ‘pending’ or ‘hold’. | :ballot_box_with_check: |      | W4    |             |
| **(E1)** The vendor may **browse the product catalog** in an interface similar to product list for customers. *(Refer
to requirements A1, A2, A3 and
A6)*. The vendor is not a customer, and no shopping cart or ‘add to cart’ button should be shown. | :ballot_box_with_check: |      | W3    |             |
| **(
E2)** The vendor can find products by searching keywords in product names. They can also find a specific product by entering a unique product ID. | :ballot_box_with_check: |      | W3    |             |
| **(E3)** The vendor may **add a new
product** to the catalog. The vendor enters basic information of the product, including product name, brand, price and a thumbnail image. They can enter detail information of the new product as a list of properties. *(
Refer to requirement A6*) | :ballot_box_with_check: |      | W2 W3 |             |
| (E4) In addition to the thumbnail image, the vendor can **upload 1 to 4 detailed
photographs** for a product. These photos are usually of higher resolution and are displayed in the product detail page in a user-friendly interface. *(
Refer to requirement A7)* | :ballot_box_with_check: |      |       |             |
| **(E5)** The vendor can **edit
information** of a product in a product detail page. They can change the product name and product brand. They can also change detail information as a list of properties. *(
Refer to requirement E3).* | :ballot_box_with_check: |      | W3    |             |
| **(
E6)** The vendor can change the thumbnail and detail photos for a product. They can add or remove photos. | :ballot_box_with_check: |      | W3    |             |
| **(F1)** The **purchase order list
page** lists purchase orders received by the application. It shows the P.O. numbers, purchase dates, customer names, total order amounts and purchase order status. The purchase orders are sorted in descending order of purchase date (i.e. newest first). The vendor can click an entry to open a purchase order processing page. | :ballot_box_with_check: | W7   | W3    | W7          |
| **(
F2)** The vendor can filter the purchase order list in three ways. They can show only the ‘pending orders’ (with status ‘pending’). They can show only the ‘orders on hold’ (with status ‘hold’). Finally, the vendor can select to show ‘past orders’ (with status ‘shipped’ or ‘cancelled’). | :ballot_box_with_check: | W7   | W3    | W7          |
| **(F3)** The **purchase order processing page** shows similar information as the purchase order detail page *(refer to
requirement D3)*. In addition, the vendor can click a button to **ship a purchase
order**. This action changes the status of the purchase order from ‘pending’ to ‘shipped’ and starts the shipping process. | :ballot_box_with_check: | W7   | W7    | W7          |
| **(
F4)** The vendor can enter a P.O. number to view and process a specific purchase order. | :ballot_box_with_check: | W7   | W7    | W7          |
| **(F5)** In the purchase order processing page, the vendor can click a button to **hold a purchase
order**. This is useful, for example, if some product in the purchase order is temporarily out-of-stock. This action is only available when the status of the purchase order is ‘pending’, and this action changes the status to ‘hold’. | :ballot_box_with_check: | W7   | W4    | W7          |
| **(F6)** In the purchase order processing page, the vendor can click a button to **unhold and ship a purchase
order**. This action changes the status of the purchase order from ‘hold’ to ‘shipped’ and starts the shipping process. | :ballot_box_with_check: | W7   | W4    | W7          |
| **(F7)** In the purchase order processing page, the vendor can click a button to **cancel a purchase
order**. This is useful, for example, to inform the customer that the ordered products are no longer available. This action is only available for purchase orders in the status ‘pending’ or ‘hold’. This action changes the status of the purchase order to ‘cancelled’. | :ballot_box_with_check: | W7   | W4    | W7          |
| **(
Z0)** Develop a mobile app as the frontend of the system. The mobile app should communicate with the server backend through a Web API. You have to design and implement both the frontend and the backend. | :ballot_box_with_check: | W6   |       |             |
|                                                              |                         |      |       |             |
|                                                              |                         |      |       |             |
|                                                              |                         |      |       |             |

