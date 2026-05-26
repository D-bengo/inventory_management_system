from unittest.mock import patch
from openfoodfacts_service import get_product_by_barcode

@patch("requests.get")
def test_api(mock_get):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Organic Almond Milk",
            "brands": "Silk"
        }
    }

    result = get_product_by_barcode("123")

    assert result["product_name"] == "Organic Almond Milk"