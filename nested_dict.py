# A simple program that imitates the admin panel of an online store

products = {}


def add():
    '''This function is going to add a new product(name and price) to "products" nested dictionary'''
    name = input('Please enter the name of the product\n')
    price_in = input('Please enter the price of the product\n')
    products[name] = {}
    products[name]["price"] = price_in
    

def new_atr():
    '''This fuction is going to add a new atribute to a certain product. Firts it asks for the name of the product
    and checks if such product exists'''
    product = input('Please enter the name of the product to which you want to add the attribute\n')
    if product in products:
        name = input('Please enter the name of the attribute\n')
        value = input('Please enter the value\n')
        products[product][name] = value
    else:
        print('No product was found')
        

def lookup():
    '''This function displays attributes of a certain product. First it checks if such product exits'''
    name = input("Please enter the name of the product\n")
    if name in products:
        for k,v in products[name].items():
            print(f'{k} --> {v}')
    else:
        print('No product was found')
            

def list_products():
    '''The following  function displays a names of all products'''
    for i in products:
        print(i)
        
        
while True:
    command = int(input('Please choose the action\n1) Add new Product\n2) Add new attribute\n3) Lookup a product\n4) List of products\n5) Exit\n'))
    if command == 1:
        add()
    elif command == 2:
        new_atr()
    elif command == 3:
        lookup()
    elif command == 4:
        list_products()
    elif command == 5:
        break
// test
