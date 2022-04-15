number = int(input())
is_prime = False

if number > 1:
    for i in range(2, int(number / 2)+ 1):
        if (number % i) == 0:
            print("False")
            break
        else:
            print("True")
            break

# else:
#     print("False")

# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             is_prime = True
#             break
# if is_prime:
#     print("True")
# else:
#     print("False")