import requests

def get_all_category():
    response = requests.get("https://fakestoreapi.com/products/categories")
    if response.status_code == 200:
        products = response.json()
        return products

def get_specific_category(category_name):
    response = requests.get(f"https://fakestoreapi.com/products/category/{category_name}")
    if response.status_code == 200:
        products = response.json()
        return products


print(get_all_category())
