from functools import reduce
purchases = [
    ("c101","Anu","Laptop",55000,1),
    ("c102","rahul","mouse",800,2),
    ("C103", "Priya", "Mobile", 25000, 1),
    ("C104", "Arun", "Keyboard", 1500, 2),
    ("C105", "Meera", "Headphones", 3000, 3)
] 
calculate_total = lambda purchase: purchase[3]*purchase[4]

processed_purchases = list(
    map(
        lambda purchase:(
            purchase[0],purchase[1],purchase[2],purchase[3],purchase[4],calculate_total(purchase)
        ),
        purchases
    )
)
print("Processed Customer Purchase Records")
print("-----------------------------------")
list(map(lambda p : print(
    f"Customer ID:{p[0]},"
    f"Name:{p[1]},"
    f"Product:{p[2]},"
    f"Quantity: {p[4]},"
    f"Total: Rs{p[5]}"
),processed_purchases))

threshold = 10000
high_value_purchases = list(
    filter(lambda p :p[5] > threshold,processed_purchases)
)
print("\nHigh-Value Purchases")
print("----------------------")
list(map(
    lambda p : print(
        f"{p[1]} - {p[2]} - {p[5]}"
    ),
    high_value_purchases
))

total_sales = reduce(
    lambda total,purchase : total + purchase[5],
    processed_purchases,
    0
)

average_purchase = total_sales / len(processed_purchases)

print("\nPurchase Statistics")
print("---------------------")
print("Total Sales: Rs",total_sales)
print("Number of Purchases:",len(processed_purchases))
print("Average Purchase Value: Rs.", average_purchase)

print("Number of High-Value Purchases:", len(high_value_purchases))