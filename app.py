from flask import Flask, jsonify, request
from data.inventory_data import inventory
from openfoodfacts_service import get_product_by_barcode

app = Flask(__name__)

# GET all inventory
@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

# GET single item
@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):

    item = next((i for i in inventory if i["id"] == item_id), None)

    if item:
        return jsonify(item)

    return jsonify({"error": "Item not found"}), 404

# POST item
@app.route('/inventory', methods=['POST'])
def add_item():

    data = request.json

    new_item = {
        "id": len(inventory) + 1,
        "barcode": data["barcode"],
        "product_name": data["product_name"],
        "brand": data["brand"],
        "price": data["price"],
        "stock": data["stock"],
        "ingredients": data.get("ingredients", "")
    }

    inventory.append(new_item)

    return jsonify({
        "message": "Item added successfully",
        "item": new_item
    }), 201

# PATCH item
@app.route('/inventory/<int:item_id>', methods=['PATCH'])
def update_item(item_id):

    item = next((i for i in inventory if i["id"] == item_id), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.json

    item["price"] = data.get("price", item["price"])
    item["stock"] = data.get("stock", item["stock"])

    return jsonify({
        "message": "Item updated",
        "item": item
    })

# DELETE item
@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):

    item = next((i for i in inventory if i["id"] == item_id), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    inventory.remove(item)

    return jsonify({
        "message": "Item deleted"
    })

# Search OpenFoodFacts
@app.route('/search', methods=['GET'])
def search_product():

    barcode = request.args.get("barcode")

    product = get_product_by_barcode(barcode)

    return jsonify(product)

if __name__ == '__main__':
    app.run(debug=True)