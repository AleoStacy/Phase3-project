# helpers.py
from models import Product, Customer, Order, SessionLocal
# Function to view a product by ID
def get_product():
    product_id = input('Enter the product ID: ').strip()
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        print(f"Product {product.id}: {product.name} - {product.description}, ${product.price}")
    else:
        print(f"Product with ID {product_id} not found.")
    db.close()

# Function to view a customer by ID
def get_customer():
    customer_id = input('Enter the customer ID: ').strip()
    db = SessionLocal()
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if customer:
        print(f"Customer {customer.id}: {customer.name} - {customer.email}")
    else:
        print(f"Customer with ID {customer_id} not found.")
    db.close()

# Function to create a new order
def create_order():
    customer_id = input('Enter the customer ID: ').strip()
    product_id = input('Enter the product ID: ').strip()
    quantity = int(input('Enter the quantity: ').strip())
    
    db = SessionLocal()
    order = Order(customer_id=customer_id, product_id=product_id, quantity=quantity)
    db.add(order)
    db.commit()
    print(f"Order created: Product {product_id} for Customer {customer_id}, Quantity: {quantity}")
    db.close()

# Function to list all orders
def list_orders():
    db = SessionLocal()
    orders = db.query(Order).all()
    if orders:
        for order in orders:
            print(f"Order {order.id}: Product {order.product_id}, Customer {order.customer_id}, Quantity {order.quantity}")
    else:
        print("No orders found.")
    db.close()

# Function to list all products
def list_products():
    db = SessionLocal()
    products = db.query(Product).all()
    if products:
        for product in products:
            print(f"Product {product.id}: {product.name} - {product.description}, ${product.price}")
    else:
        print("No products found.")
    db.close()

# Function to list all customers
def list_customers():
    db = SessionLocal()
    customers = db.query(Customer).all()
    if customers:
        for customer in customers:
            print(f"Customer {customer.id}: {customer.name} - {customer.email}")
    else:
        print("No customers found.")
    db.close()

# Function to update an order's quantity
def update_order():
    order_id = input('Enter the order ID to update: ').strip()
    db = SessionLocal()
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        new_quantity = int(input('Enter the new quantity: ').strip())
        order.quantity = new_quantity
        db.commit()
        print(f"Order {order_id} updated to quantity: {new_quantity}")
    else:
        print(f"Order with ID {order_id} not found.")
    db.close()

# Function to delete an order
def delete_order():
    order_id = input('Enter the order ID to delete: ').strip()
    db = SessionLocal()
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        db.delete(order)
        db.commit()
        print(f"Order {order_id} deleted successfully.")
    else:
        print(f"Order with ID {order_id} not found.")
    db.close()

