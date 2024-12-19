from models import Product, Customer, Order, SessionLocal
from faker import Faker

# Initialize a Faker instance to generate fake data
fake = Faker()

# Create a database session
db = SessionLocal()

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

# came up with 5 fake customers with unique emails
for _ in range(5):
    first_name = fake.first_name().lower()
    customer = Customer(
        name=fake.name(),
        email=f"{first_name}@gmail.com"
    )
    db.add(customer)

# Came up with 20 fake orders
for _ in range(20):
    order = Order(
        customer_id=fake.random_int(min=1, max=5),
        product_id=fake.random_int(min=1, max=10),
        quantity=fake.random_int(min=1, max=5)
    )
    db.add(order)

# Commit the changes to the database
db.commit()

# Close the session
db.close()

print("Database seeded successfully with meaningful product data!")
