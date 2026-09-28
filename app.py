from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Favorites/Search History (CRUD requirement meet karne ke liye)
favorite_cities = [
    {"id": 1, "city": "Delhi", "temp": "28°C", "condition": "Sunny"},
    {"id": 2, "city": "Mumbai", "temp": "31°C", "condition": "Humid"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({"status": "Healthy", "service": "Weather Dashboard"}), 200

# READ
@app.route('/api/favorites', methods=['GET'])
def get_favorites():
    return jsonify(favorite_cities), 200

# CREATE
@app.route('/api/favorites', methods=['POST'])
def add_favorite():
    data = request.get_json() or {}
    city = data.get("city")
    if not city:
        return jsonify({"error": "City name is required"}), 400
    
    item = {
        "id": len(favorite_cities) + 1,
        "city": city,
        "temp": data.get("temp", "N/A"),
        "condition": data.get("condition", "Clear")
    }
    favorite_cities.append(item)
    return jsonify(item), 201

# DELETE
@app.route('/api/favorites/<int:item_id>', methods=['DELETE'])
def delete_favorite(item_id):
    global favorite_cities
    favorite_cities = [c for c in favorite_cities if c["id"] != item_id]
    return jsonify({"message": f"City {item_id} deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)