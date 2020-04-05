number = 10001
simple = 1


for i in range (2,number):
    if number % i == 0:
        simple = 0

if simple == 0:
    print("Not simple")
else:
    print("Simple")

