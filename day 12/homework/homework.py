#number 1

budget = int(input("what is your budget: "))
cost = int(input("please enter cost: "))

if budget  >= cost:
    print("you have enough money")
else:
    print("you dont have enough money")

#nuumber 2
    
registered_password = "1234"

password = input("please enter your pasword again: ")

while password != registered_password:
    password = input("please enter your password")
    if password == registered_password:
        print("you have acces on your account")
    else:
        print("you have entered the wrong password please try again")


#number 4
        
s1 = int(input("please enter first slide: "))
s2 = int(input("please enter second slide: "))
s3= int(input("please enter third slide: "))

is_valid = (s1 + s2 > s3) and (s2 + s3 > s1) and (s3 + s1 > s2)

while is_valid != true:
    s1 = int(input("please enter first slide: "))
    s2 = int(input("please enter second slide: "))
    s3= int(input("please enter third slide: "))

    is_vlaid = s1 + s2 > s3

#number 4
    
operation = input("please enter operation (+,-,*,/)")
num1 = int(input("please enter first number: "))
num2 = int(input("please enter second number :"))

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
else:
    print("operation is not valid")