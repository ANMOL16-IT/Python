
class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display_details(self):
        print("Name:", self.name)
        print("Phone:", self.phone)


class Customer(User):
    def __init__(self, name, phone, address):
        super().__init__(name, phone)
        self.address = address
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)
        print(self.name, "placed an order.")

    def calculate_discount(self, amount):
        return 0


class PremiumCustomer(Customer):
    def calculate_discount(self, amount):
    
        return amount * 0.10

    def display_details(self):
        super().display_details()
        print("Address:", self.address)
        print("Membership: Premium")

class DeliveryPartner(User):
    def __init__(self, name, phone, partner_id):
        super().__init__(name, phone)
        self.partner_id = partner_id
        self.available = True

    def display_details(self):
        super().display_details()
        print("Partner ID:", self.partner_id)

class Restaurant:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display_details(self):
        print("Restaurant:", self.name)
        print("Location:", self.location)


class Order:
    def __init__(self, order_id, customer, restaurant, items, amount):
        self.order_id = order_id
        self.customer = customer
        self.restaurant = restaurant
        self.items = items
        self.amount = amount
        self.delivery_partner = None

    def assign_delivery(self, partner):
        if partner.available:
            self.delivery_partner = partner
            partner.available = False
            print("Delivery partner assigned:", partner.name)
        else:
            print("Delivery partner is not available.")

    def generate_bill(self):
        discount = self.customer.calculate_discount(self.amount)
        final_amount = self.amount - discount

        print("\n----- BILL -----")
        print("Order ID:", self.order_id)
        print("Customer:", self.customer.name)
        print("Restaurant:", self.restaurant.name)
        print("Amount: ₹", self.amount)
        print("Discount: ₹", discount)
        print("Final Amount: ₹", final_amount)

        if self.delivery_partner:
            print("Delivery Partner:", self.delivery_partner.name)
        else:
            print("Delivery Partner: Not Assigned")




customer1 = Customer("Rahul", "9876543210", "Bangalore")
customer2 = PremiumCustomer("Anmol", "9876543211", "Bangalore")


restaurant = Restaurant("Pizza House", "Electronic City")


partner = DeliveryPartner("Ravi", "9876543212", "DP101")


print("CUSTOMER DETAILS")
customer2.display_details()

print("\nRESTAURANT DETAILS")
restaurant.display_details()

print("\nDELIVERY PARTNER DETAILS")
partner.display_details()


order1 = Order(
    101,
    customer2,
    restaurant,
    ["Pizza", "Cold Drink"],
    800
)


customer2.place_order(order1)


order1.assign_delivery(partner)


order1.generate_bill()