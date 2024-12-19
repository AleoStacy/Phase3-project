#!/usr/bin/env python3
from helpers import (
    get_product,
    get_customer,
    create_order,
    list_orders,
    list_products,
    list_customers,
    update_order,
    delete_order,
)

def main():
    print('Welcome to the CLI Application!')
    choice = None

    while choice != 'q':
        print('\nPlease choose an option:')
        print('1. View Product')
        print('2. View Customer')
        print('3. Create Order')
        print('4. List All Orders')
        print('5. List All Products')
        print('6. List All Customers')
        print('7. Update Order')
        print('8. Delete Order')
        print('q. Quit')

        choice = input('Enter your choice: ').strip()

        if choice == '1':
            get_product()
        elif choice == '2':
            get_customer()
        elif choice == '3':
            create_order()
        elif choice == '4':
            list_orders()
        elif choice == '5':
            list_products()
        elif choice == '6':
            list_customers()
        elif choice == '7':
            update_order()
        elif choice == '8':
            delete_order()
        elif choice == 'q':
            print('Thanks for using the CLI! Goodbye!')
        else:
            print('Invalid choice. Please try again.')

if __name__ == "__main__":
    main()
