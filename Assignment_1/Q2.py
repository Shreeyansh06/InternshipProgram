#Customer name (string)
#o Product price (float)
#o Is the customer a premium member? (boolean)
#o Coupon code entered (string)
#2. Apply discount rules:
#o If price > 5000 AND customer is premium → 20% discount
#o If coupon code is "SAVE10" OR customer is premium → 10% discount
#(Use short-circuit logic so that if the customer is premium, coupon checking
#may not be required)

Bill = {}
Bill["Customer Name"] = input("Enter your Name: ")
Bill["Product Price"] = float(input("Enter the price of the product"))
Premium_customer = input("Does the customer is an premium member ? ")
Bill["Premium_customer"] = Premium_customer.lower() == "true" 
Coupon_Code = input("Enter the coupon code")

if Coupon_Code:
    (Bill["Product Price"] > 5000 and Bill["Premium_customer"])
    Bill["Discounted_Price"] = Bill["Product Price"]*0.20
elif(Coupon_Code == "SAVE10" or Bill["Premium_customer"]):
    Bill["Discounted_Price"] = Bill["Product Price"]*.10

Final_price = Bill["Product Price"] - Bill["Discounted_Price"]
print("\nTotal_Bill: ", Bill)
print(Final_price)

