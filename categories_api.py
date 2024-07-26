import requests

def get_all_category():
    response = requests.get("https://fakestoreapi.com/products/categories")
    if response.status_code == 200:
        products = response.json()
        return products

def get_specific_category():
    response = requests.get("https://fakestoreapi.com/products/category/jewelery")
    if response.status_code == 200:
        products = response.json()
        return products


print(get_specific_category())
