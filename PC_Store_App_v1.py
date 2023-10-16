from tkinter import Button, Label, Tk, Entry, Text
from datetime import datetime
# from ClientGen import generate_test_client
# from faker import Faker

app = Tk()
app.title('PC Components Store')
product_report_text = Text(app, height=10, width=50)
product_id_entry = None
name_entry = None
manufacturer_entry = None
category_entry = None
price_entry = None
stock_entry = None

MAIN_MENU = """
1. Products
2. Clients
3. Transactions
4. Reports
X. Exit
"""


PRODUCTS_MENU = """
1. Add
2. Remove
3. Update
4. Display all
x. Go Back
"""


CLIENTS_MENU = """
1. Add
2. Remove
3. Update
4. Display all
x. Go Back
"""


TRANSACTIONS_MENU = """
1. Add
2. Remove
3. Update
4. Display all
x. Go Back
"""


products = {
    1: {
        'name': 'CPU',
        'manufacturer': 'Intel',
        'category': 'Processor',
        'price': 299.99,
        'stock': 50
    },
    2: {
        'name': 'GPU',
        'manufacturer': 'NVIDIA',
        'category': 'Graphics Card',
        'price': 699.99,
        'stock': 30
    },
    3: {
        'name': 'RAM',
        'manufacturer': 'Corsair',
        'category': 'Memory',
        'price': 99.99,
        'stock': 100
    },
    4: {
        'name': 'SSD',
        'manufacturer': 'Samsung',
        'category': 'Storage',
        'price': 149.99,
        'stock': 80
    },
}


clients = {
    1: {
        'last_name': 'Nutiu',
        'first_name': 'Adrian',
        'date_of_birth': '09/09/1999',
        'email': 'adrian.nutiu@test.com'
    },
    2: {
        'last_name': 'Zaharie',
        'first_name': 'Ioana',
        'date_of_birth': '07/01/2000',
        'email': 'ioana.zaharie@test.com'
    },
    3: {
        'last_name': 'Kolozsi',
        'first_name': 'Erik',
        'date_of_birth': '25/08/1993',
        'email': 'erik.kolozsi@test.com'
    },
}

transactions = {
    1: {
        'product_id': 1,
        'client_id': 1,
        'quantity': 2,
        'date': '2023-09-19',
    },
    2: {
        'product_id': 2,
        'client_id': 2,
        'quantity': 1,
        'date': '2023-05-18',
    },
    3: {
        'product_id': 3,
        'client_id': 3,
        'quantity': 4,
        'date': '2023-07-18',
    },
    4: {
        'product_id': 4,
        'client_id': 3,
        'quantity': 10,
        'date': '2022-07-18',
    },

}


def add_product():
    product_id = int(input('Please provide a product_id: '))
    name = input('Please provide a name: ')
    manufacturer = input('Please provide a manufacturer: ')
    category = input('Please provide a category: ')
    price = float(input('Please provide a price: '))
    stock = int(input('Please provide a stock: '))
    product_info = {
        'name': name,
        'manufacturer': manufacturer,
        'category': category,
        'price': price,
        'stock': stock
    }
    products[product_id] = product_info
    print(f'Added {name} to the products.')


def add_clients():
    client_id = int(input('Please provide a client_id: '))
    first_name = input('Please provide a first name: ')
    last_name = input('Please provide a last name: ')
    date_of_birth = input('Please provide a date of birth (DD/MM/YYYY): ')
    email = input('Please provide an email: ')
    client_info = {
        'first_name': first_name,
        'last_name': last_name,
        'date_of_birth': date_of_birth,
        'email': email
    }
    clients[client_id] = client_info
    print(f'Added {first_name} {last_name} to the products.')


def add_transaction():
    transaction_id = int(input('Please provide a transaction_id: '))
    product_id = int(input('Please provide a product_id: '))
    client_id = int(input('Please provide a client_id: '))
    quantity = int(input('Please provide a quantity: '))
    date = input('Please provide a date (YYYY-MM-DD): ')

    transaction_info = {
        'product_id': product_id,
        'client_id': client_id,
        'quantity': quantity,
        'date': date,
    }

    transactions[transaction_id] = transaction_info
    print(f'Added transaction with ID {transaction_id} to the transactions.')


