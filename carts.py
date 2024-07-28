import requests

def get_all_carts():
    response = requests.get("https://fakestoreapi.com/carts")
    if response.status_code == 200:
        carts = response.json()
        return carts

def get_single_cart(cart_id):
    response = requests.get(f"https://fakestoreapi.com/carts/{cart_id}")
    if response.status_code == 200:
        carts = response.json()
        return carts

def get_sorted_carts(sort_type):
    response = requests.get(f"https://fakestoreapi.com/carts/{sort_type}")
    if response.status_code == 200:
        carts = response.json()
        return carts

def get_limited_carts(limit):
    response = requests.get(f"https://fakestoreapi.com/carts/{limit}")
    if response.status_code == 200:
        carts = response.json()
        return carts

print(get_all_carts())     