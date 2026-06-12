#logical operators : They are used to create custom logics on the basis of product requirements

#logical AND  : Every condition given needs to be true.
#logical OR   : Any one condition needs to be true.
#logical NOT  : It reverse the answer

a = 50
b = 70
c = 50
d = 40

print(a > b and c < d)
print(b > d and c < b)

print(a < b or c > b)
print(b < a or d < a)

print(not(a > b or b < d))
print((a > b or c > d) and (a < d and b > c))
print((a > 65 or b < 70) or (b > c and c < 50))