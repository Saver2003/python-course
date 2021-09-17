productName = input("Enter product name: ")
productQuantity = input("Enter quantity of product: ")
productPrice = input("Enter product price: ")

product2Name = input("Enter product name: ")
product2Quantity = input("Enter quantity of product: ")
product2Price = input("Enter product price: ")

product1Common = int(productPrice) * int(productQuantity)
product2Common = int(product2Price) * int(product2Quantity)

print(productName + " - x" + productQuantity + " :", product1Common) 
print(product2Name + " - x" + product2Quantity + " :", product2Common)
print("Common: ", product1Common + product2Common)
