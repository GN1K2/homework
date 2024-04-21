# 1. მომხმარებელს შემოატანინეთ ნებისმიერი სიტყვა. თუ მისი სიგრძე აღემატება სამს, დაბეჭდეთ მისი პირველი სამი ასო. ხოლო თუ ნაკლებია ან ტოლი სამის, დაბეჭდეთ სიტყვის პირველი ასო.

name = input("please enter your name :")
if len(name) > 3:
    print(name[:3])
else:
    print(name[0])

# 2. for ციკლით შექმენით 10-იდან 20-ის ჩათვლით არსებული მთელი რიცხვების სია. შემდეგ გამოიყენეთ slicing, სადაც სტეპი იქნება 2-ის ტოლი.

numbers = list(range(10,20 + 1))
sliced_numbers = numbers[::2]
print(sliced_numbers)

# 3. მომხმარებელს შემოატანინეთ სიტყვა. შემდეგ გამოიყენეთ ნასწავლი მასალა და შეაბრუნეთ ის.

word = input("please enter a word :")
reversed_word = word[::-1]
print(reversed_word)


