# ShopSurfer Django Backend

![ShopSurfer Home Page](https://shopsurfer.s3.ap-south-1.amazonaws.com/screenshots/shopsurfer.png)

## Overview

This Django Rest Framework project serves as the backend for [ShopSurfer React application](https://github.com/nishantshetty92/shop-surfer-app). It provides a set of RESTful endpoints that allow users to interact with the application's resources, such as products, categories, user accounts, and orders. The API uses JSON Web Token (JWT) authentication to secure endpoints and manage user sessions.

## Features

- **User Authentication**: JWT authentication is implemented to allow secure user registration, login, and access to protected endpoints
- **Products & Categories**: Ability to categorize products and fetch products based on categories.
- **Cart Management**: Users can add to cart, update quantity for item, remove a product from cart and select/deselect item in cart
- **Checkout and Order Placement**: Users can add/update shipping addresses and place order for selected products
- **Admin Panel**: CRUD operations for managing products, categories and their relationship is handled by Django Admin.

## Demo

Please checkout the live application at [https://shopsurfer.netlify.app/](https://shopsurfer.netlify.app/)

## Technologies Used

- Django REST Framework
- PostgreSQL (Database)
- JWT Authentication System
- AWS S3

## Conclusion

As this is a personal project, I will be constantly improving on this and adding new features.

Any feedback and suggestions for improvements are really appreciated.
