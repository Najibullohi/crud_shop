import requests

def carts():
    response = requests.get("https://fakestoreapi.com/carts")
    if response.status_code == 200:
        products = response.json()
        return products

carts ()
print(carts())     