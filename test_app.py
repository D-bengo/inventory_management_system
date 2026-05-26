from app import app

client = app.test_client()

def test_get_inventory():

    response = client.get('/inventory')

    assert response.status_code == 200

def test_add_item():

    response = client.post('/inventory', json={
        "barcode": "123",
        "product_name": "Test Product",
        "brand": "Test Brand",
        "price": 5,
        "stock": 10
    })

    assert response.status_code == 201