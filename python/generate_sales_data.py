import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

NUM_ROWS = 100000

data = []

sales_channels = ["Online", "Distributor", "Hospital Direct", "Retail Pharmacy"]
payment_types = ["Cash", "Credit", "Insurance", "UPI"]
customer_types = ["New", "Returning"]

for sale_id in range(1, NUM_ROWS + 1):
    quantity = random.randint(1, 500)
    unit_price = random.randint(100, 5000)
    discount = round(random.uniform(0, 25), 2)

    revenue = quantity * unit_price
    profit = revenue * random.uniform(0.15, 0.40)

    data.append({
        "Sale_ID": sale_id,
        "Doctor_ID": random.randint(1, 5),
        "Hospital_ID": random.randint(1, 5),
        "Product_ID": random.randint(1, 5),
        "Region_ID": random.randint(1, 5),
        "Time_ID": random.randint(1, 5),
        "Quantity_Sold": quantity,
        "Revenue": round(revenue, 2),
        "Unit_Price": unit_price,
        "Discount": discount,
        "Profit": round(profit, 2),
        "Sales_Channel": random.choice(sales_channels),
        "Payment_Type": random.choice(payment_types),
        "Customer_Type": random.choice(customer_types)
    })

df = pd.DataFrame(data)

df.to_csv("healthcare_sales_100k.csv", index=False)

print("Generated 100,000 records successfully!")