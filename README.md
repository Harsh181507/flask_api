# 💊 Medical Shop Management API

A robust, modular, and extensible RESTful API for managing users, products, and orders in a medical shop. Built with **Python**, **Flask**, and **SQLite**, this project is designed for real-world use and as a learning resource for backend development, database design, and API best practices.

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Flask-2.x-green?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/SQLite-3.x-lightgrey?logo=sqlite" alt="SQLite">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License">
</p>

---

## 🚀 Features

- **User Management:** Registration, authentication, approval, update, and deletion
- **Product Management:** Add, view, and query products with inventory tracking
- **Order Management:** Place orders, view order history, and manage order details
- **Database Integrity:** Automatic table creation, UUID-based IDs, and relational structure
- **Error Handling:** Consistent, informative JSON error responses
- **Extensible Architecture:** Modular codebase for easy feature addition and maintenance

---

## 🗂️ Project Structure

```
flask_api/
│
├── addOperation.py           # Add users, products, and orders
├── createTableOpration.py    # Database schema and table creation
├── delete.py                 # Delete operations
├── main.py                   # Flask app and API endpoints
├── my_medicalShop.db         # SQLite database file (auto-generated)
├── readOperation.py          # Read/query operations
├── updateOperation.py        # Update operations
```

---

## 🛠️ Setup & Installation

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/medical-shop-api.git
cd medical-shop-api
```

### 2. Install Dependencies

```sh
pip install flask
```

### 3. Run the Application

```sh
python main.py
```
The API will be available at: [https://harsh01815.pythonanywhere.com/](https://harsh01815.pythonanywhere.com/)

---

## 📚 API Endpoints

### 👤 User Management

| Endpoint                | Method | Description                    | Body / Params                          |
|-------------------------|--------|--------------------------------|----------------------------------------|
| `/createUser`           | POST   | Register a new user            | `name`, `password`, `email`, `address`, `phoneNumber`, `pinCode` |
| `/login`                | POST   | Authenticate user              | `email`, `password`                    |
| `/getAllUsers`          | GET    | List all users                 | -                                      |
| `/getSpecificUser`      | POST   | Get user by ID                 | `user_id`                              |
| `/approveUser`          | POST   | Approve/disapprove user        | `user_id`, `isApprove`                 |
| `/updateUserAllDetails` | PATCH  | Update user details            | `user_id`, fields to update            |
| `/deleteSpecificUser`   | DELETE | Delete user by ID              | `userID`                               |

### 📦 Product Management

| Endpoint           | Method | Description            | Body / Params                  |
|--------------------|--------|------------------------|-------------------------------|
| `/addProduct`      | POST   | Add a new product      | `name`, `price`, `category`, `stock` |
| `/getAllProduct`   | GET    | List all products      | -                             |
| `/getSpecificProduct` | POST | Get product by ID      | `products_id`                 |

### 🛒 Order Management

| Endpoint             | Method | Description            | Body / Params                                      |
|----------------------|--------|------------------------|----------------------------------------------------|
| `/addOrderDetails`   | POST   | Place a new order      | `user_id`, `product_id`, `product_name`, `user_name`, `quantity`, `message`, `price`, `category` |
| `/getAllOrdersDetail`| GET    | List all orders        | -                                                  |

---

## 🗃️ Database Schema

### Users Table

| Column                   | Type         | Description                  |
|--------------------------|--------------|------------------------------|
| id                       | INTEGER      | Primary Key (Auto Increment) |
| user_id                  | VARCHAR(255) | Unique User ID (UUID)        |
| password                 | VARCHAR(255) | User password (hashed in production) |
| date_of_account_creation | DATE         | Account creation date        |
| isApproved               | BOOLEAN      | Approval status              |
| block                    | BOOLEAN      | Block status                 |
| name                     | VARCHAR(255) | User name                    |
| address                  | VARCHAR(255) | User address                 |
| email                    | VARCHAR(255) | User email                   |
| phone_number             | VARCHAR(255) | User phone number            |
| pin_code                 | VARCHAR(255) | User pin code                |

### Products Table

| Column      | Type         | Description                  |
|-------------|--------------|------------------------------|
| id          | INTEGER      | Primary Key (Auto Increment) |
| products_id | VARCHAR(255) | Unique Product ID (UUID)     |
| name        | VARCHAR(255) | Product name                 |
| price       | FLOAT        | Product price                |
| category    | VARCHAR(255) | Product category             |
| stock       | INTEGER      | Product stock                |

### Order_Details Table

| Column                  | Type         | Description                  |
|-------------------------|--------------|------------------------------|
| id                      | INTEGER      | Primary Key (Auto Increment) |
| order_id                | VARCHAR(255) | Unique Order ID (UUID)       |
| user_id                 | VARCHAR(255) | User ID                      |
| product_id              | VARCHAR(255) | Product ID                   |
| isApproved              | BOOLEAN      | Approval status              |
| quantity                | INT          | Quantity ordered             |
| date_of_order_creation  | DATE         | Order creation date          |
| price                   | FLOAT        | Product price                |
| total_amount            | FLOAT        | Total order amount           |
| product_name            | VARCHAR(255) | Product name                 |
| user_name               | VARCHAR(255) | User name                    |
| message                 | VARCHAR(255) | Order message                |
| category                | VARCHAR(255) | Product category             |

---

## 🧩 Code Structure & Module Overview

### `main.py`
- **Purpose:** Entry point for the Flask application. Registers all API endpoints and initializes the database.
- **Highlights:**  
  - Uses Flask's routing to map HTTP requests to Python functions.
  - Handles request parsing, validation, and response formatting.
  - Calls `createTables()` on startup to ensure all tables exist.

### `createTableOpration.py`
- **Purpose:** Defines and creates all necessary database tables using SQLite.
- **Highlights:**  
  - Ensures idempotent table creation with `CREATE TABLE IF NOT EXISTS`.
  - Can be extended for new tables as the application grows.

### `addOperation.py`
- **Purpose:** Contains functions to add users, products, and order details to the database.
- **Highlights:**  
  - Uses UUIDs for unique identifiers.
  - Handles date/time formatting and default values.
  - Returns IDs for further processing.

### `readOperation.py`
- **Purpose:** Provides functions to authenticate users and retrieve users, products, and orders.
- **Highlights:**  
  - Returns data as Python dictionaries/lists for easy JSON serialization.
  - Supports both bulk and specific queries.

### `updateOperation.py`
- **Purpose:** Functions for updating user approval status and user details.
- **Highlights:**  
  - Dynamic field updates using keyword arguments.
  - Ensures only valid fields are updated.

### `delete.py`
- **Purpose:** Handles deletion of users from the database.
- **Highlights:**  
  - Uses parameterized queries to prevent SQL injection.

---

## ⚠️ Error Handling & Best Practices

- **Consistent JSON Responses:** All endpoints return JSON with `message` and `status` fields for easy client-side handling.
- **Exception Handling:** Try-except blocks catch and return errors, preventing server crashes and aiding debugging.
- **Input Validation:** All required fields are checked before database operations.
- **Security Note:** Passwords are stored in plain text for demonstration. **In production, always hash passwords!**

---

## 🧑‍💻 Contributing

Contributions are welcome!  
- Fork the repository
- Create a new branch (`git checkout -b feature/your-feature`)
- Commit your changes (`git commit -am 'Add new feature'`)
- Push to the branch (`git push origin feature/your-feature`)
- Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## ℹ️ About

This API is designed to provide a robust backend for a medical shop management system. It demonstrates best practices in RESTful API design, modular Python programming, and SQLite integration. The codebase is easy to extend and suitable for both production use (with further enhancements) and educational purposes.

---

## 📞 Contact

For questions, suggestions, or support, please open an issue or contact [harsh.sshr@gmail.com](mailto:harsh.sshr@gmail.com).

---

<p align="center">
  <b>Made with ❤️ using Python & Flask</b>
</p>
