"""
Cheat sheet for basic queris in Django
"""
from models import * # Import all models used within scope

# (1) Returns all records from Customer table
customers = Customer.objects.all()

# (2) Returns first record from table
firstCustomer = Customer.objects.first()

# (3) Returns last record from table
lastCustomer = Customer.objects.last()

# (4) Returns single customer by name
customerByName = Customer.objects.get(name='BuBu')

# (5) Returns single customer by id
customerById = Customer.objects.get(id=4)

# (6) Returns all orders related to customer (firstCustomer)
firstCustomer.order_set.all()

# (7) Returns orders customer name: (Query parent model)
order = Order.objects.first()
parentName = order.customer.name

# (8) Returns products from products table with category value "Outdoor"
products = Product.objects.filter(category="Outdoor")

# (9) Order/Sort objects by id
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

# (10) Returns all products with tag of "Sports":
productFiltered = Product.objects.filter(tags__name = "Sports")

# (11) Bonus
productFiltered = Product.objects.filter(tags__name = "Sports")