def generate_product_report():
    print("-----||| Product Report |||-----")
    for product_id, product_info in products.items():
        print(f"Product ID: {product_id}")
        print(f"Name: {product_info['name']}")
        print(f"Manufacturer: {product_info['manufacturer']}")
        print(f"Category: {product_info['category']}")
        print(f"Price: ${product_info['price']:.2f}")
        print(f"Stock: {product_info['stock']} units")
        print("--------------------------")


def generate_client_report():
    print("-----||| Client Report |||-----")
    total_age = 0
    youngest_age = float('inf')
    oldest_age = 0

    for client_id, client_info in clients.items():
        print(f"Client ID: {client_id}")
        print(f"First Name: {client_info['first_name']}")
        print(f"Last Name: {client_info['last_name']}")
        print(f"Date of Birth: {client_info['date_of_birth']}")
        print(f"Email: {client_info['email']}")
        print("-------------------------")

        age = calculate_age(client_info['date_of_birth'])
        total_age += age
        youngest_age = min(youngest_age, age)
        oldest_age = max(oldest_age, age)

    average_age = total_age / len(clients)
    print(f"Average Client Age: {average_age:.2f} years")
    print(f"Youngest Client: {youngest_age} years old")
    print(f"Oldest Client: {oldest_age} years old")

    upcoming = upcoming_birthdays()
    if upcoming:
        print("Upcoming Birthdays:")
        for client_info in upcoming:
            print(f"{client_info['first_name']} {client_info['last_name']} - {client_info['date_of_birth']}")


def generate_transaction_report():
    print("-----||| Transaction Report |||-----")
    product_count = {}
    product_quantities = {}
    category_count = {}
    low_stock_products = []
    most_bought_item = None
    most_bought_quantity = 0
    top_product_revenue = {}
    top_client_revenue = {}
    most_expensive_order = None
    most_expensive_order_amount = 0

    for transaction_id, transaction_info in transactions.items():
        product_id = transaction_info['product_id']
        client_id = transaction_info['client_id']
        quantity = transaction_info['quantity']
        date = transaction_info['date']
        product = products[product_id]


        product_count[product_id] = product_count.get(product_id, 0) + 1
        product_quantities[product_id] = product_quantities.get(product_id, 0) + quantity


        category_count[product['category']] = category_count.get(product['category'], 0) + 1


        if product['stock'] < 10:
            low_stock_products.append(product['name'])


        if quantity > most_bought_quantity:
            most_bought_quantity = quantity
            most_bought_item = product['name']


        price = product['price']
        top_product_revenue[product_id] = top_product_revenue.get(product_id, 0) + price * quantity
        top_client_revenue[client_id] = top_client_revenue.get(client_id, 0) + price * quantity


        order_amount = price * quantity
        if order_amount > most_expensive_order_amount:
            most_expensive_order_amount = order_amount
            most_expensive_order = transaction_id

    print_top("Top 5 Manufacturers (by number of products)", product_count, products)
    print_top("Top 5 Categories (by number of products)", category_count)
    print("Products Low on Stock:", *low_stock_products)
    print(f"Most Bought Item:\n{most_bought_item} - {most_bought_quantity} units")
    print_top("Top 5 Revenue Bringers (by products)", top_product_revenue, products)
    print_top("Top 5 Revenue Bringers (by clients)", top_client_revenue, clients, 'first_name', 'last_name')
    print(f"Most Expensive Order:\nTransaction ID: {most_expensive_order} - ${most_expensive_order_amount:.2f}")

def print_top(title, data, reference=None, *keys):
    sorted_data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True)[:5])
    print(title)
    for key, value in sorted_data.items():
        if reference is not None:
            ref_data = reference[key]
            formatted_key = " ".join(ref_data[key] for key in keys)
            print(f"{formatted_key} - {value} {'products' if 'product' in title.lower() else 'units'}")




def calculate_age(date_of_birth):
    birth_date = datetime.strptime(date_of_birth, '%d/%m/%Y')
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def upcoming_birthdays():
    today = datetime.today()
    upcoming = []
    for client_id, client_info in clients.items():
        birth_date = datetime.strptime(client_info['date_of_birth'], '%d/%m/%Y')
        if today.month == birth_date.month and today.day < birth_date.day:
            upcoming.append(client_info)
    return upcoming

