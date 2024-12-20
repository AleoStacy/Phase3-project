from models import Product, Customer, Order, SessionLocal
from faker import Faker

# Initialized a Faker instance to generate fake data
fake = Faker()

# Created a database session
db = SessionLocal()

# Seed Products
products = [
    {"name": "Laptop", "description": "A high-performance laptop for professionals.", "price": 85000},
    {"name": "Smartphone", "description": "A sleek smartphone with the latest features.", "price": 40000},
    {"name": "Headphones", "description": "Noise-canceling headphones for immersive sound.", "price":12000},
    {"name": "Coffee Maker", "description": "Brew fresh coffee every morning.", "price": 7500},
    {"name": "Gaming Console", "description": "Next-gen gaming experience.", "price": 60000},
    {"name": "Washing Machine", "description": "Efficient washing machine with multiple modes.", "price": 35000},
    {"name": "Refrigerator", "description": "Energy-efficient double-door fridge.", "price": 55000},
    {"name": "Microwave", "description": "Compact microwave with quick-cook settings.", "price": 10000},
    {"name": "Smartwatch", "description": "Stylish smartwatch with health tracking.", "price": 15000},
    {"name": "Bluetooth Speaker", "description": "Portable speaker with crystal-clear sound.", "price": 8000},
    {"name": "Smart Home Thermostat", "description": "Control your home temperature remotely.", "price": 3000},
    {"name": "Smart Home Door Lock", "description": "Secure your home doors with facial recognition.", "price": 2500},
    {"name": "Smart Home Motion Sensor", "description": "Monitor your home's security with a single device.", "price": 1000},
    {"name": "Smart Home Light Switch", "description": "Toggle your home lights with a single press.", "price": 500},
    {"name": "Smart Home Doorbell", "description": "Receive a notification when your home doorbell rings.", "price": 2000},
    {"name": "Smart Home Security Camera", "description": "Monitor your home's security with a single device.", "price": 15000},
    {"name": "Smart Home HVAC Thermostat", "description": "Control your home's HVAC system remotely.", "price": 3500},
    {"name": "Smart Home Humidifier", "description": "Monitor and control your home's humidity.", "price": 2000},
]

for product in products:
    db.add(Product(
        name=product["name"],
        description=product["description"],
        price=product["price"],
        in_stock=fake.boolean()
    ))

# Seed Test Customers
for _ in range(5):
    first_name = fake.first_name().lower()
    customer = Customer(
        name=fake.name(),
        email=f"{first_name}@gmail.com"
    )
    db.add(customer)

# Commit seeded data
db.commit()

# Interactive Order Creation
name = input("Enter your name: ")
email = input("Enter your email: ")

# Check if the customer exists
existing_customer = db.query(Customer).filter(Customer.email == email).first()

if not existing_customer:
    # Add the customer to the database
    new_customer = Customer(name=name, email=email)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)  # Refresh to access the new ID
    customer_id = new_customer.id
else:
    customer_id = existing_customer.id

# Create an order
product_id = int(input("Enter the product ID you want to order: "))
quantity = int(input("Enter the quantity: "))

new_order = Order(customer_id=customer_id, product_id=product_id, quantity=quantity)
db.add(new_order)
db.commit()

print(f"Order created successfully for {name}!")

# Close the session
db.close()
