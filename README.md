# CRUD_SHOP
Project which is make zapros in Api service Fakeapi
choice = int(input("Enter command "))

if choice == 1:
    products = products_api.get_all_products()
    pprint(products)