# GUI using tkinter

def add_product_tkinter():
    product_id = int(product_id_entry.get())
    name = name_entry.get()
    manufacturer = manufacturer_entry.get()
    category = category_entry.get()
    price = float(price_entry.get())
    stock = int(stock_entry.get())
    product_info = {
        'name': name,
        'manufacturer': manufacturer,
        'category': category,
        'price': price,
        'stock': stock
    }
    products[product_id] = product_info
    print(f'Added {name} to the products.')
    generate_product_report_tkinter()

def generate_product_report_tkinter():
    product_report_text.delete(1.0, 'end')
    product_report_text.insert('end', "-----||| Product Report |||-----\n")
    for product_id, product_info in products.items():
        product_report_text.insert('end', f"Product ID: {product_id}\n")
        product_report_text.insert('end', f"Name: {product_info['name']}\n")
        product_report_text.insert('end', f"Manufacturer: {product_info['manufacturer']}\n")
        product_report_text.insert('end', f"Category: {product_info['category']}\n")
        product_report_text.insert('end', f"Price: ${product_info['price']:.2f}\n")
        product_report_text.insert('end', f"Stock: {product_info['stock']} units\n")
        product_report_text.insert('end', "--------------------------\n")

def load_menu():
    app.destroy()
    app.__init__()
    app.title('PC Components Store')

    Label(app, text='Product ID: ').grid(row=0)
    Label(app, text='Name: ').grid(row=1)
    Label(app, text='Manufacturer: ').grid(row=2)
    Label(app, text='Category: ').grid(row=3)
    Label(app, text='Price: ').grid(row=4)
    Label(app, text='Stock: ').grid(row=5)

    product_id_entry = Entry(app)
    product_id_entry.grid(row=0, column=1)
    name_entry = Entry(app)
    name_entry.grid(row=1, column=1)
    manufacturer_entry = Entry(app)
    manufacturer_entry.grid(row=2, column=1)
    category_entry = Entry(app)
    category_entry.grid(row=3, column=1)
    price_entry = Entry(app)
    price_entry.grid(row=4, column=1)
    stock_entry = Entry(app)
    stock_entry.grid(row=5, column=1)

    Button(app, text='Add Product', width=100, command=add_product_tkinter).grid(row=6, column=0, columnspan=2)
    Button(app, text='Back', width=100, command=load_menu).grid(row=7, column=0, columnspan=2)

    product_report_text = Text(app, height=10, width=50)
    product_report_text.grid(row=8, column=0, columnspan=2)

    generate_product_report_tkinter()

while True:
    print(MAIN_MENU)

    option = input('Select an option from the menu: ').lower()

    match option:
        case '1':
            display_second_menu = True
            while display_second_menu:
                print(PRODUCTS_MENU)
                option = input('Select an option from the product menu: ').lower()

                match option:
                    case '1':
                        add_product()
                    case '2':
                        print('Remove')
                    case '3':
                        print('Update')
                    case '4':
                        print(products)
                    case 'x':
                        print('Back')
                        display_second_menu = False
                    case _:
                        print('No such option!')
        case '2':
            display_second_menu = True
            while display_second_menu:
                print(CLIENTS_MENU)
                option = input('Select an option from the clients menu: ').lower()

                match option:
                    case '1':
                        add_clients()
                    case '2':
                        print('Remove')
                    case '3':
                        print('Update')
                    case '4':
                        print(clients)
                    case 'x':
                        print('Back')
                        display_second_menu = False
                    case _:
                        print('No such option!')
        case '3':
            display_second_menu = True
            while display_second_menu:
                print(TRANSACTIONS_MENU)
                option = input('Select an option from the transactions menu: ').lower()

                match option:
                    case '1':
                        add_transaction()
                    case '2':
                        print('Remove')
                    case '3':
                        print('Update')
                    case '4':
                        print(add_transaction)
                    case 'x':
                        print('Back')
                        display_second_menu = False
                    case _:
                        print('No such option!')
        case '4':
            generate_product_report()
            generate_client_report()
            generate_transaction_report()
        case 'x':
            print('Exiting')
            break
        case _:
            print('No such option!')
             
app.mainloop()

