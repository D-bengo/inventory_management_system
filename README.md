#  Inventory Management System (Flask + OpenFoodFacts API)

A RESTful Inventory Management System built with Flask that allows administrators to manage products, integrate external product data from OpenFoodFacts, and interact using both API endpoints and a CLI tool.

---

#  Features

- Full CRUD operations (Create, Read, Update, Delete)
- REST API built with Flask
- External API integration (OpenFoodFacts)
- CLI-based interaction tool
- In-memory database (Python list)
- Unit testing with pytest
- Clean modular code structure

---

#  Tech Stack

- Python 3
- Flask
- Requests
- Pytest
- OpenFoodFacts API

---

#  Project Structure
inventory_management_system/
│
├── app.py # Main Flask application
├── cli.py # Command-line interface
├── openfoodfacts_service.py # External API integration logic
├── data/
│ └── inventory_data.py # Mock database (list of dictionaries)
│
├── test_app.py # API tests
├── test_openfoodfacts.py # External API tests (mocked)
├── requirements.txt
└── README.md


---

#  Installation & Setup

## 1. Clone the repository

```bash
git clone https://github.com/<your-username>/inventory_management_system.git
cd inventory_management_system

2. Install dependencies
pipenv install flask
pipenv install requests

3. Run the Flask server
python3 app.py
- Server will run at:
http://127.0.0.1:5000

#  API ENDPOINTS

## 1. Get all inventory items
```http
GET /inventory
