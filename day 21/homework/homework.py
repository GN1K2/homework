#number 1

numbers_list = []
repeat_value = []

for i in range(5):
    num = int(input("Please enter number: "))
    numbers_list.append(num)


for number in numbers_list:
    count = numbers_list.count(number)
    if count > 1 and number not in repeat_value:
        repeat_value.append(number)

print(repeat_value)

#number 2

numbers_list = []
repeat_value = []

for i in range(5):
    num = int(input("Please enter number: "))
    numbers_list.append(num)


for number in numbers_list:
    count = numbers_list.count(number)
    if count > 1 and number not in repeat_value:
        repeat_value.append(number)

print(repeat_value)