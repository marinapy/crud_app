import csv

#READ PRODCUTS CSV

products = []

csv_file_path = "/Users/mtereo/Desktop/crud_app/data/product.csv"
headers = ["id", "name", "aisle", "department", "price"]
user_input_headers = [header for header in headers if header != "id"]

def get_product_id(product): return int(product["id"])

def auto_incremented_id():
    product_ids = map(get_product_id, products)
    return max(product_ids) + 1

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for ordered_dict in reader:
        products.append(dict(ordered_dict))
        #print(row["id"], row["name"])

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)

menu = """

Hello.

Welcome to the products app!

There are {20} products.

Available operations: 'List', 'Show', 'Create', 'Update', 'Destroy'

Please choose an operation:

"""

chosen_operation = input(menu)
chosen_operation = chosen_operation.title()

def list_products():
    print("LISTING PRODUCTS")
    for product in products:
        print(" + Product #" + str(product["id"]) + ": " + product["name"])

def show_products():
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("SHOWING PRODUCT", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product)

def create_products():
    print("OK. PLEASE PROVIDE THE PRODUCT'S INFORMATION...")
    product = {"id": auto_incremented_id() }
    for header in user_input_headers:
        product[header] = input("The '{0}' is: ".format(header))
    products.append(product)
    print("CREATING PRODUCT", product)

def update_products():
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("OK. PLEASE PROVIDE THE PRODUCT'S INFORMATION...")
        for header in user_input_headers:
            product[header] = input("Change '{0}' from '{1}' to: ".format(header, product[header]))
        print("UPDATING PRODUCT HERE", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)

def destroy_products():
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("DESTROYING PRODUCT HERE", product)
        del products[products.index(product)]
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)

if chosen_operation.title() == "List": list_products()
elif chosen_operation == "Show": show_products()
elif chosen_operation == "Create": create_products()
elif chosen_operation == "Update": update_products()
elif chosen_operation == "Destroy": destroy_products()
else: print("Unrecognized Operation. Please choose one of the following: 'List', 'Show', 'Create', 'Update', or 'Destroy'.")
