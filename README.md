## Introduction

This project is a web app on browsers and iOS providing a convenient online shopping experience for both customers and vendors which covers many functions such as browsing and maintaining the product catalog, placing and processing purchase orders, etc.

This is a group project completed by five people (Zhongbo Yan, Yajing Liu, Yi Wang, Zhuojun Yu, and Minghuang Hong). It is for the class COMP321 Information System Implementation. 

## Major Techniques and Tools Used

- **Frontend**: TypeScript, Tailwind CSS, Vue.js 3.0
- **Backend**: Python, FastAPI, Nginx, MariaDB
- **iOS**: SwiftUI, WebKit WebView

## Functions

- For customers:
  - About products: browse products in a list, page, filter the product list, search product, sort product, and show product details. 
  - About account management: register a new account, log in and log out, and change password.
  - About shopping cart: add a product to shopping cart, list all products in shopping cart, check out, and remove an item.
  - About purchase tracking: list all purchase orders that the customer has placed, filter the purchase order, show purchase details and cancel the order
- For vendors:
  - About product catalog maintenance: browse the product catalog, add a new product, and edit product.
  - About purchase order processing: list all purchase orders, filter orders, show purchase order details, ship a purchase order, hold a purchase order, unhold and ship a purchase order, and cancel a purchase order.

## Outcomes

### Demo Video

