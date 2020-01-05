# print("Hello, Daddy! Hello, Mom.")

# userInput = input("Hello to who?")
#
# print(userInput)

x = "Hello, there Aubriana!"

print(x[7:-1])
print(len(x))

quantity = 4
itemno = "zx12"
price = 19.94
orderstring = "I want {} pieces of {} item for {} dollars."
orderstringindexed = "I want to pay {2} dollars for {1} item from your website - i'll take {0}"

print(orderstring.format(quantity, itemno, price))
print(orderstringindexed.format(quantity, itemno, price))
print("I want {} number of {} item at {} per item".format(quantity, itemno, price))

print(isinstance(orderstringindexed, str))
