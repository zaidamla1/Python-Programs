#Loops : To perform certain task in repeatedly till certain condition

#while Loop : Entry Level loop. Itgets executed till the condition reaches false.

# Increment Loop
# i = 5
# while(i <= 10):
#     print(i)
#     i+=1


# Decrement Loop
# j = 10
# while(j >= 5):
#     print(j)
#     j-=1


# Odd Numbers

# a = 1

# while(a <= 20):
#     if(a % 2 != 0):
#         print(a)
#     a+=1    


#Sum of Numbers Loop
# num = 5
# a = 1
# sum = 0
# while(a <= num):
#     sum += a
#     a+=1
# print(sum)


# Factorial
# fact = 1
# while(a <= num):
#     fact *= a
#     a+=1
# print(fact)



# Reverse a Number
num = 121
flag = num
rem = 0
rev = 0
while(num > 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

print(rev)


if(flag == rev):
    print("Palindrome Number")
else:
    print("Not a Plaindrome Number")




