import requests  

API_URL = 'http://127.0.0.1:5000/products'  

def add_product(name, description, price):  
    response = requests.post(API_URL, json={'name': name, 'description': description, 'price': price})  
    if response.status_code == 201:  
        print('Product created:', response.json())  
    else:  
        print('Failed to create product:', response.json())  

def get_products():  
    response = requests.get(API_URL)  
    if response.status_code == 200:  
        print('Product list:', response.json())  
    else:  
        print('Failed to retrieve products:', response.json())  

if __name__ == '__main__':  
    add_product('Sample Product', 'This is a sample product.', 19.99)  

  
    get_products()