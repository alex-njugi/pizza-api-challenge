### Pizza Restaurant API

A RESTful API for managing restaurants, pizzas, and their relationships. Built with Flask, SQLAlchemy and Flask-Migrate.

## Setup Instructions

# 1. Clone the Repository

git clone git@github.com:alex-njugi/pizza-api-challenge.git
cd pizza-api-challenge

# 2. Install Dependencies

pipenv install
pipenv shell

# 3. Set Environment Variable

export FLASK_APP=server/app.py

# 4. Run Migrations

flask db init
flask db migrate -m "Tables created"
flask db upgrade

# 5. Seed the Database

python -m server.seed


### API Endpoints

## GET /restaurants

Returns all restaurants.

**Response:**

[
  {
    "id": 1,
    "name": "Luigi's",
    "address": "123 Pasta Lane"
  }
]


## GET /restaurants/<id>

Returns a specific restaurant and its pizzas.

**Response:**

{
  "id": 1,
  "name": "Luigi's",
  "address": "123 Pasta Lane",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Dough, Tomato Sauce, Mozzarella"
    }
  ]
}


## DELETE /restaurants/<id>

Deletes a restaurant and all its associated data.

**Success:** `204 No Content`
**Error:**

{ "error": "Restaurant not found" }


## GET /pizzas

Returns all pizzas.

**Response:**

[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Mozzarella"
  }
]


## POST /restaurant\_pizzas

Creates a new restaurant-pizza connection.

**Request:**

{
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 2
}

**Response:**

{
  "id": 3,
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Mozzarella"
  },
  "restaurant": {
    "id": 2,
    "name": "Kiki's Pizza",
    "address": "456 Cheesy Blvd"
  }
}

**Error (validation):**

{ "errors": ["Price must be between 1 and 30"] }


## Validations

* `RestaurantPizza.price` must be between **1 and 30**


## Testing with Postman

1. Open Postman
2. Import the file `challenge-1-pizzas.postman_collection.json`
3. Make sure your Flask server is running on `http://localhost:5000`
4. Test all routes


## Tech Stack

* Python
* Flask
* Flask SQLAlchemy
* Flask Migrate
* SQLite (local DB)

