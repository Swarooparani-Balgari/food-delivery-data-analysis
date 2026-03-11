import pandas as pd

data = {
"Customer":["Rahul","Neha","Amit","Priya","Karan","Rahul","Neha","Amit","Priya","Rahul"],
"City":["Delhi","Mumbai","Bangalore","Delhi","Hyderabad","Mumbai","Delhi","Bangalore","Hyderabad","Delhi"],
"Category":["Indian","Italian","Fast Food","Indian","Indian","Japanese","Fast Food","Italian","Indian","Italian"],
"Quantity":[2,1,3,1,2,1,2,1,1,2],
"Price":[250,450,180,300,220,600,200,420,250,450],
"DeliveryFee":[40,50,35,40,45,60,40,50,45,50]
}

df = pd.DataFrame(data)

df["Revenue"] = (df["Quantity"] * df["Price"]) + df["DeliveryFee"]

print("Total Revenue:",df["Revenue"].sum())

print(df.groupby("City")["Revenue"].sum().sort_values(ascending=False))

print(df.groupby("Category")["Revenue"].sum().sort_values(ascending=False))

print(df.groupby("Customer")["Revenue"].sum().sort_values(ascending=False))

