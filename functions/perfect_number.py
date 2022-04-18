def perfect_num_func(number):
    if number > 0:
        num_sum = 0
        for i in range(1, number + 1 // 2):
            if number % i == 0:
                num_sum += i
    if number == num_sum:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

number = int(input())
perfect_num_func(number)
