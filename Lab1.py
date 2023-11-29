# a = int(input("Enter number : "))
# num = 1
# checknum = a
# checknum1 = a
# b = []
# while True:
#     for i in range(2,a):
#         if checknum1 % i == 0:
#             num *= i
#             checknum1 /= i
#             b.append(str(i))
#             break
#     if num == checknum:
#         break
# print(f"Factoring Result : {' x '.join(b)}")
# print("Press any key to continue . . .")


a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

cehck_min = min([a, b])

for i in range(cehck_min, -1, -1):
    if (a % i == 0 and b % i == 0):
        print("Greatest common divisor =", i)
        break
