from models import Product, Customer, Order, SessionLocal
from faker import Faker

# Initialized a Faker to generate fake data
fake = Faker()

# Created a database session
db = SessionLocal()

# Seed Products (generate 10 fake products)
for _ in range(10):
    product = Product(
        name=fake.word(),
        description=fake.sentence(),
        price=fake.random_number(digits=3),
        in_stock=fake.boolean()
    )
    db.add(product)

# Seed Customers (generate 5 fake customers with unique emails like 'alice@gmail.com')
for _ in range(5):
    first_name = fake.first_name().lower()  # Get first name and convert it to lowercase
    customer = Customer(
        name=fake.name(),
        email=f"{first_name}@gmail.com"  # Email corresponds to the first name
    )
    db.add(customer)

# Seed Orders (generate 20 fake orders)
for _ in range(20):
    order = Order(
        customer_id=fake.random_int(min=1, max=5),  # Assuming 5 customers are created
        product_id=fake.random_int(min=1, max=10),   # Assuming 10 products are created
        quantity=fake.random_int(min=1, max=5)
    )
    db.add(order)

# Commit the changes to the database
db.commit()

# Close the session
db.close()

print("Database seeded successfully with Faker data!")



