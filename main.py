import carts_api, categories_api, products_api

while True:
    print("Welcome to our Shop")
    categories = categories_api.get_all_category()
    formatted_categories = " | ".join(categories_api.get_all_category())
    print(f"Our categories: {formatted_categories}")
    print("#"*30)

    print("Choose an action")
    print("1. Receive products from the selected category")
    print("2. Get the list of all products")
    print("3. Get the list of carts")
    print("4. Exit")
    choice = int(input("Select an action : "))

    if choice == 1:
        category = input("Enter category : ")
        products = categories_api.get_specific_category(category)
        for product in products:
            print(f'{product["id"]}. {product["title"]}. Цена: {product["price"]}')
    elif choice == 2:
        products = products_api.get_all_products()
        for product in products:
            print(f'{product["id"]}. {product["title"]}. Price:{product["price"]}')
    elif choice == 3:
        products = carts_api.get_all_carts()
        for product in products:
            print(f'{product["id"]}. UserID: {product["userId"]}. Date:{product["date"]}')
    else:
        print("Thank you for visiting")
        break
    print("----------------------------------")
    print("----------------------------------")
    print("----------------------------------")
