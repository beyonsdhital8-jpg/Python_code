#Identity operator
a=[1,2,3]
b=[1,2,3]
c=a
print(a is c)
print(a is c)
print(a ==b)
print(a==c)
print(id(a))
print(id(c))
print(id(a))

#assigment operator
print(5 + 3)#addition
print(2 - 1)#Substractiom
print(10/3)#Division
print(10 // 3)# Floor division: 3
print(10 % 3) # Modulus (remainder): 1
print(10 ** 3)# Exponentiation

#comparsion operator
print(1==2)
print(1!=5)
print(1>2)
print(1<2)
print(10>=10)
print(10<=11)

#assignment operator
score = 0
score += 50
score += 10
print(f"{score}")

#Logical operator
print(5 and 6)
print(5 or 6)
print(True and True)
print(True or False)
print(not True)

#5 Bitwise Operators
print(7 & 5)    
print(7 | 5)    
print(7 ^ 5)    
print(9 << 2)   
print(9 >> 1)

#Membership operator
print("py" in "python")
print("k" not in "programming")

#operator precedence
print(2 + 3 * 4)
print(5 > 3 and 2 < 4)
print((2 ** 3) ** 2)
      