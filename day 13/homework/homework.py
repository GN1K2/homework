#number 1

for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0: 
        print("fizz buzz")
    elif 1 % 3 == 0:
        print("fizz")
    elif 1 % 5 == 0:
        print("buzz")

#number 2

num = int(input("enter a number"))
if num > 0 :
    print("this number is possitive")
elif num < 0 :
    print("this number is negative")
else:
    print("this number is zero")

#number 3

for i in range(2, 101 ,2):
    print(i)

#number 4
    
total = 0
number = 1 
while number<=100:
    total += number
    number +=1
print("ყველა რიცხვის ჯამი 1-იდან 100-მდე არის ", total )

#number 5

day_number = int(input("enter weak day 1 to 7"))
if day_number == 1:
    print ("monday")
elif day_number == 2:
    print("tuesday")
elif day_number == 3:
    print("wensday")
elif day_number == 4:
    print("thursday")
elif day_number == 5:
    print("friday")
elif day_number == 6:
    print("saturday")
elif day_number == 7:
    print("sunday")
else:
    print("its incorect number")

#number 6
    
number = int(input("please enter your number"))
if number == 0:
    print("its 0")
elif number % 2 == 0:
    print("its even")
else:
    print("its oven")