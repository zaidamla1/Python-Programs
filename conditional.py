#Conditional Statements (Decision Making Statements) : These are the statements that are used to get decision regarding user.

#if statement : This statement gets executed when a given statement returns true.

#else statement : this statement gets exeecuted when a given statement returns false

#elif statement : this statement gets executed when a given statement returns true but they can be written multiple times


# if statement 
# age = int(input("Enter Your age")) 

# if age > 18:
#     print("You can vote:)")

# print("Statement out of if block")



#else statement
# purchase = int(input("Enter Your purchase value"))

# if purchase > 3500:
#     print("You are eligible for discount")
# else:
#     print("You are not eligible")


# num = 35

# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")


# year = 2024

# if year % 400 == 0 or (year % 100 != 0 and year % 4 ==0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")



#elif statement 


# purchase = int(input("Enter Your purchase value"))

# if purchase > 5000:
#     discount = purchase * 30 / 100
#     purchase -= discount
#     print(f"Final value after 30% disocunt {purchase}")

# elif purchase > 3000:
#     discount = purchase * 20 / 100
#     purchase -= discount
#     print(f"Final value after 20% discount {purchase}")

# elif purchase > 1000:
#     discount = purchase * 10 / 100
#     purchase -= discount
#     print(f"Final value after 10% discount {purchase}")
# else:
#     print(f"Purchase value without discount {purchase}")


a = 100
b = 300
c = 2000

if a > b:
    if a > c:
        print("A is grater")
    else:
        print("C is grater")
elif b > c:
    print("B is greater")
else:
    print("C is greater")
