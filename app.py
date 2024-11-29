from flask import Flask, jsonify, request  

app = Flask(__name__)  

# In-memory storage for products  
products = []  

# Endpoint to create a new product  
@app.route('/products', methods=['POST'])  
def create_product():  
    data = request.get_json()  

    # Validate input data  
    if 'name' not in data or 'description' not in data or 'price' not in data:  
        return jsonify({'error': 'Invalid input. Name, description, and price are required.'}), 400  
    
    # Validate price  
    try:  
        price = float(data['price'])  
    except ValueError:  
        return jsonify({'error': 'Price must be a float'}), 400  

    # Create product dictionary and add it to the list  
    new_product = {  
        'name': data['name'],  
        'description': data['description'],  
        'price': price  
    }  
    products.append(new_product)  

    return jsonify({'message': 'Product created', 'product': new_product}), 201  

# Endpoint to retrieve all products  
@app.route('/products', methods=['GET'])  
def get_products():  
    return jsonify(products), 200  

if __name__ == '__main__':  
    app.run(debug=True)