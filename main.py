import categories_api,products_api,carts
from pprint import pprint

while True:
    print("Welcome to our Shop")
    categories = categories_api.get_all_category()
    formatted_categories = " | ".join(categories_api.get_all_category())
    pprint(f"Our categories: {formatted_categories}")
    print("#"*30)


    print("Choose an action")
    print("1. Receive products from the selected category")
    print("2. Get the list of all products")
    print("3. Get the list of carts")
    print("4. Exit")
    choice = int(input("Select an action : "))

    if choice == 1:
        category = input("Enter category : ")
        print(categories_api.get_specific_category(category_name=category))
        print("----------------------------------")
        print("----------------------------------")
        print("----------------------------------")


    elif choice == 2:
        print(products_api.get_all_products())
        print("----------------------------------")
        print("----------------------------------")
        print("----------------------------------")
    elif choice == 3:
        print(carts.get_all_carts)
        print("----------------------------------")
        print("----------------------------------")
        print("----------------------------------")
    else:
        print("Thank you for visiting")
        break
