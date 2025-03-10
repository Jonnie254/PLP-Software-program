def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))


final_price = calculate_discount(price, discount_percent)

# Print the result
if final_price == price:
    print(f"No discount applied. The price remains: ${price:.2f}")
else:
    print(f"Discount applied! The final price is: ${final_price:.2f}")
