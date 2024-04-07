"""Qn 01: 
 Create a function named calculate_discount(price, discount_percent) that calculates
 the final price after applying a discount. 
 The function should take the original price (price) and 
 the discount percentage (discount_percent) as parameters. 
 If the discount is 20% or higher, apply the discount; otherwise, return the original price."""

def calculate_discount(price, discount_percent): #function definition
    finalPrice=price-(discount_percent*price)    #calculation method
    #if..else condition applies
    if discount_percent >= 0.2:
     print('the finalPrice after discount:',finalPrice)
    else:
       print("No discount! The price is:",price)
calculate_discount(2000, 0.6) 

"""Qn 02:
Using the calculate_discount function, prompt the user to enter the original price of an item and
the discount percentage. Print the final price after applying the discount, or if no discount was applied, 
print the original price.
"""
def calculate_discount(): #function definition
    #the input statements here prompt the user to eneter the price and discount respectively
    price=float(input('Enter the price:')) 
    discount_percent=float(input('Enter the discount percent:'))

    #calculation method
    finalPrice=price-(discount_percent*price/100)   

    #if..else condition applies
    if discount_percent >= 20:
     print('the finalPrice after discount:',finalPrice)
    else:
       print("No discount! The price is:",price)

    #Function calling
calculate_discount()