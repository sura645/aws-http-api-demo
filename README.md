# 🚀 AWS HTTP API Demo (CRUD)

This project demonstrates a simple serverless API using:

* AWS Lambda
* API Gateway (HTTP API)
* Python

---

## 📌 Features

* GET → Fetch orders
* POST → Create order
* PUT → Update order
* DELETE → Delete order

---

## 🏗️ Architecture

Client → API Gateway → Lambda → (In-memory storage)

---

## 🧪 API Endpoints

### GET Orders

GET /orders

### Create Order

POST /orders

```json
{
  "id": "1",
  "item": "Book",
  "price": 200
}
```

### Update Order

PUT /orders

```json
{
  "id": "1",
  "item": "Laptop",
  "price": 50000
}
```

### Delete Order

DELETE /orders?id=1

---

## ⚠️ Note

Data is stored temporarily (in-memory).
Use DynamoDB for production.

---

## 📸 Screenshots

(Add API Gateway, Lambda, Postman screenshots here)

---

