import csv


# READ PRODCUTS CSV

products = []

csv_file_path = "/Users/mtereo/Desktop/crud_app/data/product.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)
        #print(row["id"], row["name"])


#menu = """

#Hi.

#Welcome to the prodcuts app.

#There are 100 products.

#Available operations: 'List', 'Show', 'Create', 'Update'

#Please choose an operation:

#""".format(len(products))

csv_file_path = "/Users/mtereo/Desktop/crud_app/data/product.csv"
with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)

#chosen_operation = input(menu)
#chosen_operation = chosen_operation.title()

# def list_products():
    #print("LISTING PRODUCTS")

# def show_products():
    #print("SHOWING A PRODUCT")

#def create_products():
    #print("CREATING A PRODUCT")

#def update_products():
    #print("UPDATING A PRODUCT")

#def destroy_products():
    #print("DESTROYING A PRODUCT")

# if chosen_operation.title() == "List": list_product()
# elif chosen_operation == "Show": show_products()
# elif chosen_operation == "Create": create_products()
# elif chosen_operation == "Update": update_products ()
# elif chosen_operation == "Destroy": destroy_products ()
# else: print("Unrecognized Operation. Please choose one of the following: 'List', 'Show', 'Create', 'Update', or 'Destroy'.")