[Demo video](https://www.youtube.com/watch?v=GXnfV49RIu4)

### Customer - Home Page

The following image shows the home page of our project. 

![Home Page](https://drive.google.com/uc?id=1SgSWygfvXlqahTCnydnp37VzHMffBoLP)

### Customer - Register, Log in and Log out

When users want to login, they can press the login button in the bottom navigation of home page. Then they can see the login page. If they do not have an account, they can press the link "Sign up here" to create an account. On the register page, there are two steps - inputting users' basic information and adding users' address. When users successfully register, the system will automatically help users to log in and jump to the account management page.

![Login](https://drive.google.com/uc?id=1MD3gnzKKrcT-OebGmf-YK4EQ5LyUnFEN)

![Register page](https://drive.google.com/uc?id=1fHlu7cTIybQGy75SMOCciffaDZ1Q39mk)

![Adding address page](https://drive.google.com/uc?id=1n5ay1ecGuFlbnO7mF0-tNkvBJi93uF3J)

![Account Management](https://drive.google.com/uc?id=1INhjh2Tlg7tsvyPM29ch4G0-g0oXWBni)

After registering or login, the home page shows the user's name and the navigation bar is changed.

![Home page after login](https://drive.google.com/uc?id=1mrHKXnbdQS6SDDxzzm0ybDz-_-3jyR2R)

### Customer - Product **L**ist with Paging, **S**earching and **Fi**ltering

The user opens the Open Mall and sees a waterfall content list of products. Each product will display some basic information in the form of a card view. 

![Home Page](https://drive.google.com/uc?id=1SgSWygfvXlqahTCnydnp37VzHMffBoLP)

Paging function is shown in the bottom right corner of the home page. User can jump to particular pages by pushing buttons or inputting page number.

![Paging](https://drive.google.com/uc?id=11GsGLSsIMxvjFWNuz7K1y06Ap9rAvs0f)

Users can enter products' key words directly in search bar. Besides, they can also find favoured products by filtering products by brand and sort products by price.

![Filter, search bar and sort tool](https://drive.google.com/uc?id=1G-zQ3YniEGtRMSXHHZk-TIJGCxzQ-fe5)

### Customer - Product Detail Page

After finding the product, customer can go to the Product Detail page by clicking on the products. On this page, more detailed information about products is shown. 

There is an orange button on the bottom of the product – “Add to the shopping cart”. Users can press this bottom to add the product to the shopping cart after they are login. 

![Add to the shopping cart successfully](https://drive.google.com/uc?id=1vGbhp7M-PlpAsyVRm9qpwTw5_cx5nc0q)

### Customer - Shopping Cart

After users have finished browsing and selecting, the shopping cart function will be provided for them to check out. On the shopping cart page, users can list the products in their shopping cart. Users can click on items in the shopping cart to go to the product detail page of entries. User can also remove the item or change the quantity of an item. Users can press the button “Checkout” to check out all items in the shopping cart. 

![Shopping Cart Page](https://drive.google.com/uc?id=1n-9JiyEaeRJjlV1UmDCUsEA6iXrwdHeA)

After clicking the “Checkout” button, the system will create an order. After checking the content of the order, if there is no error about the content, users can click the “Pay” button to pay for the order. If there is an error in the content, the user can click “Go Back” to check the shopping cart again.

![Order detail page](https://drive.google.com/uc?id=192gIZl_-HmTumf8bkVnYaNLTzwq2hk3b)

Once paying is finished, the system will create a purchase order and clears the content of the cart. Then the system will show the purchase order detail page of the newly created purchase order.

![Purchase detail page](https://drive.google.com/uc?id=1PIMmbtqXesDj98OGNqn-yHlk6VDC3hv6)

### Customer - Purchase Tracking

Users can trace the processing status of the order on the purchase tracking page. The purchase tracking page lists the purchase orders that the user has placed. The purchase orders are displayed in reverse chronological order of purchase date. When the user clicks an entry in the list, they can see the detail in a purchase order detail page.

![Purchase list](https://drive.google.com/uc?id=1QbTWcFtZz6K6RT9Th4iW7y5juC-t0chZ)

Before a purchase order is shipped, the customer can cancel the order. This can be done by clicking

a button on the purchase order detail page.

![Purchase detail page](https://drive.google.com/uc?id=1PIMmbtqXesDj98OGNqn-yHlk6VDC3hv6)

### Vendor - Vendor Dashboard

The vendor can maintain product catalogue in the shopping mall and process purchase orders from cus- tomers as well.

![Vendor Dashboard](https://drive.google.com/uc?id=1C1vjTG61ms2zwTqGWoMSiDZZGkqxOTiS)

### Vendor - Product Catalog Management

Vendor can create a new products.

![Create Product](https://drive.google.com/uc?id=1wqsG7I-9_8xDC6HdmqE0C38Fp2HE_UJu)

![Create products](https://drive.google.com/uc?id=1xr8ciIT6Uwe00kcStGwqzO_MefV5OhkU)

Vendor can also edit an existing product.

![Edit an existing products](https://drive.google.com/uc?id=13Uf6zQVJS97xrW4Pt6P3NiShUFUYzVJk)

### Vendor - Product Delivery Management

Vendor can view all orders, and modify the status of orders. When an order is in pending status, it can be delivered if it has been shipped successfully or be changed into “hold” if the product is temporarily out-of-stock. When the desired product of an order held by the vendor is in stock, it can then be delivered. Each order that has not been shipped can be marked as cancelled either by the user or the vendor. 

![Order management page](https://drive.google.com/uc?id=1qunz_dnByf4n4l3kmZ5zyYkpHxavPGL0)

![Pending order](https://drive.google.com/uc?id=1FzD8SXBDnJpSv8uvJ3euEJT0AE4fQPZI)

![Hold order](https://drive.google.com/uc?id=1r160qRa-3R8278ANyXlGcX8psEeofUGl)

![Cancel by users](https://drive.google.com/uc?id=1libbl_BLw9U5Hbdats4LKlw_wG9Dkbvu)

![Cancel by vendor](https://drive.google.com/uc?id=101sImr2ZiGJEXDX2uIoOi172CK7g4vkF)

![Ship order](https://drive.google.com/uc?id=1nU7EO5AsnLWnsRwTyGrC8t-rDT3w6wj6)

### Mobile Application

A hybrid IOS software of the OpenMall project has been developed for Apple users.

<img src="https://drive.google.com/uc?id=1ItzF-Pj0nfN7TAhf_9QrtWbqoUpRKHG7" alt="Desktop" style="zoom: 25%;" />

The mobile application can communicate with the server backend through a Web API as the web applica- tion. Moreover, the UI layouts are consistent with the UI layouts in the web application. The consistency between the mobile application and the web application is in order to reduce the learning cost of users to use the mobile application.

Then the following screen captures demonstrate how our mobile application works.

Customer:

![Customer view](https://drive.google.com/uc?id=1t40Y1a5-Pfor4kBV6nMnp1PNrLCH65DM)

Vendor:

![Vendor View](https://drive.google.com/uc?id=1QPzP6rcfj4EyWu32yzD7F10OqPTqD1nA)

## Report

More information about design and implementation can be found in the [report](https://drive.google.com/file/d/1sMp9dkTE86Ocr1mfu8MmbVMNzTMibFX6/view?usp=sharing).
