# Міні проєкт----------------------------------------
# Написати програму для зберігання та керування 
# списком покупок.

# Основна ідея полягає в тому, щоб програма зберігала дані 
# про список продуктів та їх кількість у текстовому файлі. 
# Кожен рядок в файлі містить інформацію про один продукт 
# та його кількість у форматі "назва продукту, кількість".

# Після запуску програми користувач може додавати нові 
# продукти до списку та їх кількість, переглядати список, 
# редагувати наявну інформацію, видаляти продукти зі списку 
# та зберігати зміни у файлі.


def read_shopping_list(file_path):
    shopping = {
    'lemon': 5,
    'pumpkin': 12,
    'sugar': 2,
    'tea': 2,
    'flour': 1,
    'onion': 7,
    'garlic': 9,
    'potatoes': 30,
    }
    with open(file_path, 'r') as f:
        for line in f:
            product, product_num = line.strip().split(',')
            shopping[product] = int(product_num)
    return shopping

def write_shopping_list(file_path, shopping):
    with open(file_path, 'w') as f:
        for product, product_num in shopping.items():
            f.write(f'{product},{product_num}\n')


def plus(file_path, shopping):
    product = input('Enter product name: ')
    product_num = int(input(f'Enter number of {product} - '))
    shopping.setdefault(product, product_num)
    print('Added')

    write_shopping_list(file_path, shopping)

def revision(shopping):
    for product, product_num in shopping.items():
        print(f'\\\\   {product},{product_num}')
    

def edit(file_path, shopping):
    with open(file_path, 'w') as file:
        what_doing = int(input('What are we editing?\n1. Name\n2. Number\n> '))
        product = input('Enter product name: ')
        
        if product in shopping:
            if what_doing == 1:
                new_name = input('Enter new product name: ')
                shopping[new_name] = shopping.pop(product)
                print(f"Product '{product}' has been renamed to '{new_name}'.")
            elif what_doing == 2:
                new_quantity = int(input('Enter new quantity: '))
                shopping[product] = new_quantity
                print(f"Quantity of '{product}' has been updated to {new_quantity}.")
            else:
                print("Invalid option")
        else:
            print('Product not found')

    write_shopping_list(file_path, shopping)

def removal(file_path, shopping):
    with open(file_path, 'w') as file:
        product = input('Enter product name: ')
        if product in shopping:
            del shopping[product]
            print('Deleted')
        else:
            print('Not founded')
    return shopping

    write_shopping_list(file_path, shopping)
    
def main():
    file_path = 'shopping.txt'
    shopping = read_shopping_list(file_path)
    while True:
        diya = int(input('Enter the number of action:\n1. Plus product\n2. Revision shopping\n3. Edit shopping list\n4. Delete the product\n5. Exit\n> '))
        if diya == 1:
            plus(file_path, shopping)
        elif diya == 2:
            revision(shopping)
        elif diya == 3:
            edit(file_path, shopping)
        elif diya == 4:
            removal(file_path, shopping)
        elif diya == 5:
            break

main()
