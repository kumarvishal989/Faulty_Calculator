# Exercise - 2 Faulty Calculator Solutions
a = int(input("Enter the first number\n"))
b = int(input("Enter the Second number\n"))
c = input("Enter the Operators\n")
if a==45 and b==3 and c=='*':
    print(455)
elif a==56 and b==9 and c=='+':
    print(77)
elif a==56 and b==4 and c=='/':
    print(4)
elif c=='+':
    print("The sum of the number is:", a+b)
elif c=='-':
    print("The differnce of the number is:", a-b)
elif c=='*':
    print("The product of the number is:", a*b)
elif c=='/':
    print("The quotient of the number is:", a/b)
else:
    print("Wrong operator input")


