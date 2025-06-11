# Medical Shop Flask API

A RESTful API for managing users, products, and orders in a medical shop, built with Flask and SQLite.

## Features

- User registration, authentication, approval, update, and deletion
- Product management (add, view all, view specific)
- Order management (add order details, view all orders)
- SQLite database with tables for users, products, orders, sell history, and user stock

## Project Structure

```
addOperation.py
createTableOpration.py
delete.py
main.py
my_medicalShop.db
readOperation.py
updateOperation.py
```

## Setup

1. **Clone the repository**
2. **Install dependencies**
   ```sh
   pip install flask
   ```
3. **Run the application**
   ```sh
   python main.py
   ```
   The API will be available at `https://harsh01815.pythonanywhere.com/`.

## API Endpoints

### User Endpoints

- `POST /createUser`  
  Create a new user.

- `POST /login`  
  Authenticate a user.

- `GET /getAllUsers`  
  Get all users.

- `POST /getSpecificUser`  
  Get details of a specific user.

- `POST /approveUser`  
  Approve or disapprove a user.

- `PATCH /updateUserAllDetails`  
  Update user details.

- `DELETE /deleteSpecificUser`  
  Delete a user.

### Product Endpoints

- `POST /addProduct`  
  Add a new product.

- `GET /getAllProduct`  
  Get all products.

- `POST /getSpecificProduct`  
  Get details of a specific product.

### Order Endpoints

- `POST /addOrderDetails`  
  Add order details.

- `GET /getAllOrdersDetail`  
  Get all order details.

## Database

The database file `my_medicalShop.db` is created automatically. Table creation is handled by [`createTableOpration.py`](createTableOpration.py).

## Authors

- [Your Name]

## License

This project is licensed under the MIT License.
